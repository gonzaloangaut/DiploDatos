### Dataset original (datos de precios de propiedades en Melbourne):
https://cs.famaf.unc.edu.ar/~mteruel/datasets/diplodatos/melb_data.csv

Cada fila corresponde a un aviso publicitario de una propiedad en venta.

Detallamos a continuación las transformaciones que llevaron al nuevo dataset producido.

## Criterios de exclusión

### Columnas excluidas:
- Suburb: Esta columna es superflua por encontrarse "Propertycount" (cantidad de propiedades en un suburbio).
- Address: Difícil de procesar para su uso, y poseemos mejores datos de geolocalización.
- Date: El rango temporal de recolección de los datos es muy acotado, por lo que decidimos descartar dicha columna.

### Filas excluidas
- Se descartaron todas las filas que estaban por encima del percentil 99 del campo Landsize, a fin de eliminar variables extremas.


## Columnas utilizadas:
- Categóricas:
  - Type: tipología de la propiedad
  - Method: Método de venta (Por ejemplo, S - property sold; SP - property sold prior, ...).
  - SellerG: a que corredor inmobiliario pertenecía el aviso
  - CouncilArea: Municipio al que pertenece la propiedad
  - Regionname: Región general dentro de Melbourne

- Numéricas:
  - Rooms: cantidad de habitaciones
  - Price: precio de la propiedad
  - Distance: distancia de la propiedad al centro de Melbourne
  - Poscode: código postal de la propiedad
  - Bedroom2: cantidad de dormitorios
  - Bathroom: cantida de baños
  - Car: Cantidad de cocheras
  - Landsize: Tamaño del terreno
  - BuildingArea: Tamaño de la edificación
  - YearBuilt: Año de construcción
  - Lattitude: Latitud geográfica
  - Longtitude: Longitud geográfica
  - Propertycount: cantidad de propiedades en el mismo suburbio


## Transformaciones

1. Los valores categóricos fueron codificados usando el método "OneHotEncoding", con un límite máximo de 25 categorías únicas (las 24 más frecuentes, mas 1 que representa a las menos infrecuentes), descartando las variables categóricas originales.

2. Las variables numéricas fueron escaladas a una escala [0-1], excepto BuildingArea y YearBuilt.

3. Para las columnas BuildingArea y YearBuilt, eliminamos las filas que se encuentran por encima del percentil 99 y por debajo del percentil 1 para evitar outliers importantes.

4. Se imputaron los valores inexistentes de las columnas BuildingArea y YearBuilt usando IterativeImputer con la estrategia K-nearest-neighbors. Fueron graficadas las distribuciones antes y después de la imputación. Luego, estas columnas, ahora completas, fueron también escaladas a la escala [0-1].


## Reducción de dimensionalidad (PCA)
Se aplicó Análisis de Componentes Principales (PCA) sobre la matriz completamente procesada:

- Se obtuvieron las primeras 20 componentes principales.

- Se agregaron las primeras 2 componentes (pca1, pca2) como nuevas columnas al dataset final.

Realizamos un gráfico de las componentes principales que muestra una clara estructura agrupada: hay regiones bien definidas donde se concentran los puntos. Esto sugiere que, a pesar de la alta dimensión del dataset original, los datos tienen una estructura que puede ser capturada en 2 dimensiones.