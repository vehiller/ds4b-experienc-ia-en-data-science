# Bitácora de Desarrollo e Ingeniería del Proyecto
> **Proyecto:** ds4b-experienc-ia-en-data-science  
> **Programa:** Experienc-IA en Data Science (DS4B - Data Science 4 Business)  
> **Fecha de Creación del Repositorio:** 8 de Noviembre de 2026  
> **Fecha de Última Actualización:** 21 de Noviembre de 2026  
> **Propósito:** Registro exhaustivo de decisiones técnicas, gobernanza de IA, configuración del entorno y evolución del ciclo de vida del dato.

---

## 1. Fundamentos Metodológicos y Marco del Programa (DS4B)

### 1.1 El Nuevo Paradigma del Data Science (Lección 6)
- **Transformación del mercado:** La irrupción de la IA Generativa ha redefinido el perfil del Data Scientist tradicional, priorizando perfiles híbridos con visión de negocio y capacidad de apalancarse en herramientas cognitivas.
- **La fórmula de valor aplicada:**
  Problema de Negocio -> Modelo de Machine Learning (XGBoost) -> Aplicación Interactiva (Streamlit)
- **Caso práctico del curso:** Previsión de ventas (Forecasting) para un retailer deportivo y desarrollo de un simulador de impacto en ingresos según políticas de descuentos.

### 1.2 Hoja de Ruta Formativa del Proyecto
- **Etapa 1:** Entorno de trabajo profesional, estación de trabajo con IA, Miniconda y gobernanza mediante directivas.
- **Etapa 2:** Ingesta, auditoría de calidad de datos, EDA, ingeniería de variables, modelización con Machine Learning y evaluación temporal.
- **Etapa 3:** Pipeline de inferencia, construcción de interfaz con Streamlit y entrega final de producto de datos.

---

## 2. Registro Cronológico de Decisiones y Configuración Técnica (Fase Inicial - Antes del 17/11/2026)

### Hito 1: Creación del Entorno Aislado Conda (forecasting)
- **Objetivo:** Garantizar un entorno cerrado y reproducible para evitar colisiones con el entorno base o librerías del sistema operativo.
- **Resolución de librerías iniciales:** Se definieron y depuraron los paquetes requeridos por el pipeline: pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit y holidays (con soporte para el calendario festivo de España).
- **Especificación de versión:** Python 3.13 sobre canal conda-forge.
- **Comprobación:** Creación directa del entorno forecasting en C:\Users\Vehiller\miniconda3\envs\forecasting.

### Hito 2: Configuración del Shell de PowerShell y Visibilidad del Entorno
- **Incidencia detectada:** La terminal integrada de PowerShell mostraba únicamente el prompt PS sin reflejar el estado activo del entorno Conda ((base) o (forecasting)).
- **Causa raíz:** Restricción de directivas de ejecución de scripts en Windows (ExecutionPolicy Restricted) y falta del hook de inicialización de Conda para PowerShell.
- **Solución aplicada:**
  1. Habilitación de scripts locales: Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser.
  2. Inicialización de Conda en PowerShell: conda init powershell.
  3. Configuración del auto-activador: conda config --set auto_activate true.
- **Resultado:** Integración completa de la terminal con prefijo de entorno activo visible.

### Hito 3: Solución de Términos de Servicio y Registro del Kernel de Jupyter
- **Incidencia detectada:** El notebook notebooks/entrenamiento.ipynb no detectaba el entorno forecasting en el selector de kernels (Select Kernel). Al intentar instalar ipykernel vía Conda, se generó un error de bloqueo no interactivo por términos de servicio del canal comercial (CondaToSNonInteractiveError).
- **Solución aplicada:**
  1. Instalación desacoplada y rápida del conector mediante PyPI: pip install ipykernel dentro del entorno activo.
  2. Registro formal del kernelspec en el sistema:
     python -m ipykernel install --user --name forecasting --display-name "Python (forecasting)"
- **Resultado:** Detección inmediata y enlace del kernel Python (forecasting) en entrenamiento.ipynb.

### Hito 4: Gobernanza del Asistente Cognitivo (.agent/instructions.md)
- **Adaptación arquitectónica:** En lugar de depender de .github/copilot-instructions.md (específico de GitHub Copilot), se configuró el equivalente nativo para Google Antigravity en .agent/instructions.md.
- **Reglas implementadas:**
  - Protocolo de respuesta: inicio obligatorio con el emoji de robot y respuesta exclusiva en español.
  - Whitelist cerrada de dependencias: prohibición de paquetes fuera de pandas, numpy, scikit-learn, matplotlib, seaborn, holidays, streamlit y librería estándar.
  - Control de variables en df: restricción estricta sobre la creación de columnas para evitar alucinaciones y data leakage.
  - Manejo de terminal: entrega de comandos para ejecución interactiva en lugar de subprocesos bloqueantes en background (especialmente para servidores como Streamlit).

