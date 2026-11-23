from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# ----------------------------------------------------------------------------
# Configuración
# ----------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "models" / "modelo_final.joblib"
DATA_PATH = ROOT / "data" / "processed" / "inferencia_df_trasnformado.csv"

COLOR_1 = "#667eea"
COLOR_2 = "#764ba2"
COLOR_BF = "#e63946"

DIAS_ES = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
ESCENARIOS = {
    "Actual (0%)": 1.00,
    "Competencia -5%": 0.95,
    "Competencia +5%": 1.05,
}
LAGS = [f"unidades_lag_{k}" for k in range(1, 8)]
PREFIJO_PRODUCTO = "nombre_h_"
DIA_BF = 28

st.set_page_config(
    page_title="Simulador de Ventas Noviembre 2025",
    page_icon="📈",
    layout="wide",
)

st.markdown(
    f"""
    <style>
    .main-header {{
        background: linear-gradient(135deg, {COLOR_1} 0%, {COLOR_2} 100%);
        padding: 1.6rem 2rem; border-radius: 14px; color: white;
        margin-bottom: 1.2rem;
    }}
    .main-header h1 {{ color: white; margin: 0; font-size: 2rem; }}
    .main-header p {{ margin: .3rem 0 0 0; opacity: .9; }}
    div[data-testid="stMetric"] {{
        background: #f6f7ff; border-left: 5px solid {COLOR_1};
        padding: 14px 16px; border-radius: 10px;
        box-shadow: 0 2px 6px rgba(102,126,234,.15);
    }}
    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] div {{ color: #2b2d42 !important; }}
    div.stButton > button {{
        width: 100%; height: 3.2rem; font-size: 1.1rem; font-weight: 600;
        color: white; border: none; border-radius: 10px;
        background: linear-gradient(135deg, {COLOR_1} 0%, {COLOR_2} 100%);
    }}
    div.stButton > button:hover {{ color: white; opacity: .9; }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ----------------------------------------------------------------------------
# Carga de recursos
# ----------------------------------------------------------------------------
@st.cache_resource(show_spinner=False)
def cargar_modelo(path: Path):
    return joblib.load(path)


@st.cache_data(show_spinner=False)
def cargar_datos(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, encoding="utf-8")


def obtener_productos(df: pd.DataFrame) -> dict:
    """Mapa nombre_producto -> columna one-hot nombre_h_*."""
    cols = [c for c in df.columns if c.startswith(PREFIJO_PRODUCTO)]
    return {c[len(PREFIJO_PRODUCTO):]: c for c in sorted(cols)}


# ----------------------------------------------------------------------------
# Formato
# ----------------------------------------------------------------------------
def fmt_eur(valor: float) -> str:
    """Formato moneda europeo: 1.234,56 €"""
    s = f"{valor:,.2f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{s} €"


def fmt_uds(valor: float) -> str:
    return f"{valor:,.0f}".replace(",", ".")


# ----------------------------------------------------------------------------
# Lógica de simulación
# ----------------------------------------------------------------------------
def preparar_producto(df: pd.DataFrame, col_producto: str, ajuste_desc: float,
                      factor_comp: float) -> pd.DataFrame:
    """Filtra el producto y recalcula precio_venta, precio_competencia,
    descuento_porcentaje y ratio_precio según los controles."""
    d = df[df[col_producto] == 1].sort_values("dia_mes").reset_index(drop=True).copy()

    # descuento_porcentaje está en puntos porcentuales (negativo = rebaja).
    # Slider positivo = más descuento (precio más bajo); 0 reproduce el CSV.
    d["descuento_porcentaje"] = d["descuento_porcentaje"] - ajuste_desc
    d["precio_venta"] = d["precio_base"] * (1 + d["descuento_porcentaje"] / 100.0)
    d["precio_competencia"] = d["precio_competencia"] * factor_comp
    d["ratio_precio"] = d["precio_venta"] / d["precio_competencia"]
    return d


def predecir_recursivo(modelo, d: pd.DataFrame) -> np.ndarray:
    """Predicción día a día actualizando lags y media móvil con predicciones."""
    columnas = list(modelo.feature_names_in_)
    n = len(d)
    preds = np.zeros(n)

    # Lags del día 1 tal cual vienen en el archivo: [lag_1, ..., lag_7]
    lags = [float(d.loc[0, c]) for c in LAGS]

    for i in range(n):
        if i > 0:
            # lag_k <- lag_{k-1}; lag_1 <- predicción del día anterior
            lags = [preds[i - 1]] + lags[:6]
        fila = d.loc[[i], columnas].copy().astype(float)
        for k, c in enumerate(LAGS):
            fila[c] = lags[k]
        fila["media_movil_7_dias"] = float(np.mean(lags))
        preds[i] = max(0.0, float(modelo.predict(fila)[0]))

    return preds


def simular(modelo, df, col_producto, ajuste_desc, factor_comp) -> pd.DataFrame:
    d = preparar_producto(df, col_producto, ajuste_desc, factor_comp)
    preds = predecir_recursivo(modelo, d)
    res = pd.DataFrame({
        "dia_mes": d["dia_mes"].astype(int),
        "dia_semana": d["dia_semana"].astype(int),
        "precio_venta": d["precio_venta"],
        "precio_competencia": d["precio_competencia"],
        "descuento_porcentaje": d["descuento_porcentaje"],
        "unidades": preds,
    })
    res["ingresos"] = res["unidades"] * res["precio_venta"]
    return res


# ----------------------------------------------------------------------------
# Gráficos y tablas
# ----------------------------------------------------------------------------
def grafico_prediccion(res: pd.DataFrame):
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(11, 4.6))
    sns.lineplot(data=res, x="dia_mes", y="unidades", color=COLOR_1,
                 linewidth=2.8, marker="o", markersize=5, ax=ax)

    bf = res[res["dia_mes"] == DIA_BF]
    ax.axvline(DIA_BF, color=COLOR_BF, linestyle="--", linewidth=1.8, alpha=0.8)
    if not bf.empty:
        y_bf = float(bf["unidades"].iloc[0])
        sns.scatterplot(data=bf, x="dia_mes", y="unidades", color=COLOR_BF,
                        s=170, zorder=5, ax=ax, legend=False)
        ax.annotate(
            f"Black Friday\n{y_bf:.0f} uds",
            xy=(DIA_BF, y_bf),
            xytext=(DIA_BF - 7, y_bf + res["unidades"].max() * 0.08),
            fontsize=11, fontweight="bold", color=COLOR_BF,
            arrowprops=dict(arrowstyle="->", color=COLOR_BF, lw=1.5),
        )

    ax.set_xlim(0.5, 30.5)
    ax.set_xticks(range(1, 31))
    ax.set_ylim(0, res["unidades"].max() * 1.25 + 1)
    ax.set_xlabel("Día de noviembre 2025")
    ax.set_ylabel("Unidades predichas")
    ax.set_title("Predicción diaria de unidades vendidas", fontsize=13,
                 color=COLOR_2, fontweight="bold")
    sns.despine()
    fig.tight_layout()
    return fig


def tabla_detalle(res: pd.DataFrame) -> pd.DataFrame:
    fechas = pd.to_datetime(
        pd.DataFrame({"year": 2025, "month": 11, "day": res["dia_mes"]})
    )
    t = pd.DataFrame({
        "Fecha": fechas.dt.strftime("%d/%m/%Y"),
        "Día": res["dia_semana"].map(lambda x: DIAS_ES[int(x)]),
        "Precio venta (€)": res["precio_venta"].round(2),
        "Precio competencia (€)": res["precio_competencia"].round(2),
        "Descuento (%)": res["descuento_porcentaje"].round(1),
        "Unidades": res["unidades"].round(0).astype(int),
        "Ingresos (€)": res["ingresos"].round(2),
    })
    t.loc[(res["dia_mes"] == DIA_BF).values, "Fecha"] += " 🛍️ BF"
    return t


def resaltar_bf(fila):
    if "🛍️" in str(fila["Fecha"]):
        return ["background-color: #ffe3e6; font-weight: bold; color: #7a1020"] * len(fila)
    return [""] * len(fila)


# ----------------------------------------------------------------------------
# Carga y validaciones
# ----------------------------------------------------------------------------
try:
    modelo = cargar_modelo(MODEL_PATH)
    df = cargar_datos(DATA_PATH)
except Exception as e:
    st.error(f"❌ No se pudieron cargar el modelo o los datos: {e}")
    st.stop()

faltan = [c for c in modelo.feature_names_in_ if c not in df.columns]
if faltan:
    st.error(f"❌ Faltan columnas esperadas por el modelo: {faltan}")
    st.stop()

productos = obtener_productos(df)
if not productos:
    st.error("❌ No se encontraron columnas de producto (nombre_h_*) en los datos.")
    st.stop()

# ----------------------------------------------------------------------------
# Sidebar
# ----------------------------------------------------------------------------
with st.sidebar:
    st.title("⚙️ Controles de Simulación")
    producto = st.selectbox("🛒 Producto", list(productos.keys()))
    ajuste = st.slider(
        "💸 Ajuste de descuento (%)",
        min_value=-50,
        max_value=50,
        value=0,
        step=5,
        help="Positivo = más descuento (precio más bajo). Negativo = subir precio.",
    )
    escenario = st.radio(
        "🏁 Escenario de competencia",
        list(ESCENARIOS.keys()),
        index=0,
    )
    st.markdown("---")
    simular_click = st.button("🚀 Simular Ventas")

# ----------------------------------------------------------------------------
# Estado de la simulación
# ----------------------------------------------------------------------------
if simular_click:
    with st.spinner("Calculando predicciones recursivas día a día..."):
        try:
            col_prod = productos[producto]
            res_main = simular(modelo, df, col_prod, ajuste, ESCENARIOS[escenario])
            res_esc = {
                nombre: simular(modelo, df, col_prod, ajuste, factor)
                for nombre, factor in ESCENARIOS.items()
            }
            st.session_state["resultado"] = {
                "producto": producto,
                "ajuste": ajuste,
                "escenario": escenario,
                "main": res_main,
                "escenarios": res_esc,
            }
        except Exception as e:
            st.error(f"❌ Error durante la simulación: {e}")
            st.stop()

# ----------------------------------------------------------------------------
# Zona principal
# ----------------------------------------------------------------------------
if "resultado" not in st.session_state:
    st.markdown(
        """
        <div class="main-header">
            <h1>📈 Simulador de Ventas · Noviembre 2025</h1>
            <p>Predicción recursiva con HistGradientBoostingRegressor</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.info("👈 Selecciona un producto, ajusta el descuento y el escenario de "
            "competencia en la barra lateral, y pulsa **Simular Ventas**.")
    st.stop()

r = st.session_state["resultado"]
res = r["main"]

st.markdown(
    f"""
    <div class="main-header">
        <h1>📈 Simulación de Ventas · Noviembre 2025</h1>
        <p>🛒 <b>{r['producto']}</b> &nbsp;|&nbsp; Ajuste de descuento: {r['ajuste']:+d}%
        &nbsp;|&nbsp; {r['escenario']}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# KPIs
total_uds = res["unidades"].sum()
total_ing = res["ingresos"].sum()
precio_medio = res["precio_venta"].mean()
desc_medio = res["descuento_porcentaje"].mean()

k1, k2, k3, k4 = st.columns(4)
k1.metric("📦 Unidades totales", fmt_uds(total_uds))
k2.metric("💶 Ingresos proyectados", fmt_eur(total_ing))
k3.metric("🏷️ Precio promedio de venta", fmt_eur(precio_medio))
k4.metric("🎯 Descuento promedio", f"{desc_medio:.1f}%")

st.markdown("---")

# Gráfico
st.subheader("📊 Predicción diaria de unidades")
fig = grafico_prediccion(res)
st.pyplot(fig)
plt.close(fig)

st.markdown("---")

# Tabla
st.subheader("📋 Detalle diario")
tabla = tabla_detalle(res)
st.dataframe(
    tabla.style.apply(resaltar_bf, axis=1).format({
        "Precio venta (€)": "{:.2f}",
        "Precio competencia (€)": "{:.2f}",
        "Descuento (%)": "{:.1f}",
        "Unidades": "{:.0f}",
        "Ingresos (€)": "{:,.2f}",
    }),
    use_container_width=True,
    hide_index=True,
    height=600,
)

st.markdown("---")

# Comparativa de escenarios
st.subheader("⚖️ Comparativa de escenarios de competencia")
st.caption("Se mantiene tu ajuste de descuento; solo varía el precio de la competencia.")

base_uds = r["escenarios"]["Actual (0%)"]["unidades"].sum()
base_ing = r["escenarios"]["Actual (0%)"]["ingresos"].sum()

cols = st.columns(len(ESCENARIOS))
for col, (nombre, res_e) in zip(cols, r["escenarios"].items()):
    uds = res_e["unidades"].sum()
    ing = res_e["ingresos"].sum()
    with col:
        st.markdown(f"**{nombre}**")
        if nombre == "Actual (0%)":
            st.metric("Unidades totales", fmt_uds(uds))
            st.metric("Ingresos", fmt_eur(ing))
        else:
            st.metric("Unidades totales", fmt_uds(uds),
                      delta=f"{uds - base_uds:+,.0f}".replace(",", "."))
            st.metric("Ingresos", fmt_eur(ing),
                      delta=fmt_eur(ing - base_ing))

st.markdown("---")
st.caption("Modelo: HistGradientBoostingRegressor · Predicción recursiva de 30 días · "
           "Datos: inferencia_df_trasnformado.csv")