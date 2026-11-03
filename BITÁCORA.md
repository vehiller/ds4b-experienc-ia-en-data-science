# Bitácora de Desarrollo e Ingeniería del Proyecto
> **Proyecto:** ds4b-experienc-ia-en-data-science  
> **Programa:** Experienc-IA en Data Science (DS4B - Data Science 4 Business)  
> **Propósito:** Registro exhaustivo de decisiones técnicas, gobernanza de IA, configuración del entorno y evolución del ciclo de vida del dato.

---

## 1. Fundamentos Metodológicos y Marco del Programa (DS4B)

### 1.1 El Nuevo Paradigma del Data Science (Lección 6)
- **Transformación del mercado:** La irrupción de la IA Generativa ha redefinido el perfil del Data Scientist tradicional, priorizando perfiles híbridos con visión de negocio y capacidad de apalancarse en herramientas cognitivas.
- **La fórmula de valor aplicada:**
  $$\text{Problema de Negocio} \longrightarrow \text{Modelo de Machine Learning (XGBoost)} \longrightarrow \text{Aplicación Interactiva (Streamlit)}$$
- **Caso práctico del curso:** Previsión de ventas (Forecasting) para un retailer deportivo y desarrollo de un simulador de impacto en ingresos según políticas de descuentos.

### 1.2 Hoja de Ruta Formativa del Proyecto
- **Etapa 1:** Entorno de trabajo profesional, estación de trabajo con IA (VS Code / Antigravity), Miniconda y gobernanza mediante directivas.
- **Etapa 2:** Ingesta, auditoría de calidad de datos, EDA, ingeniería de variables, modelización con Machine Learning y evaluación temporal.
- **Etapa 3:** Pipeline de inferencia, construcción de interfaz con Streamlit y entrega final de producto de datos.

---

## 2. Registro Cronológico de Decisiones y Configuración Técnica

### Hito 1: Creación del Entorno Aislado Conda (`forecasting`)
- **Objetivo:** Garantizar un entorno cerrado y reproducible para evitar colisiones con el entorno base o librerías del sistema operativo.
- **Resolución de librerías iniciales:** Se definieron y depuraron los paquetes requeridos por el pipeline: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `streamlit` y `holidays` (con soporte para el calendario festivo de España).
- **Especificación de versión:** Python 3.13 sobre canal `conda-forge`.
- **Comprobación:** Creación directa del entorno `forecasting` en `C:\Users\Vehiller\miniconda3\envs\forecasting`.

### Hito 2: Configuración del Shell de PowerShell y Visibilidad del Entorno
- **Incidencia detectada:** La terminal integrada de PowerShell mostraba únicamente el prompt `PS` sin reflejar el estado activo del entorno Conda (`(base)` o `(forecasting)`).
- **Causa raíz:** Restricción de directivas de ejecución de scripts en Windows (`ExecutionPolicy Restricted`) y falta del hook de inicialización de Conda para PowerShell.
- **Solución aplicada:**
  1. Habilitación de scripts locales: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`.
  2. Inicialización de Conda en PowerShell: `conda init powershell`.
  3. Configuración del auto-activador: `conda config --set auto_activate true`.
- **Resultado:** Integración completa de la terminal con prefijo de entorno activo visible.

### Hito 3: Solución de Términos de Servicio y Registro del Kernel de Jupyter
- **Incidencia detectada:** El notebook `notebooks/entrenamiento.ipynb` no detectaba el entorno `forecasting` en el selector de kernels (*Select Kernel*). Al intentar instalar `ipykernel` vía Conda, se generó un error de bloqueo no interactivo por términos de servicio del canal comercial (`CondaToSNonInteractiveError`).
- **Solución aplicada:**
  1. Instalación desacoplada y rápida del conector mediante PyPI: `pip install ipykernel` dentro del entorno activo.
  2. Registro formal del kernelspec en el sistema:
     ```powershell
     python -m ipykernel install --user --name forecasting --display-name "Python (forecasting)"
     ```
- **Resultado:** Detección inmediata y enlace del kernel `Python (forecasting)` en `entrenamiento.ipynb`.

### Hito 4: Gobernanza del Asistente Cognitivo (`.agent/instructions.md`)
- **Adaptación arquitectónica:** En lugar de depender de `.github/copilot-instructions.md` (específico de GitHub Copilot), se configuró el equivalente nativo para Google Antigravity en `.agent/instructions.md`.
- **Reglas implementadas:**
  - Protocolo de respuesta: inicio obligatorio con 🤖 y respuesta exclusiva en español.
  - Whitelist cerrada de dependencias: prohibición de paquetes fuera de `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `holidays`, `streamlit` y librería estándar.
  - Control de variables en `df`: restricción estricta sobre la creación de columnas para evitar alucinaciones y *data leakage*.
  - Manejo de terminal: entrega de comandos para ejecución interactiva en lugar de subprocesos bloqueantes en background (especialmente para servidores como Streamlit).

### Hito 5: Configuración del Espacio de Trabajo (`.vscode/settings.json`)
- Establecimiento del intérprete por defecto a nivel de proyecto:
  ```json
  {
      "r.lsp.promptToInstall": false,
      "python.defaultInterpreterPath": "C:\\Users\\Vehiller\\miniconda3\\envs\\forecasting\\python.exe",
      "python.terminal.activateEnvironment": true
  }
  ```

### Hito 6: Normalización y Renombrado del Repositorio
- Se migró el nombre del directorio local de `DS4B` a `ds4b-experienc-ia-en-data-science` para guardar correspondencia exacta con el repositorio remoto de GitHub.
- Se verificó que la estructura de carpetas, el intérprete de Conda y las directivas del agente se mantuvieran intactos tras la reapertura del proyecto.

---

## 3. Estado de Auditoría del Entorno

- **Ruta de proyecto:** `C:\Users\Vehiller\Documents\GitHub\ds4b-experienc-ia-en-data-science`
- **Intérprete activo:** `C:\Users\Vehiller\miniconda3\envs\forecasting\python.exe`
- **Librerías verificadas y operativas:** pandas (3.1.0), scikit-learn (1.9.1), matplotlib (3.11.2), seaborn (0.13.2), streamlit (1.66.1), holidays (0.108), ipykernel.
- **Siguiente paso operativo:** Vinculación de control de versiones con GitHub y primer commit semántico de estado del arte.

