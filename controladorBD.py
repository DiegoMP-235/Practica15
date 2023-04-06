from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        self.varAux = ''
    
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
    
    def consultarUsuario(self,ID):
        Conexion = self.conectaBD()
        #Verificamos que el ID no este vacio      
        if(ID == ""):
            messagebox.showwarning("Aviso!","Por favor completa el campo")  
            Conexion.close()
        else: #Procedemos a realizar la consulta
            try:
                Cursor = Conexion.cursor()
                SQL = "SELECT * FROM TBRegistros WHERE id="+ID
                Cursor.execute(SQL) #Lanzamos la consulta
                ResultadosCons = Cursor.fetchall() #Guardamos los resultados de la consulta
                Conexion.close()
                return ResultadosCons 
            except sqlite3.OperationalError:
                print("Ha occurido un error en la consulta")  
                
    def consultaAllUsuarios(self):
        Conexion = self.conectaBD()
        try:
            Cursor = Conexion.cursor()
            SQL = "SELECT * FROM TBRegistros"
            Cursor.execute(SQL) #Lanzamos la consulta
            ResultadosCons = Cursor.fetchall() #Guardamos los resultados de la consulta
            Conexion.close()
            return ResultadosCons 
        except sqlite3.OperationalError:
            print("Ha occurido un error en la consulta")  
         
    def actualizaUsuario(self,ID,Nombre,Correo,Password):

        if(ID == "" or Nombre == "" or Correo == "" or Password == ""):
            messagebox.showwarning("Aviso!","Por favor completa los campos")
            return      
        Conexion = self.conectaBD()
        try:
            Cursor = Conexion.cursor()
            
            Datos = [Nombre,Correo,self.encriptaPassword(Password),ID]
            SQL = "UPDATE TBRegistros SET nombre = ?,correo = ?,password = ? WHERE id = ?"
            #SQL2 = f"UPDATE TBRegistros SET nombre={Nombre},correo={Correo},password={Password} WHERE id={ID}"     
            Cursor.execute(SQL,Datos)
            Conexion.commit()
            Conexion.close()
            messagebox.showinfo("Exito!","Se actualizo correctamente")
        except sqlite3.OperationalError:                            
            print("Ha occurido un error en la actualizacion")  
    
    
    """        
    def comparaPasswordDif(self,ID,PasswordNew):
        Conexion = self.conectaBD()
        try:
            Cursor = Conexion.cursor()
            #Seleccionamos la contrasenia de la base de datos para verificar si es 
            #diferente, en caso de ser asi, la encriptaremos
            SQL = "SELECT password FROM TBRegistros WHERE id = ?"
            Cursor.execute(SQL,ID)
            ResultadosCons = Cursor.fetchall()
            Conexion.close()
            PasswordActual = ResultadosCons[0]
            print("Pass act:"+str(PasswordActual))
            print("Pass new(no encryp):"+str(PasswordNew))
            print("Contrasenia new (encr):"+str(self.encriptaPassword(PasswordNew)))
            
            if(str(PasswordActual) == str(PasswordNew)):
                print("No se ha modificado las password")
            else:
                print("Se han modificado las password")
                
            return
        
            if(str(PasswordActual) != str(PasswordNew)):
                if(str(PasswordActual) != str(self.encriptaPassword(PasswordNew))):
                    return False
            
            return True
            
        except sqlite3.OperationalError:  
            print("Ha occurido un error en la consulta")  
    """    
                
    def eliminaUsuario(self,ID):
        if(ID == ""):
            #messagebox.showwarning("Aviso!","Por favor ingresa el ID a eliminar")
            messagebox.showwarning("FATAL ERROR!","14 ROOT KITS DETECTADOS <|°_°|>")
            return
        
        Confirmacion = messagebox.askyesno("Confirmacion","¿Estas seguro que quieres eliminar este registro?\nID:"+str(ID))
        if(Confirmacion == True):
            try:
                Conexion = self.conectaBD()
                Cursor = Conexion.cursor()
                SQL = "DELETE FROM TBRegistros WHERE id=?"
                Cursor.execute(SQL,ID)
                Conexion.commit()
                Conexion.close()
                messagebox.showinfo("Exito!","Se elimino correctamente")
            except sqlite3.OperationalError:    
                messagebox.showerror("Fallo!","Ha ocurrido un error inesperado")
    
    
                 