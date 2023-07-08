# Proyecto Individual N°1 - Henry - Oliva Pinto Tobías  <img src="https://assets.soyhenry.com/LOGO-REDES-01_og.jpg" alt="Imagen" width="70">

## Machine Learning Operations (MLOps)

## Índice 
- [Índice](#indice)
- [Presentación](#presentacion)
- [Introducción](#introducción)
- [Primera Parte](#primeraparte)
- [Segunda Parte](#segundaparte)
- [Archivos](#archivos)
- [Despliegue Web](#despliegueweb)
- [Cierre](#cierre)

## Presentación

**[Linkedin](https://www.linkedin.com/in/olivapintotobias/)**

 <img src="https://media.licdn.com/dms/image/D4D03AQHOo19d5aSn0A/profile-displayphoto-shrink_800_800/0/1687974921520?e=1694044800&v=beta&t=iOkiAK7xkoaArzy-e_BEmHQhquDcNcIfqy97K3qYwfA" alt="Imagen" width="200" style="margin-right: 20px;">
 
Hola de nuevo! Por si no viste mi primer repositorio, me presento otra vez. Soy Tobias Oliva, estudiante de la carrera Data Science en Henry (por ahora... ;)), para mas información puedes revi. Este es mi segundo proyecto induvidual de la carrera. 
¡Hola! ¿Como estas? Me presento, soy Tobias Oliva Pinto, estudiante de Data Science en la academia Henry (por ahora ;)). Para ser mas preciso, tambien soy un ingeniero industrial de 25 años de Córdoba, Argentina. Mi pasión por la innovación y la exploración me ha llevado al emocionante mundo de la ciencia de datos. Combino habilidades técnicas y visión práctica para descubrir ideas transformadoras. Tengo experiencia en higiene y seguridad en la industria química, lo cual me brinda un sólido entendimiento de los aspectos prácticos y la importancia de mantener entornos seguros.

## Introducción 
Este es mi primer proyecto completo de Data Science, como puedes ver, se llama Proyecto Individual N°1 - Henry. Te contaré un poco acerca de él. El nombre formal, acorde a Henry, es "PROYECTO INDIVIDUAL Nº1 - Machine Learning Operations (MLOps)". Aquí podrás encontrar un proyecto que consta de dos partes: La primera, es la parte de Data Engeniering, donde básicamente hicimos el proceso de ETL (Extracción, Transformación, Carga). La segunda, es la parte de Machine Learning, donde tuvimos que hacer el EDA (Análisis Exploratorio de Datos) para preparar los datos que nos habían proporcionado para confeccionar el modelo de Machine Learning. Puede que estos conceptos no sean claros para todo el mundo, no se preocupen, más adelante detallaremos la información necesaria para que cualquiera pueda comprender lo que encontrará aquí.

## Primera Parte 
**Data Engeniering**
En la primera parte del proyecto debíamos asumir el rol de un Data Engenier. Se nos daba una base de datos en formato .cvs y debíamos llevar a cabo ciertas transformaciones para luego poder realizar algunas consultas a modo de prueba. Básicamente, esto es el ETL, de todas formas, aquí tienen una definición más general que he formulado: "es el proceso donde extraemos los datos de la base de datos que nos provee el cliente, para hacerle las transformaciones necesarias con el objetivo de dejar los datos ordenados y preparados para que se le puedan hacer consultas (preguntas se podría decir). Por ultimo, procedemos a cargar los datos donde corresponda."

## Segunda Parte
**Machine Learning**
En la segunda parte del proyecto debíamos asumir el rol de un Data Scientist. La consigna era confeccionar un análisis exploratorio de datos (EDA) para luego crear un modelo de recomendación de películas. Debíamos ingresar el título de la película y que este nos devuelva una lista con 5 películas similares, por así decirlo. En esta parte he decidido explayarme ya que considero importante que entiendan el enfoque que tome. Como casi todo proyecto, ya sea estudiando o trabajando, hay plazos de entrega. Comenzamos este proyecto un Lunes a las 11 am y lo debíamos entregar 9 días después, el Martes a las 4 pm. Además de lo que ya se mencionó, debíamos hacer un despliegue de un servicio virtual en Render, para poder acceder a las consultas desde cualquier computador. Como pueden ver, no era un proyecto corto, ni fácil, por lo que hubo que aprovechar cada minuto de trabajo. Dadas estas circunstancias, opté por hacer el modelo de recomendaciones de la primera manera que se me ocurrió, centrándome en el resultado y no en el proceso interno del mismo. Por lo que se pueden llevar una sorpresa cuando vean que no tome las recomendaciones de Henry para hacerlo. Esto de ir contra la corriente casi nunca funciona, pero cuando no hay alternativas y el tiempo se agota hay que tomar decisiones y simplemente hacerlo posible. Me guíe por la consigna, que era obtener un MVP (Producto Viable Mínimo), significa que debe cumplir con los requerimientos y funcionar, a mi parecer lo logré =). Para hacer el modelo de recomendación decidí conservar las columnas:
- **"belongs_to_collection":** Hace referencia a que franquicia pertenece la película.
- **"genres":** Hace referencia al género de la película.
- **"production_companies:** Hace referencia a la compañía que produjo la película.
- **"original_language":** Hace referencia al idioma de origen de la película.
- **"range_year":** Una columna que creo yo mismo, para dar referencia de cuando se hizo la película.

En el modelo, se inserta el título de la película, el cual tiene estos mismo atributos en la base de datos, y se comienza a efectuar una comparación. La idea es que cada vez que un valor coincida con el de la película insertada se le va sumar un puntaje determinado. Al final se va entregar una lista con las 5 películas que mayor puntaje obtuvieron, es decir las que más coincidencias poseen. Se prioriza si pertenece a la franquicia, luego el género, después la compañía productora y por último el idioma y hace cuanto se hizo la película.

## Archivos
En este proyecto podrás encontrar:
- **Bases de Datos:** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/tree/main/Bases%20de%20Datos) 
	- **movies_dataset.csv** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/blob/main/Bases%20de%20Datos/movies_dataset.csv)  →  Los datos crudos tal y como nos los dieron.
	- **movies_db_ETL.cvs** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/blob/main/Bases%20de%20Datos/movies_db_ETL.cvs)  →  Los datos despues de haber realizado el ETL.
	- **movies_db_EDA.cvs** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/blob/main/Bases%20de%20Datos/movies_db_EDA.cvs)  →  Los datos despues de haber realizado el EDA.
- **ETL-EDA:** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/tree/main/ETL%20-%20EDA) 
	- **ETL.ipynb:** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/blob/main/ETL%20-%20EDA/ETL.ipynb)  →  Extracción, Transformación y Carga de los datos. 
	- **EDA.ipynb:** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/blob/main/ETL%20-%20EDA/EDA.ipynb)  →  Analisis Exploratorio de Datos
- **main.py:** [(link)](https://github.com/tobiasolivapinto/ProyectoIndividual1-OlivaPinto/blob/main/main.py)  →  Las consultas que se nos requirieron, incluida la de Machine Learning.

## Despliegue Web
Este link sirve para testear las consultas y el modelo de recomendación de películas (este último tarda un poco, no se preocupen ;)).
- **Despliegue web:** [(link)](https://render-proyectoindividual1-olivapinto.onrender.com/docs)

## Cierre
Espero que mi proyecto te sea útil, sin importar el motivo por el que decidiste investigarlo. Decidí confeccionar el README.md de una manera informal, para que sea más entretenido y práctico para el público general. Que los disfrutes. Saludos! Tobías.

