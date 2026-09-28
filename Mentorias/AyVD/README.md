# TP1 — Análisis y visualización de objetos espaciales

Autores del trabajo original: Ana Paula Cobresí, Gonzalo Angaut, Javier Albiero y Octavio Santi.

Revisión de la notebook original de la mentoría. Conserva sus secciones y análisis; corrige el alcance de las interpretaciones, los rótulos y algunas visualizaciones.

## Ejecutar

Desde esta carpeta, en un entorno Python 3.12:

```bash
python -m pip install -r requirements.txt
```

Abrir `TP1_Análisis_y_Visualización_mentoría.ipynb` en Jupyter, Colab o un editor compatible y ejecutar todas las celdas en orden. En Colab se puede instalar con `%pip install -r requirements.txt` después de subir este archivo, o instalar directamente pandas, numpy, matplotlib, seaborn y openpyxl.

La primera ejecución descarga cinco archivos (aproximadamente 49 MB) y requiere acceso a `raw.githubusercontent.com`. Se guardan en `data/raw/<commit>/`, excluido de Git. Las siguientes ejecuciones reutilizan esa copia. Se conserva también el `environment.yml` original como referencia del entorno del trabajo.

## Fuentes y alcance

Los datos quedan fijados al commit `1c49c73b92e84d3eba2c53f43313ed861d08f896` de [EnzoRg/space_debris](https://github.com/EnzoRg/space_debris/tree/1c49c73b92e84d3eba2c53f43313ed861d08f896/data/raw). Esto conserva los archivos de entrada; no convierte la fecha del commit en fecha de observación.

- Cada fila es un objeto catalogado; el catálogo incluye reentradas registradas.
- Un objeto no-DEBRIS no necesariamente está operativo.
- Las bandas de perigeo no constituyen una clasificación orbital completa.
- Los conteos por año corresponden al año de lanzamiento asociado al registro, no a eventos de lanzamiento ni a fechas de fragmentación.
- Las categorías radar no miden directamente masa o diámetro.

## Validación de esta revisión

Las 37 celdas de código se ejecutaron en orden en una sesión limpia de IPython, regenerando tablas y figuras a partir de los cinco archivos fijados. El entorno de revisión no permite abrir los sockets de un kernel Jupyter, por lo que se usó IPython dentro del mismo proceso. Se comprobó el formato del archivo y se revisaron las figuras. Las versiones usadas están en `requirements.txt`.
