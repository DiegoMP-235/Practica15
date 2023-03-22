import sqlite3

class Funciones:
    def __init__(self,BaseDatos):
        self.__BaseDatos = BaseDatos
        self.__Conexion= self.__conectaBD()
        
    def __conectaBD(self):
        conexion = sqlite3.connect(self.__BaseDatos)
        return conexion 
       
    def __cierraConexion(self):
        self.__Conexion.close()
        
    def insertar(self,Tabla):
        conexion = self.__Conexion
        estado = conexion.cursor()
        Sentencia = "INSERT INTO "+Tabla