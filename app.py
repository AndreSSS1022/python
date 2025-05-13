#Se importan las librerias a usar en el proyecto

import requests
import configparser

#Habilita las capacidades de servidor en la aplicacion
#Es la libreria encargada de gestionar la renderizacion de las vistas 

from flask import Flask, render_template, request

#El objeto principal de la aplicacion se llama app
app = Flask(__name__)

#Iniciamos con la logica de la aplicacion

#Se gestiona la ruta inicial de la aplicacion
@app.route('/')
#Aqui va el nombre de la funcion o metodo que gestiona la ruta
def weather_dashboard():
    return render_template ('home.html')





#Esta condicion siempre va en los proyectos de python e indica que por defecto  el metodo  principal en el main
if __name__ == "__main__":
    app.run(debug=True)