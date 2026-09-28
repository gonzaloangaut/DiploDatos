# TP1 — Análisis y visualización de objetos espaciales

Autores: Ana Paula Cobresí, Gonzalo Angaut, Javier Albiero y Octavio Santi.

Análisis exploratorio de un catálogo histórico de objetos espaciales: integración de fuentes, calidad de datos, distribuciones orbitales y radar, y evolución por año de lanzamiento. Proyecto de la mentoría «Predicciones en el Espacio: ¿Cuántos satélites y desechos podremos tener?».

## Ejecutar

Desde esta carpeta, en un entorno Python 3.12:

```bash
python -m pip install -r requirements.txt
```

Abrir `TP1_Análisis_y_Visualización_mentoría.ipynb` en Jupyter, Colab o un editor compatible y ejecutar todas las celdas en orden. En Colab se puede instalar con `%pip install -r requirements.txt` después de subir este archivo, o instalar directamente pandas, numpy, matplotlib, seaborn y openpyxl.

La primera ejecución descarga cinco archivos (aproximadamente 49 MB) y requiere acceso a `raw.githubusercontent.com`. Se guardan en `data/raw/<commit>/`, excluido de Git. Las siguientes ejecuciones reutilizan esa copia. El archivo `environment.yml` documenta el entorno utilizado durante la Diplomatura.

## Fuentes y alcance

Los datos quedan fijados al commit `1c49c73b92e84d3eba2c53f43313ed861d08f896` de [EnzoRg/space_debris](https://github.com/EnzoRg/space_debris/tree/1c49c73b92e84d3eba2c53f43313ed861d08f896/data/raw). Esto conserva los archivos de entrada; no convierte la fecha del commit en fecha de observación.

- Cada fila es un objeto catalogado; el catálogo incluye reentradas registradas.
- Un objeto no-DEBRIS no necesariamente está operativo.
- Las bandas de perigeo no constituyen una clasificación orbital completa.
- Los conteos por año corresponden al año de lanzamiento asociado al registro, no a eventos de lanzamiento ni a fechas de fragmentación.
- Las categorías radar no miden directamente masa o diámetro.
