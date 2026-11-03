import pathlib
import streamlit as st

st.set_page_config(
    page_title="ML App",
    page_icon="🤖",
    layout="wide",
)

ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent
DATA_PROCESSED_DIR = ROOT_DIR / "data" / "processed"
MODELS_DIR = ROOT_DIR / "models"


def main():
    st.title("🤖 Aplicación de Machine Learning")
    st.markdown(
        "Interfaz interactiva para explorar datos procesados y ejecutar predicciones con los modelos entrenados."
    )

    with st.sidebar:
        st.header("Navegación")
        seccion = st.radio(
            "Selecciona una vista:",
            ["Inicio", "Exploración de Datos", "Predicción"],
        )

    if seccion == "Inicio":
        st.subheader("Estado del Proyecto")
        col1, col2 = st.columns(2)
        modelos = list(MODELS_DIR.glob("*.pkl")) + list(MODELS_DIR.glob("*.joblib"))
        datasets = list(DATA_PROCESSED_DIR.glob("*.csv")) + list(DATA_PROCESSED_DIR.glob("*.parquet"))

        col1.metric("Datos procesados disponibles", len(datasets))
        col2.metric("Modelos serializados", len(modelos))

    elif seccion == "Exploración de Datos":
        st.subheader("📊 Datos Procesados")
        st.info("Coloca tus archivos `.csv` o `.parquet` en `data/processed/` para visualizarlos aquí.")

    elif seccion == "Predicción":
        st.subheader("🎯 Inferencia del Modelo")
        st.info("Guarda tu modelo entrenado en `models/` para habilitar las predicciones en tiempo real.")


if __name__ == "__main__":
    main()

