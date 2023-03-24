from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
    
    def conectaBD(self):
        try:
            Conexion = sqlite3.connect('UsuariosDB.db')#C:/Users/mungu/Desktop/5to_Cuatrimestre/POO/3erParcial/Practica15/Practica15/UsuariosDB.db
            print("Conectado a la base de datos")
            return Conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar :/")
            
    def guardarUsuario(self,Nombre,Correo,Password):
        #Solicitamos la conexion
        Conexion = self.conectaBD()
        #Comprobamos que no esten vacios los campos
        if(Nombre == "" or Correo == "" or Password == ""):
            messagebox.showwarning("Aviso!","Completa los campos")
            Conexion.close()
        else:
            #Preparamos la insercion SQL
            Cursor = Conexion.cursor()
            Datos=[Nombre,Correo,self.encriptaPassword(Password)]
            SQL = "INSERT INTO TBRegistros(nombre,correo,password) VALUES(?,?,?)"
            #Procedemos a realizar la insercion y cerrar la conexion
            Cursor.execute(SQL,Datos)
            Conexion.commit()
            Conexion.close()
            messagebox.showinfo("Exito","Se inserto correctamente")
            
    def encriptaPassword(self,Password):   
        PasswordPlain = Password
        PasswordPlain = PasswordPlain.encode() #Convierte la contrasenia a bytes
        sal = bcrypt.gensalt()
        conHa = bcrypt.hashpw(PasswordPlain,sal)
        return conHa     
                        
                 