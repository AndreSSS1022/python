#Se importan las librerias a usar en el proyecto

import requests
import configparser

#Habilita las capacidades de servidor en la aplicacion
#Es la libreria encargada de gestionar la renderizacion de las vistas 

from flask import Flask, render_template, request # type: ignore

#El objeto principal de la aplicacion se llama app
app = Flask(__name__)

#Iniciamos con la logica de la aplicacion

#Se gestiona la ruta inicial de la aplicacion

#Ruta principal
@app.route('/')
#Aqui va el nombre de la funcion o metodo que gestiona la ruta
def weather_dashboard():
    return render_template ('home.html')

#Ruta que pinta los resultados
@app.route('/results')
def render_resultados():
#Para poder mostrar los resultados, antes debo saber cual es la ciudad que digito en el formulario
    cityname= request.form['cityname']


#Es pasarle el valor de la ciudad que el usuario digito al api
#Pero antes de consumir el api

#Esta variable esta almacenando el valor del api key que se encuentra en el archivo config.ini
    api = get_api_key(); 

#Vamos a conectarnos al api y consumirlo
#Data contiene el json con la respuestas

    data = get_weather_results(cityname, api) 
    
    #Se toma la temperatura del json
    temp ="{0:.2f}"format (data['main']['temp'])

def get_weather_results(cityname, api_key):
    url= "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(cityname, api_key)
    
    r= request.get(url)
    return r.json
    
   



def get_api_key():
    #Esta funcion obtiene el valor del api key que se va a utilizar para consumir el servicio web

    #Se lee el archivo que guarda la api key del servicio web
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config ['openweathermap']['api']



#Esta condicion siempre va en los proyectos de python e indica que por defecto  el metodo  principal en el main
if __name__ == "__main__":
    app.run(debug=True)