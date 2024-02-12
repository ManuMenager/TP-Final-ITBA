# TP Final Certificación Profesional Python

## Objetivo

Realizar un programa que permita recolectar datos de la API de finanzas de [Polygon](https://polygon.io/) para analizar la evolución del valor de una acción. El propósito es recolectar información del sitio, almacenarla en una base de datos, y permitir al usuario visualizar la evolución de la acción solicitada. El usuario podrá visualizar un resumen de dicha información e incluso solicitar un gráfico para su análisis, para ello el programa solicitará ciertos parámetros que el usuario deberá proporcionar para poder identificar la información correspondiente.

## Implementación del programa

El programa trabaja con Polygon.io, esto quiere decir que para poder utilizarlo el usuario necesitará obtener una API-KEY para lograr solicitar información.

Para obtener la API-KEY se deberá acceder al [siguiente link](https://polygon.io/docs/stocks/getting-started)
Una vez en la página de polygon.io, es necesario que el usuario este registrado y haya iniciado sesión. Teniendo esto en cuenta habrá un botón en la parte superior derecha de la página "Dashboard", al colocar el cursor sobre el botón se desplegará una lista de opciones, acceder a la opción "API Keys" haciendo click en ella. Finalmente aparecerá en pantalla una tabla con todas las api keys que el usuario posee, en el caso de que nunca haya agregado una api key, se mostrará con el name "default" y a su derecha el código de la api key que se debe copiar para utilizar en el programa.

A través del programa se podrán solicitar cuatro tipos de indices (TICKERS) que polygon nos brindá: Stocks/Equities, Indices, Forex y Crypto.

Para poder solicitar información de alguno de estos indices, el programa nos pedirá el nombre del TICKER, la fecha de inicio y la fecha de fin y la API KEY de Polygon.

Si los datos ingresados son correctos se guardará la información en una base de datos.

Con la información en la base de datos el usuario podrá acceder a un resumen, a partir del cual se visualizaran todos los tickers almacenados, indicando por fila cada solicitud que se hayá realizado exitosamente. con el siguiente formato:
TICKER - FECHA DE INICIO(YYYY-MM-DD) <-> FECHA DE FIN (YYYY-MM-DD)

Por otro lado, el usuario también podrá visualizar un gráfico el cual presentará la variación del valor del TICKER durante periodo solicitado.

## Extras

El programa avisará al usuario en el caso de que la solicitud deseada no sea válida o haya un dato erróneo, mediante el siguiente mensaje: "Error al hacer la solicitud a la API. Código de error: {json_file.status_code}".

El usuario podrá organizar la base de datos, ya que el programa tiene una opción para eliminar datos de una manera sencilla. Se solicitará el nombre del TICKER, la fecha de inicio y la fecha de fin para identificar la información.

El programa cuenta con una función de verificación a partir de la cual notificará al usuario si la operación se realizó se manera exitosa o si hubo algún problema.


## Primera entrega
Estamos trabajando para agregar una interfaz gráfica, intentaremos hacer un archivo ejecutable del programa y completaremos la documentación readme


## Integrantes

* [Christian Armenteros](https://www.linkedin.com/in/carmenteros2001/)
* [Emanuel Menager](https://www.linkedin.com/in/emanuel-menager-785b41269/)
* [Leonardo Alexis Cordoni](https://www.linkedin.com/in/acordoni/)
* [Sergio García Mora](https://www.linkedin.com/in/sergiogarciamora/)