### Hito 5: Configuración del Espacio de Trabajo (.vscode/settings.json)
- Establecimiento del intérprete por defecto a nivel de proyecto:
  {
      "r.lsp.promptToInstall": false,
      "python.defaultInterpreterPath": "C:\\Users\\Vehiller\\miniconda3\\envs\\forecasting\\python.exe",
      "python.terminal.activateEnvironment": true
  }

### Hito 6: Normalización y Renombrado del Repositorio
- Se migró el nombre del directorio local de DS4B a ds4b-experienc-ia-en-data-science para guardar correspondencia exacta con el repositorio remoto de GitHub.
- Se verificó que la estructura de carpetas, el intérprete de Conda y las directivas del agente se mantuvieran intactos tras la reapertura del proyecto.

### Hito 7: Inicialización del Repositorio Local y Primer Commit Semántico
- **Control de versiones local:** Inicialización del repositorio Git local (git init) y preparación de la rama main.
- **Commit fundacional:** Creación del primer commit semántico (95201cd) registrando la arquitectura inicial del proyecto, directivas del agente, entorno Conda y documentación técnica.

### Hito 8: Aislamiento de Identidad Git y Sincronización Remota vía Token (Classic)
- **Gestión multi-cuenta:** Para prevenir colisiones con otras cuentas activas en el sistema, se aislaron las credenciales a nivel local mediante un Personal Access Token (classic) con ámbito exclusivo repo.
- **Fijación de autoría:** Configuración explícita de user.name ("vehiller") y user.email para este repositorio.
- **Sincronización:** Publicación exitosa de la rama main hacia el repositorio remoto https://github.com/vehiller/ds4b-experienc-ia-en-data-science.git, transfiriendo los 27 objetos de la arquitectura inicial.

---

## 3. Migración Estratégica y Reconfiguración (Realizada el 17 de Noviembre de 2026)

Los siguientes hitos documentan la transición desde el stack inicial (Conda + Antigravity) hacia el stack definitivo (venv + Python 3.12.8 + Continue + Abacus.ai) ejecutada el 17/11/2026.

### Hito 9: Transición y Reconfiguración del Asistente Cognitivo
- **Motivación:** Imposibilidad de contratar la suscripción de GitHub Copilot debido a las restricciones geográficas y de políticas de pago que GitHub aplica en Venezuela, lo que impide procesar el pago desde esta región. Esto obligó a buscar una alternativa compatible con la suscripción existente a Abacus.ai para mantener la asistencia de IA en VS Code.
- **Solución adoptada:** Instalación de la extensión Continue vinculada vía API a la suscripción de Abacus.ai.
- **Configuración del entorno:**
  - Se configuró config.yaml con el proveedor openai, modelo route-llm y apiBase apuntando a https://routellm.abacus.ai/v1.
  - Se definieron dos roles: chat y edit para el modelo principal, y autocomplete para un segundo modelo.
  - **Incidencia resuelta:** Se detectó un error 404 en el endpoint /v1/completions de Abacus, lo que impide el autocompletado de código. Se optó por desactivar el rol autocomplete para evitar el error, manteniendo el chat y la edición funcionales.

### Hito 10: Reconstrucción del Entorno con venv y Python 3.12.8
- **Motivación:** El instructor del curso utiliza Python 3.12.8, por lo que se decidió estandarizar el entorno a esa versión para garantizar compatibilidad con los notebooks y el flujo del curso.
- **Proceso de migración:**
  1. Verificación de la instalación local de Python 3.12.8 mediante py -0p y py -3.12 --version.
  2. Creación del entorno virtual con el comando: py -3.12 -m venv venv.
  3. Verificación de la creación exitosa: venv\Scripts\python.exe --version (devolvió Python 3.12.8).
  4. Activación en PowerShell: .\venv\Scripts\Activate.ps1 (con bypass de política de ejecución si era necesario).
- **Instalación de dependencias:**
  - Se intentó instalar las librerías con pip install pandas numpy matplotlib seaborn scikit-learn jupyter streamlit holidays.
  - **Incidencia:** Fallo por timeout de red durante la descarga de pandas.
  - **Solución:** Reintento con --default-timeout=120 --retries 10, que completó la instalación exitosamente.
  - **Verificación:** pip list confirmó la presencia de los 8 paquetes requeridos y sus dependencias.

### Hito 11: Configuración del Kernel del Notebook
- **Problema:** El notebook no reconocía el entorno venv como kernel válido.
- **Solución:** Se seleccionó manualmente el kernel Python 3.12.8 (correspondiente al venv) en la esquina superior derecha del notebook, tras hacer clic en "Select Kernel" y elegir "Python Environments...".
- **Resultado:** El notebook ejecuta correctamente las celdas de importación y carga de datos.

