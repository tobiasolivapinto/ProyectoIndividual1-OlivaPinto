#Librerias Utilizadas
from fastapi import FastAPI
import pandas as pd

#Creacion de la APP
app = FastAPI()

#Creamos la ruta para la API. La ruta raiz
#http://127.0.0.1:8000
#@app.get("/")

#Carga de base de datos con las tarnsformaciones ya realizdas 
movies_db = pd.read_csv("/Users/tobiasolivapinto/Desktop/PI-1-General/DataBase/movies_db_mod4.cvs")

#Creamos un directorio index con un mensaje de bienvenida
@app.get("/")
def index ():
    return "Hola Mundo"

#Se desarollaran las consignas que fueron solicitadas

@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes: str):
    #Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente
    mes = mes.capitalize()
    cantidad = len(movies_db.loc[movies_db["month"] == mes, "title"])
    return {"mes" : str(mes), "cantidad" : int(cantidad)}

@app.get("/peliculas_dias/{dia}")
def peliculas_dias(dia: str):
    #Se ingres el dia y la funcion retorna la cantidad de peliculas que se estrenaron ese dia historicamente
    dia = dia.capitalize()
    cantidad = len(movies_db.loc[movies_db["day"] == dia, "title"])
    return {"dia" : str(dia), "cantidad" : int(cantidad)}

@app.get("/franquicia/{franquicia}")
def franquicia(franquicia: str):
    #Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio
    franquicia = franquicia.lower()
    cantidad_peliculas = (movies_db[movies_db["belongs_to_collection"].str.lower() == franquicia]).shape[0]
    presupuesto = movies_db[movies_db["belongs_to_collection"].str.lower() == franquicia]["budget"]
    ingresos = movies_db[movies_db["belongs_to_collection"].str.lower() == franquicia]["revenue"]
    ganancia_total = ingresos.sum() 
    ganancia_promedio = ganancia_total / cantidad_peliculas
    return {"franquicia" : str(franquicia), "cantidad" : int(cantidad_peliculas), "ganancia_total" : int(ganancia_total), "ganancia_promedio" : int(ganancia_promedio)}

@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais: str):
    #Se ingres el pais y la funcion retorna la cantidad de peliculas producidas en el mismo
    mask = movies_db['production_countries'].str.join('|').str.contains(pais, case=False)
    cantidad = len(movies_db[mask]['title'])
    return {"pais" : str(pais), "cantidad" : int(cantidad)}

@app.get("/productoras/{productora}")
def productoras(productora: str):
    #Ingresa la productora, retornando la ganancia total y la cantidad de peliculas que produjeron
    mask = movies_db['production_companies'].str.join('|').str.contains(productora, case=False)
    cantidad = len(movies_db[mask]['title'])
    ingresos = movies_db[mask]['revenue']
    ganancia = ingresos.sum()
    return {"productora" : str(productora), "Ganancia" : int(ganancia), "cantidad de peliculas que produjeron" : int(cantidad)}

@app.get("/retorno/{pelicula}")
def retorno(pelicula: str):
    # Ingresa la pelicula, retornando la inversion, la ganancia, el retorno y el ano que se lanzo
    pelicula = pelicula.lower()  # convertir a minúsculas
    pelicula_df = movies_db.loc[movies_db["title"].apply(lambda x: str(x).lower() == pelicula if pd.notnull(x) else False)]
    inversion = pelicula_df["budget"].values[0]
    ganancia = pelicula_df["revenue"].values[0]
    retorno = pelicula_df["return"].values[0]
    ano = pelicula_df["release_year"].values[0]
    return {"Pelicula": str(pelicula), "Inversion": int(inversion), "Ganancia": int(ganancia), "retorno": int(retorno), "ano": int(ano)}

#ML
#@app.get("/recomendacion/")
#def recomendacion("titulo"):
    #Se ingresa el nommbre de la pelicula y te recomienda las similares en una lista
#   return {"lista recomendad" : respuesta}