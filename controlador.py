from jinja2 import contextfilter
from dbmysql import crear_conexion
from flask import Flask, jsonify, redirect, render_template, request

'''Query INSERT INTO'''
def insertCountrys(Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2):
    conexion = crear_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO country (Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                      (Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2))
    conexion.commit()
    conexion.close()

'''Query SELECT FROM'''
def getAllCountrys():
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT *FROM country")
            cursor=cursor.fetchall()
            data = []
            for (Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2) in cursor:
                data.append({'Code' :Code, 'Name' :Name, 'Continent' :Continent, 'Region' :Region, 'SurfaceArea' :SurfaceArea, 'IndepYear' :IndepYear, 'Population' :Population, 'LifeExpectancy' :LifeExpectancy, 'GNP' :GNP, 'GNPOld' :GNPOld,'LocalName' :LocalName,'GovernmentForm' :GovernmentForm, 'HeadOfState' :HeadOfState, 'Capital' :Capital, 'Code2' :Code2})
            return data

'''Query SELECT FROM CON WHERE (BUSCAR)'''
def getOnlyCountry(Code):
        conexion = crear_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("SELECT *FROM country WHERE Code=%s",(Code))
            cursor=cursor.fetchall()
            data = []
            for (Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2) in cursor:
                data.append({'Code' :Code, 'Name' :Name, 'Continent' :Continent, 'Region' :Region, 'SurfaceArea' :SurfaceArea, 'IndepYear' :IndepYear, 'Population' :Population, 'LifeExpectancy' :LifeExpectancy, 'GNP' :GNP, 'GNPOld' :GNPOld,'LocalName' :LocalName,'GovernmentForm' :GovernmentForm, 'HeadOfState' :HeadOfState, 'Capital' :Capital, 'Code2' :Code2})
            return data

'''Query DELETE FROM'''
def deleteCountry(Code):
    conexion = crear_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM country WHERE Code=%s",(Code))
    conexion.commit()
    conexion.close()

'''Query UPDATE SET'''
def updateCountrys(Code,Name,Continent,Region,SurfaceArea,IndepYear,Population,LifeExpectancy,GNP,GNPOld,LocalName,GovernmentForm,HeadOfState,Capital,Code2):
    conexion = crear_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE country SET Name = '" + Name + "', Continent = '" + Continent + "', Region = '" + Region + "', SurfaceArea = '" + SurfaceArea + "', IndepYear = '" + IndepYear + "', Population = '" + Population + "', LifeExpectancy = '" + LifeExpectancy + "', GNP = '" + GNP + "', GNPOld = '" + GNPOld + "', LocalName ='" + LocalName + "', GovernmentForm = '" + GovernmentForm + "', HeadOfState = '" + HeadOfState + "', Capital = '" + Capital + "', Code2 = '" + Code2 + "' WHERE Code like '%" + Code + "%'")          
        data = cursor.fetchall()
    conexion.commit()
    conexion.close()
    return data