### Hito 12: Implementación de Reglas de Gobernanza para Continue (.continue/rules/project-rules.md)
- **Motivación:** Replicar la gobernanza que se tenía con Antigravity y GitHub Copilot, pero adaptada al mecanismo nativo de Continue.
- **Ubicación:** Se creó la carpeta .continue/rules/ y el archivo project-rules.md.
- **Contenido de las reglas:**
  - Inicio obligatorio con el emoji de robot y respuesta en español.
  - Lista blanca cerrada de librerías permitidas (pandas, numpy, matplotlib, seaborn, scikit-learn, jupyter, streamlit, holidays).
  - Restricción estricta de variables en el DataFrame df (con marcador de posición para futuras variables autorizadas).
  - Prohibición de ejecutar celdas del notebook automáticamente; el usuario debe presionar Play.
  - Entrega de comandos para procesos largos (Streamlit) en lugar de ejecución en background.
- **Verificación:** Se confirmó que Continue reconoce las reglas al iniciar una conversación con el emoji de robot y responder en español.

### Hito 13: Actualización de la Bitácora y Sincronización Final (17/11/2026)
- **Estado actual:** Entorno venv con Python 3.12.8 operativo, Continue configurado con Abacus.ai y reglas de gobernanza activas, notebook listo para la Etapa 2 (Ingesta y Calidad de Datos).
- **Sincronización:** Pendiente de commit y push a GitHub con los cambios de esta bitácora.

---

## 4. Estado de Auditoría del Entorno (Actualizado a 17/11/2026)

- **Ruta de proyecto:** C:\Users\Vehiller\Documents\GitHub\ds4b-experienc-ia-en-data-science
- **Intérprete activo:** .\venv\Scripts\python.exe (Python 3.12.8)
- **Librerías verificadas y operativas:** pandas (3.1.1), numpy (2.5.5), scikit-learn (1.9.1), matplotlib (3.11.2), seaborn (0.13.2), streamlit (1.67.0), holidays (0.108), jupyter (1.1.1).
- **Control de versiones:** Repositorio sincronizado en GitHub (main -> origin/main) a la espera de este commit.
- **Estado operativo:** Estación de trabajo y entorno cerrados y 100% operativos, listos para la Etapa 2 del programa (Ingesta y Calidad de Datos).

---

## 5. Avances del 18 de Noviembre de 2026

### Hito 14: Gobernanza de GitHub Copilot en el Repositorio
- **Configuración incorporada:** Se agregó el archivo `.github/instructions.md` para establecer instrucciones persistentes del asistente dentro del repositorio.
- **Directrices registradas:**
  - Respuesta obligatoria con el emoji de robot y en idioma español.
  - Uso exclusivo de pandas, numpy, matplotlib, seaborn, scikit-learn, jupyter, streamlit y holidays.
  - Restricción de variables adicionales del DataFrame `df` hasta definirlas explícitamente en el código generado.
- **Resultado:** El entorno dispone de reglas de gobernanza específicas también para GitHub Copilot, alineadas con las políticas ya aplicadas al flujo de trabajo del proyecto.

### Hito 15: Inicio del Análisis Exploratorio en el Notebook
- **Archivo preparado:** Se creó el notebook `notebooks/entrenamiento.ipynb` y se configuró con el kernel `venv (3.12.8)`.
- **Entorno técnico habilitado:** Se cargaron las librerías principales para análisis y modelado: pandas, numpy, matplotlib, seaborn, scikit-learn, Streamlit y holidays.
- **Carga de datos:** Se incorporó la lectura desde `data/raw/entrenamiento/ventas.csv` y `data/raw/entrenamiento/competencia.csv`.
- **Verificación realizada:** Se mostraron las primeras filas de ambos conjuntos de datos y se confirmó que el notebook ejecuta correctamente la carga inicial.
- **Estado de la tarea:** La base técnica y el punto de partida del análisis están listos para continuar con la etapa de ingesta, auditoría de calidad y análisis exploratorio.

---

## 6. Ingesta, Calidad e Integración de Datos (19 de Noviembre de 2026)

