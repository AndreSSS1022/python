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
def render_resultados
#Para poder mostrar los resultados, antes debo saber cual es la ciudad que digito en el formulario
cityname= request.form['cityname']

#Es pasarle el valor de la ciudad que el usuario digito al api
#Pero antes de consumir el api
api = get_api_key();




#Esta condicion siempre va en los proyectos de python e indica que por defecto  el metodo  principal en el main
if __name__ == "__main__":
    app.run(debug=True)