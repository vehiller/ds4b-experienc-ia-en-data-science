# Antigravity Project Instructions - DS4B Forecasting

## Protocolo de Comunicación y Rol del Asistente
- Comenzar siempre cada respuesta obligatoriamente con el emoji: 🤖
- Responder única y exclusivamente en español.
- Mantener respuestas directas, concisas y enfocadas en entregables funcionales.

## Entorno de Ejecución y Python
- Entorno Conda predeterminado: `forecasting` (ubicado en `C:\Users\Vehiller\miniconda3\envs\forecasting`).
- Para cualquier comando de Python o script que ejecutes vía herramientas, debes garantizar que se ejecute en el entorno `forecasting`, invocando directamente su ejecutable (`C:\Users\Vehiller\miniconda3\envs\forecasting\python.exe`) o usando `conda run -n forecasting <comando>`.
- No instales dependencias en el entorno `base`.

## Comportamiento con la Terminal y Comandos Largos
- Para servidores de desarrollo, dashboards interactivos o procesos continuos (como `streamlit run ...`), NO los ejecutes como subprocesos en background bloqueantes. En su lugar, entrega el bloque de comando listo para PowerShell para que el usuario lo pegue y ejecute en su propia terminal interactiva.
- Siempre que generes scripts interactivos o aplicaciones web, indica la URL local predeterminada y el comando de arranque en la terminal visible.

## Restricción Estricta del DataFrame (`df`) y Manejo de Datos
- **Restricción estricta de variables en `df`**: Trabajar y persistir únicamente las variables expresamente autorizadas por el proyecto / instructor para el modelado y forecasting en el DataFrame principal (`df`). No crear ni conservar columnas auxiliares, intermedias o de prueba sin justificación directa en el pipeline final.
- Las transformaciones deben realizarse de forma limpia y controlada, asegurando consistencia de tipos, nombres de columnas estandarizados y ausencia de data leakage.
- Rutas de datos: Siempre usar rutas relativas o `pathlib.Path` para evitar errores entre entornos (`data/raw/`, `data/processed/`, `models/`).

## Whitelist Cerrada de Librerías Permitidas
- Solo está permitido utilizar el conjunto cerrado de librerías aprobadas para el proyecto:
  1. `pandas` (manipulación y análisis de datos)
  2. `numpy` (operaciones numéricas y matrices)
  3. `scikit-learn` (modelos de ML, preprocesamiento y métricas)
  4. `matplotlib` (graficación estática)
  5. `seaborn` (visualización estadística)
  6. `holidays` (calendario y festivos de España)
  7. `streamlit` (interfaz interactiva y dashboard)
  8. `pytest` (pruebas unitarias e integración)
  9. Librerías estándar de Python (`pathlib`, `datetime`, `pickle`/`joblib`, `os`, `sys`, etc.)
- **Queda estrictamente prohibido** importar o requerir paquetes externos no contemplados en esta lista blanca sin autorización explícita.
