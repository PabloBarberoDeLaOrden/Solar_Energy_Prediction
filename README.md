# Solar_Energy_Prediction
Proyecto de Machine Learning cuyo objetivo es predicir la cantidad de energia solar recogida por un panel solar, utilizando tanto técnicas de regresión como series temporales.

![Paneles_Solares](https://github.com/PabloBarberoDeLaOrden/Solar_Energy_Prediction/blob/main/Solar_energy_prediction/gefs_mesonet_stations.png)

Con el objetivo de simplificar este proyecto se ha decidido predecir exclusivamente en base a un panel, utilizando como datos bien la cantidad de energia producida dias anetriores, o la información meteorológica que se disponía del area de localización del panel.

Para cualquier duda podéis contactar conmigo vía [Linkedin](https://www.linkedin.com/in/pablo-barbero-de-la-orden/)
---

## Datos

Los datos empleados para la realización del proyecto corresponden con la siguiente competición de [Kaggle](https://www.kaggle.com/competitions/ams-2014-solar-energy-prediction-contest/data)

Los datos meteorológicos son los siguientes:

|Variable |	Description |	Units |
|---------| ------------|-------|
|apcp_sfc	|3-Hour accumulated precipitation at the surface|	kg m-2|
|---------| ------------|-------|
|dlwrf_sfc|	Downward long-wave radiative flux average at the surface	|W m-2|
|---------| ------------|-------|
|dswrf_sfc|	Downward short-wave radiative flux average at the surface	|W m-2|
|---------| ------------|-------|
|pres_msl|	Air pressure at mean sea level	|Pa|
|---------| ------------|-------|
|pwat_eatm|	Precipitable Water over the entire depth of the atmosphere	|kg m-2|
|---------| ------------|-------|
|spfh_2m|	Specific Humidity at 2 m above ground	|kg kg-1|
|---------| ------------|-------|
|tcdc_eatm|	Total cloud cover over the entire depth of the atmosphere	|%|
|---------| ------------|-------|
|tcolc_eatm|	Total column-integrated condensate over the entire atmos.	|kg m-2|
|---------| ------------|-------|
|tmax_2m|	 Maximum Temperature over the past 3 hours at 2 m above the ground	 |K|
|---------| ------------|-------|
|tmin_2m|	 Mininmum Temperature over the past 3 hours at 2 m above the ground	 |K|
|---------| ------------|-------|
|tmp_2m|	 Current temperature at 2 m above the ground	 |K|
|---------| ------------|-------|
|tmp_sfc|	 Temperature of the surface	 |K|
|---------| ------------|-------|
|ulwrf_sfc|	 Upward long-wave radiation at the surface	 |W m-2|
|---------| ------------|-------|
|ulwrf_tatm| Upward long-wave radiation at the top of the atmosphere	 |W m-2|
|---------| ------------|-------|
|uswrf_sfc|	 Upward short-wave radiation at the surface	 |W m-2|
|---------| ------------|-------|

El target  corresponde con la energía solar total diaria entrante medida en (J m-2)

---
## Librerías

En el codigo se utilizan las siguientes librerías:

- Pandas
- Numpy
- matplotlib
- sklearn
- xgboost
- pickle

  Para más información consultar requirements
---

## Modelo
Debido a que el modelo esta sujeto a la variable tiempo, se ha decidido dividir el conjunto de datos desde 1994 al 2000 como conjunto de entrenamiento, del 2001 al 2003 como validación y del 2004 al 2007 como conjunto de test. De manera que la aleatorización no influirá en nuestro modelo y respetará la varible implicita del tiempo. 

Tras evaluar diferentes modelos mediante la métrica de error absoluto relativo ('RAE'), se determina que el mejor modelo corresponde con un random forest de n_estimators = 1500 y un max_features = 5.

![Predicciones](https://github.com/PabloBarberoDeLaOrden/Solar_Energy_Prediction/blob/main/Solar_energy_prediction/predicciones.png)

El modelo dispone de un error relativo absoluto de 0.32, es decir el modelo mejora en un 68% al modelo trivial, predecir todo con la media del entrenamiento.

---

## Conclusión 

Para mi sorpresa el modelo que realiza las mejores predicciones corresponde con un problema de regresión y no de series temporales, si bien es cierto que podría optimizarse en mejor medida la parte de series temporales, considero que para la dificultad de prediccion del problema y los datos empleados se alcanza una métrica aceptable. 
