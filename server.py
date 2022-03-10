import json
from flask import Flask, jsonify, redirect, render_template, request
from dbmysql import crear_conexion
import controlador

app = Flask(__name__)

'''Ruta Para Mostrar Index'''
@app.route("/")
def index():
    return render_template('index.html')

'''Ruta Para Insertar En La Tabla Countrys'''
@app.route('/api/insertarDatosCountry', methods=('GET', 'POST'))
def insertIntoCountrys():
        Code = request.form['Code']
        Name = request.form['Name']
        Continent = request.form['Continent']
        Region = request.form['Region']
        SurfaceArea = request.form['SurfaceArea']
        IndepYear = request.form['IndepYear']
        Population = request.form['Population']
        LifeExpectancy = request.form['LifeExpectancy']
        GNP = request.form['GNP']
        GNPOld = request.form['GNPOld']
        LocalName = request.form['LocalName']
        GovernmentForm = request.form['GovernmentForm']
        HeadOfState = request.form['HeadOfState']
        Capital = request.form['Capital']
        Code2 = request.form['Code2']

        controlador.insertCountrys(Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2)
        return redirect('/api/mostrarCountrys')

'''Ruta Para Mostrar Tabla Countrys'''
@app.route('/api/mostrarCountrys', methods=['GET'])
def selectFromCountrys():  
    countrys = controlador.getAllCountrys()
    return render_template('countrys.html', countrys=countrys)

'''Ruta Para Mostrar Un Registro de Countrys'''
@app.route('/api/mostrarCountrysCode', methods=('GET', 'POST'))
def findCountry():
    Code = request.form['Code']  
    countrys = controlador.getOnlyCountry(Code)
    return render_template('country.html', countrys=countrys)

'''Ruta Para Eliminar En La Tabla Countrys'''
@app.route('/api/eliminarCountrys',methods=['POST'])
def deleteCountry():
    Code = request.form['Code']
    controlador.deleteCountry(Code)
    return redirect('/api/mostrarCountrys')

'''Ruta Para Editar En La Tabla Countrys'''
@app.route("/editar")
def updateCountrys():
    return render_template('editar.html')

'''Ruta Para Editar En La Tabla Countrys'''
@app.route('/api/editarCountry', methods=('GET', 'POST'))
def updateCountry():
        Code = request.form['Code']
        Name = request.form['Name']
        Continent = request.form['Continent']
        Region = request.form['Region']
        SurfaceArea = request.form['SurfaceArea']
        IndepYear = request.form['IndepYear']
        Population = request.form['Population']
        LifeExpectancy = request.form['LifeExpectancy']
        GNP = request.form['GNP']
        GNPOld = request.form['GNPOld']
        LocalName = request.form['LocalName']
        GovernmentForm = request.form['GovernmentForm']
        HeadOfState = request.form['HeadOfState']
        Capital = request.form['Capital']
        Code2 = request.form['Code2']

        controlador.updateCountrys(Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2)
        return redirect('/api/mostrarCountrys')