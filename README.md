# ProyectoIndividual1-OlivaPinto
Proyecto Individual 1 - Henry - Oliva Pinto Tobias

Hola! Como estas?

Me presento, soy Tobias Oliva Pinto, estudiante de Data Science en la academia Henry (por ahora ;)). Si quieres saber mas sobre mi chequea mi perfil.

Este es mi primer proyecto completo de Data Science, como puedes ver, se llama Proyecto Individual 1 - Henry. Te contare un poco acerca de el. 
El nombre formal, acorde a Henry, es "PROYECTO INDIVIDUAL Nº1 - Machine Learning Operations (MLOps)". Aqui podras encontrar un proyecto que consta de dos partes:
La primera, es la parte de Data Engeniering, donde basicamente hicimos el proceso de ETL (Extraccion, Transformacion, Carga). 
La segunda, es la parte de Machine Learning, donde tuvimos que hacer el EDA (Analisis Exploratorio de Datos) para preparar los datos que nos habian proporcionado para confeccionar el modelo de Machine Learning. 
Puede que estos conceptos no sean claros para todo el mundo, no se preocupen, mas adelante detallaremos la informacion necesaria para que cualquiera puede comprender lo que encontrara aqui. 


Primera Parte - Data Engeniering 

En la primera parte del proyecto debiamos asumir el rol de un Data Engenier. Se nos daba una base de datos en formato .cvs y debiamos llevar a cabo ciertas transformaciones para luego porder realizar algunas consultas a modo de prueba. Basicamente, esto es el ETL, de todas formas, aqui tienen una definicion mas general que he formulado: "es el proceso donde extraemos los datos de la base de datos que nos provee el cliente, para hacerle las transformaciones necesarias con el objetivo de dejar los datos ordenados y preparados para que se le puedan hacer consultas (preguntas se podria decir). Por ultimo, procedemos a cargar los datos donde corresponda."

Segunda Parte - Machine Learning 

En la segunda parte del proyecto debiamos asumir el rol de un Data Scientist. La consigna era confecionar un analisis exploratorio de datos (EDA) para luego crear un modelo de recomendacion de peliculas. Debiamos ingresar el titulo de que la pelicula y que este nos devuelva una lista con 5 peliculas similares, por asi decirlo. 
En esta parte he decido explayarme ya que considero importante que entiendan el enfoque que tome. Como casi todo proyecto, ya sea estudiando o trabajando, hay plazos de entrega. Comenzamos este proyecto un Lunes a las 11 am y lo debiamos entregar 9 dias despues, el Martes a las 4 pm. Ademas de lo que ya se menciono, debiamos hacer un despliegue de un servicio virtual en Render, para poder acceder a las consultas desde cualquier computador. Como pueden ver, no era un proyecto corto, ni facil, por lo que hubo que aprovechar cada minuto de trabajo. 
Dadas estas circunstancias, opte en hacer el modelo de recomendaciones de la primera manera que se me ocurrio, centrandome en el resultado y no en el proceso interno del mismo. Por lo que se pueden llevar una sorpresa cuando vean que no tome las recomendaciones de Henry para hacerlo. Esto de ir contra la corriente casi nunca funciona, pero cuando no hay alternativas y el tiempo se agota hay que tomar decisiones y simplemente hacerlo posible. Me guie por la consigna, que era obtener un MVP (Producto Viable Minimo), significa que debe cumplir con los requerimientos y funcionar, a mi parecer lo logre =). 
Para hacer el modelo de recomendacion decidi conservar las columnas:
- "belongs_to_collection": Hace referencia a que franquicia pertenece la pelicula. 
- "genres": Hace referencia al genero de la pelicula.
- "production_companies: Hace referencia a la compania que produjo la pelicula. 
- "original_language": Hace referencia al idioma de origen de la pelicula. 
- "range_year": Una columna que cree yo mismo, para dar referencia de cuando se hizo la pelicula. 

En el modelo, se inserta el titulo de la pelicula, el cual tiene estos mismo atributos en la base de datos, y se comienza a efectuar una comparacion. La idea es que cada vez que un valor coincida con el de la pelicula insertada se le va sumar un puntaje determinado. Al final se va entregar una lista con las 5 peliculas que mayor puntaje obtuvieron, es decir las que mas coincidencias poseen. 
Se prioriza si pertenece a la franquicia, luego el genero, despues la compania productora y por utlimo el idioma y hace cuanto se hizo la pelicula. 


Archivos

En este proyecto podras encontrar:
- Dentro de la carpeta Bases de Datos, esta la base de datos en sus tres versiones. Estas serian, los datos crudos tal y como nos los dieron, los datos despues de haber realizado el ETL, los datos despues de haber realizado el EDA.
- Dentro de la carpeta ETL-EDA, se encuentran dos archivos .ipynb. Estos serian los dos analisis de la base de datos, el ETL y el EDA.
- En el archivo "main.py" podras encontrar las consultas que se nos requirieron, incluida la de Machine Learning. 

Despliegue web

Este link sirve para testear las consultas y el modelo de recomendacion de peliculas (este ultimo tarda un poco, no se preocupen ;)).
https://render-proyectoindividual1-olivapinto.onrender.com
Le deben agregar un "/docs" al final para entrar en el entorno de prueba, si no lo hacen, solamente podran ver el mensaje de bienvenida. 

Cierre

Espero que mi proyecto te sea útil, sin importar el motivo por el que decidiste investigarlo.
Decidi confeccionar el README.md de una manera informal, para que sea mas entretenido y practico para el publico general. Que los disfrutes. 
Saludos!
Tobias. 
