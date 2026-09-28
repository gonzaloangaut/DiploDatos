# TP2 — Análisis exploratorio y curación

Autores: Ana Paula Cobresí, Gonzalo Angaut, Javier Albiero y Octavio Santi.

Preparación de datos de satélites para estudiar la vida útil esperada informada por UCS y explorar sus atributos orbitales. Integra fuentes por NORAD, documenta faltantes, separa conjuntos y muestra un preprocesamiento que puede ajustarse dentro de cada fold.

## Ejecutar

Desde esta carpeta, con Python 3.12:

```bash
python -m pip install -r requirements.txt
```

Abrir `TP2_Analisis_exploratorio_mentoría.ipynb` y ejecutar todas las celdas en orden. Se necesita `preprocessing.py` junto a la notebook; en Colab, subir ambos archivos y las dependencias. La primera ejecución descarga aproximadamente 49 MB desde `raw.githubusercontent.com`. Las siguientes usan el caché local excluido de Git.

Los cinco insumos se fijan al commit `1c49c73b92e84d3eba2c53f43313ed861d08f896` de [EnzoRg/space_debris](https://github.com/EnzoRg/space_debris/tree/1c49c73b92e84d3eba2c53f43313ed861d08f896/data/raw), y se verifican por SHA-256. El commit no implica una fecha común de observación. `environment.yml` documenta el entorno de la Diplomatura; `requirements.txt` describe el entorno de ejecución de esta notebook.

## Población y variable objetivo

- Sólo PAYLOAD con coincidencia UCS. Las discrepancias de tipo se cuentan antes del filtro.
- `EXPECTED_LIFETIME_YRS` conserva la vida útil esperada informada por la fuente, en años. No se imputa, escala ni incluye como predictor.
- El modelado supervisado utiliza exclusivamente filas con etiqueta válida. Las demás permanecen disponibles por separado.
- Vida útil esperada no equivale a vida operativa realizada ni a tiempo hasta reentrada.
- Los atributos corresponden al catálogo; el ejercicio estudia asociaciones en ese catálogo, no demuestra predicción al momento del lanzamiento.

## Archivos generados

| Archivo | Contenido |
|---|---|
| `TP2_DatosDeEntrenamiento.csv` | Aproximadamente 60 % de las filas etiquetadas |
| `TP2_DatosDeEvaluacion.csv` | Aproximadamente 20 %, validación |
| `TP2_DatosDePrueba.csv` | Aproximadamente 20 %, test reservado |
| `TP2_DatosSinEtiqueta.csv` | Filas sin vida útil esperada válida |
| `TP2_CatalogoCurado.csv` | Todos los PAYLOAD con coincidencia UCS |
| `TP2_manifest.json` | Fuentes, hashes, semilla, columnas, tamaños y comprobaciones |
| `TP2_ReporteExploratorioDeDatosInicial.html` | Resumen de la integración y cobertura |
| `TP2_ReporteExploratorioDeDatosFinal.html` | Particiones y diagnóstico de entrenamiento |

**Los CSV contienen datos sin imputar, codificar ni escalar.** Los faltantes de entrada son deliberados. `INFO_*` contiene metadatos de trazabilidad, excluidos del preprocesamiento mediante una lista explícita de predictores. `INFO_NO_REENTRY_RECORDED` significa ausencia de fecha registrada; no certifica actividad.

## Preprocesamiento

`make_preprocessor()` crea una instancia sin ajustar. Contiene medianas para atributos orbitales, moda y orden para RCS_SIZE, one-hot para propósito y clase orbital, agrupación de países infrecuentes, MinMaxScaler e imputación iterativa de masa con KNeighborsRegressor. Todos los parámetros aprendidos se ajustan durante `fit`; la masa se estima sin usar el target. El orden de RCS_SIZE y las distancias entre categorías son aproximaciones estadísticas, no métricas físicas. La imputación de masa requiere al menos cinco vecinos disponibles; las particiones de este dataset superan ese mínimo.

Los valores extremos físicamente posibles no se eliminan por percentiles. Los inválidos según reglas de dominio fijas pasan a faltantes y se contabilizan. Los gráficos y percentiles se calculan sobre entrenamiento. La notebook transforma validación y test para verificar el contrato de datos, sin usarlos para seleccionar modelos.

## Conexión con TP3

La notebook de TP3 existente descarga los datos históricos `jalbiero/unc-space-debris-datasets@v2.0.0`. Esos archivos y las métricas guardadas **no corresponden a esta preparación**. Antes de reevaluar TP3 se debe:

1. Leer los tres CSV de esta carpeta; comprobar `TP2_manifest.json` (`schema_version: 3`).
2. Definir las clases de vida útil con umbrales calculados sólo a partir del entrenamiento, ahora en años.
3. Pasar los atributos sin transformar a un `Pipeline` con `make_preprocessor()` y el clasificador. En `BayesSearchCV`, usar prefijos como `model__max_depth`.
4. Mantener validación para comparar propuestas y test para la evaluación final del modelo elegido.
5. Revisar también las variables y el escalado del clustering. El catálogo completo incluye los objetos reservados para test supervisado y no debe utilizarse para decidir ese modelo.

Ejemplo de construcción, para usar desde esta carpeta:

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold, cross_validate
from preprocessing import FEATURE_COLUMNS, TARGET, make_preprocessor

train = pd.read_csv('TP2_DatosDeEntrenamiento.csv')
mu, sigma = train[TARGET].mean(), train[TARGET].std()
low, high = mu - 0.5 * sigma, mu + 0.5 * sigma
y = train[TARGET].map(lambda value: 0 if value < low else 2 if value > high else 1)
pipeline = Pipeline([
    ('preprocess', make_preprocessor(random_state=42)),
    ('model', RandomForestClassifier(random_state=42, class_weight='balanced')),
])
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
# Ejecutar durante la revisión de TP3, sin reutilizar X_train_ready de TP2:
# scores = cross_validate(pipeline, train[FEATURE_COLUMNS], y, cv=cv,
#                         scoring=['roc_auc_ovr', 'f1_macro'])
```

La partición aleatoria por NORAD no separa familias de satélites ni años. Por lo tanto, una métrica alta no demuestra extrapolación a constelaciones nuevas o lanzamientos futuros. La ausencia de etiquetas también puede introducir sesgo de selección.

## Comprobaciones

La notebook verifica unicidad y separación de identificadores, cobertura completa de los registros etiquetados, preservación del target, exclusión de target/metadatos del preprocesamiento y finitud de las matrices transformadas. Verifica además cada CSV tras volver a leerlo. `python -m unittest test_preprocessing.py` comprueba aislamiento del target y comportamiento ante categorías y extremos nuevos.
