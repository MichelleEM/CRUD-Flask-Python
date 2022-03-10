import pymysql

def crear_conexion():
       return pymysql.connect(host='localhost', user='root', password='SHINeeJongTae2213', db='world', port=3306)
    