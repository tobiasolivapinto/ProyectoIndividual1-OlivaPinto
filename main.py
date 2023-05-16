#Librerias Utilizadas
from fastapi import FastAPI
import pandas as pd
import numpy as np

#Creacion de la APP
app = FastAPI()

#Carga de base de datos con las tarnsformaciones ya realizdas 
movies_db = pd.read_csv("movies_db_mod7.cvs")

#Definimos funcion para cambiar de str a list
def safe_literal_eval(x):
    if isinstance(x, str) and x != 'nan':
        # Remover los corchetes y las comillas
        x = x.strip('[]').replace("'", "").split(", ")
        return x
    else:
        return np.nan

#Cambiamos de str a list
movies_db["production_countries"] = movies_db["production_countries"].apply(safe_literal_eval)
movies_db["production_companies"] = movies_db["production_companies"].apply(safe_literal_eval)
movies_db["genres"] = movies_db["genres"].apply(safe_literal_eval)



#Creamos un directorio index con un mensaje de bienvenida
@app.get("/")
def index ():
    return {"Hola Mundo"}

#Se desarollaran las consignas que fueron solicitadas

@app.get("/peliculas_mes/{mes}")
def peliculas_mes3(mes: str):
    # Diccionario para mapear los nombres de los meses en español a inglés
    meses = {
        "enero": "january",
        "febrero": "february",
        "marzo": "march",
        "abril": "april",
        "mayo": "may",
        "junio": "june",
        "julio": "july",
        "agosto": "august",
        "septiembre": "september",
        "octubre": "october",
        "noviembre": "november",
        "diciembre": "december"}
    # Convertir el nombre del mes en español a minúsculas
    mes = mes.lower()
    # Obtener el nombre del mes en inglés utilizando el diccionario
    mes_ingles = meses.get(mes)
    if mes_ingles:
        cantidad = len(movies_db.loc[movies_db["month"].str.lower() == mes_ingles, "title"])
        return {"mes" : str(mes), "cantidad" : int(cantidad)}

@app.get("/peliculas_dias/{dia}")
def peliculas_dias2(dia: str):
    # Diccionario para mapear los nombres de los días en español a inglés
    dias = {
        "lunes": "monday",
        "martes": "tuesday",
        "miercoles": "wednesday",
        "jueves": "thursday",
        "viernes": "friday",
        "sabado": "saturday",
        "domingo": "sunday"}
    # Convertir el nombre del día en español a minúsculas
    dia = dia.lower()
    # Obtener el nombre del día en inglés utilizando el diccionario
    dia_ingles = dias.get(dia)
    if dia_ingles:
        cantidad = len(movies_db.loc[movies_db["day"].str.lower() == dia_ingles, "title"])
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
@app.get("/recomendacion/{titulo}")
def recomendacion(titulo:str):
    pelicula = movies_db[movies_db['title'] == titulo]
    
    if pelicula.empty:
        print("No se encontró la película en la base de datos.")
        return []
    
    movies_db['similarity_score'] = 0
    
    for index, row in movies_db.iterrows():
        score = 0
        if row['belongs_to_collection'] == pelicula['belongs_to_collection'].values[0]:
            score += 50
        if set(row['genres']) & set(pelicula['genres'].values[0]):
            score += 20
        if set(row['production_companies']) & set(pelicula['production_companies'].values[0]):
            score += 15
        if row['original_language'] == pelicula['original_language'].values[0]:
            score += 10
        if row['year_range'] == pelicula['year_range'].values[0]:
            score += 10
        movies_db.loc[index, 'similarity_score'] = score

    peliculas_similares = movies_db.sort_values('similarity_score', ascending=False)
    
    peliculas_similares = peliculas_similares[peliculas_similares['title'] != titulo]
    
    peliculas_recomendadas = peliculas_similares.head(5)
    
    lista_pelis = peliculas_recomendadas['title'].tolist()
    
    return {"Lista recomendada" : str(lista_pelis)}