### Hito 16: Carga Tipada y Auditoría de Calidad de los Datos
- **Carga de archivos:** Se configuró la lectura de `ventas.csv` y `competencia.csv` desde las rutas relativas de `notebooks`, interpretando `fecha` como tipo datetime.
- **Auditoría de `ventas_df`:** Se revisaron dimensiones, tipos, nulos, duplicados, unicidad de la clave fecha-producto, cobertura por fecha, valores no positivos, descriptivos, valores atípicos IQR y consistencia entre unidades, precio de venta e ingresos.
- **Auditoría de `competencia_df`:** Se aplicaron controles equivalentes, incluyendo precios no positivos, estadísticas descriptivas, valores atípicos IQR y correspondencia de claves con `ventas_df`.
- **Resultados verificados:** Ambos conjuntos contienen 3.552 filas; no presentan nulos, duplicados ni fechas no convertibles. Hay 24 productos en cada una de las 148 fechas y las claves fecha-producto coinciden entre ambos archivos.
- **Hallazgos para seguimiento:** Los controles IQR señalan posibles valores extremos, que deben evaluarse por producto y contexto comercial. También se identificaron precios de venta superiores al precio base en algunos registros; no se modificaron ni eliminaron datos sin confirmación de reglas de negocio.

### Hito 17: Integración de Ventas y Precios de Competencia
- **DataFrame integrado:** Se creó `df` mediante una unión interna (`inner`) de `ventas_df` y `competencia_df` por `fecha` y `producto_id`, con validación de relación uno a uno.
- **Resultado:** La integración conserva las 3.552 observaciones coincidentes y produce un DataFrame de 13 columnas.
- **Validación del notebook:** Se ejecutaron las celdas para actualizar las salidas y comprobar el resultado de la unión. También se corrigieron las importaciones sin uso detectadas en el panel `Problems`, que quedó sin errores.
- **Gobernanza del proyecto:** Se ampliaron las instrucciones de `.github/instructions.md` con los esquemas de columnas de `ventas_df` y `competencia_df` para orientar el trabajo posterior.

## 7. Análisis Exploratorio de Datos (EDA) y Visualización (20 de Noviembre de 2026)

### Hito 18: Análisis Exploratorio y Creación de Gráficos
- **Análisis Temporal:** Implementación de gráficos de líneas temporales segmentados por año, mostrando la suma de unidades vendidas y destacando los picos de ventas en los días de Black Friday.
- **Estacionalidad y Categorías:** Generación de gráficos de barras para analizar la distribución de ventas por día de la semana, así como el rendimiento por categoría y subcategoría de productos.
- **Análisis de Productos:** Identificación y visualización de los Top Productos con mayor volumen de ventas.
- **Análisis de Densidad de Precios:** Gráfico de densidad (KDE) comparativo entre los precios de venta propios y los precios de Amazon (competencia) para evaluar la posición de mercado.
- **Refinamiento Visual:** Optimización estética de todos los gráficos utilizando la librería Seaborn, aplicando paletas de colores diferenciadas por barra para mejorar la legibilidad y presentación profesional del entregable.
- **Estructura del Notebook:** Organización de cada análisis en celdas independientes dentro del archivo `entrenamiento.ipynb` para mantener la modularidad y facilitar la revisión.

## 8. Ingeniería de Variables y Preparación para el Modelado (21 de Noviembre de 2026)

### Hito 19: Feature Engineering, Codificación y Exportación del Dataset
- **Variables Temporales y Calendario:** Se implementó un bloque de ingeniería de variables temporales utilizando `holidays` para España. Se crearon variables como año, mes, día, día de la semana, trimestre, semana ISO, y variables cíclicas (senos y cosenos) para meses y días. Además, se identificaron de forma dinámica los días de Black Friday, Cyber Monday y la campaña de Black Friday para cada año.
- **Variables de Descuento:** Se calculó el porcentaje de descuento aplicado sobre el precio base (`descuento_porcentaje`).
- **Variables de Competencia:** Se integraron los precios de Amazon, Decathlon y Deporvillage para calcular el precio promedio de la competencia (`precio_competencia`) y el ratio de competitividad de nuestro precio frente al mercado (`ratio_precio`). Posteriormente, se eliminaron las columnas individuales de los competidores para evitar redundancia.
- **Variables Históricas (Lags):** Se generaron los lags de ventas (del 1 al 7) y una media móvil de 7 días, agrupando por producto y año. Se aplicó un `shift(1)` en la media móvil para evitar el *data leakage* (fuga de información). Finalmente, se eliminaron las filas con historial incompleto.
- **Codificación One-Hot Encoding:** Se aplicó la técnica de One-Hot Encoding a las variables categóricas de identidad (`nombre`, `categoria`, `subcategoria`). Se generaron copias con sufijo `_h` para preservar los textos originales y se crearon las columnas binarias (0s y 1s) necesarias para que `scikit-learn` pueda procesar los datos.
- **Exportación del Dataset:** Se consolidó el DataFrame final con todas las variables integradas y se exportó a la ruta `data/processed/df.csv` utilizando `pathlib` para garantizar la portabilidad de las rutas y `encoding='utf-8'` para preservar los caracteres especiales.
