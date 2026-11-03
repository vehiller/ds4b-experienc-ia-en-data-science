# ds4b-experienc-ia-en-data-science

> Proyecto desarrollado dentro del programa intensivo **EXPERIENC-IA EN DATA SCIENCE** de **DS4B (Data Science 4 Business)**.  
> Caso de uso: **Forecasting de Ventas y Simulador de Descuentos para Retail Deportivo** mediante Machine Learning e Inteligencia Artificial asistida.

---

## 📌 Contexto y Propósito del Proyecto
El ecosistema del Data Science ha experimentado un cambio de paradigma impulsado por la IA Generativa. Hoy en día, el mayor valor reside en los **perfiles híbridos (técnico-negocio)** capaces de resolver problemas de negocio reales combinando metodologías de Ciencia de Datos y asistentes cognitivos de desarrollo.

Este repositorio documenta el ciclo de vida completo de un proyecto de analítica predictiva de extremo a extremo, aplicando la fórmula:
$$\text{Problema de Negocio} \longrightarrow \text{Modelo de Machine Learning} \longrightarrow \text{Aplicación Interactiva (App)}$$

---

## 🎯 Caso de Negocio: Retail Deportivo
* **Problema:** Optimizar la estimación de demanda y ventas en un retailer deportivo para anticipar compras, controlar stock y diseñar estrategias comerciales eficientes.
* **Solución de Machine Learning:** Construcción, validación y evaluación de un pipeline de *Forecasting* avanzado (basado en algoritmos de ensamble / XGBoost).
* **Entregable de Negocio:** Aplicación web interactiva desarrollada con **Streamlit** que permite a los tomadores de decisiones simular escenarios comerciales modificando variables clave como descuentos, estacionalidad y festivos.

---

## 🗺️ Metodología y Roadmap de Desarrollo (DS4B)

El proyecto sigue rigurosamente las etapas del programa profesional de DS4B:

### Etapa 1: Fundamentos y Estación de Trabajo
- Configuración del entorno profesional y gestor de paquetes con Miniconda.
- Entorno de desarrollo guiado con IA (Google Antigravity / VS Code).
- Gobernanza de IA mediante directivas estructuradas (`.agent/instructions.md`).
- Creación y registro de kernels Jupyter para el entorno aislado `forecasting`.

### Etapa 2: Análisis, Preparación y Modelización
- **Ingesta y Calidad de Datos:** Auditoría, depuración y consistencia de datos iniciales.
- **Análisis Exploratorio de Datos (EDA):** Detección de patrones temporales, correlaciones y tendencias.
- **Ingeniería de Características:** Generación de variables temporales, desfases (lags), festivos de España (`holidays`) y métricas de negocio.
- **Entrenamiento y Evaluación:** Ajuste de modelos de Machine Learning (XGBoost), validación temporal y métricas de error.

### Etapa 3: Implementación y Despliegue
- Pipeline de procesamiento para predicción sobre nuevos datos.
- Construcción y despliegue del simulador interactivo en **Streamlit**.
- Buenas prácticas de reproducibilidad, documentación y control de versiones.

---

## 🛠️ Stack Tecnológico

| Capa | Tecnologías |
| :--- | :--- |
| **Entorno & Lenguaje** | Python 3.13 (aislado en entorno Conda `forecasting`), Miniconda |
| **Manipulación & Cómputo** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn, XGBoost |
| **Visualización** | Matplotlib, Seaborn |
| **Reglas de Negocio** | Holidays (Calendario oficial de festivos en España) |
| **Interfaz & Despliegue** | Streamlit |
| **Desarrollo & IA** | Google Antigravity / VS Code, Jupyter Notebooks, Directivas de Agente (`.agent/`) |

---

## 📂 Estructura del Repositorio

```text
ds4b-experienc-ia-en-data-science/
├── .agent/               # Directivas de contexto, whitelist y comportamiento del agente IA
├── .vscode/              # Configuración del espacio de trabajo y kernel predeterminado
├── notebooks/            # Cuadernos de análisis exploratorio y modelado (entrenamiento.ipynb)
├── data/                 # Almacenamiento local estructurado (raw / processed)
├── models/               # Serialización de modelos predictivos entrenados
├── app/                  # Código fuente de la aplicación interactiva de simulación (Streamlit)
├── BITÁCORA.md           # Registro exhaustivo de auditoría técnica y configuración paso a paso
└── README.md             # Vitrina y documentación ejecutiva del proyecto
```

---

## ⚙️ Estándares de Ingeniería y Gobernanza
* **Aislamiento Estricto:** Entorno dedicado para evitar colisiones de dependencias globales.
* **Gobernanza del Asistente:** Whitelist de librerías y control explícito de variables del DataFrame (`df`) para prevenir alucinaciones de código y fugas de datos (*data leakage*).
* **Portabilidad Total:** Uso de rutas relativas con `pathlib.Path` y código reproducible.

