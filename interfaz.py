from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

#Instanciamos un objeto tipo de controladorBD
myControlador = controladorBD()    
#Instancia ventana
paddingY = 5
ventana = Tk()
ventana.title("CRUD users")
ventana.geometry("420x360")

#Guardamos los datos de las entradas y llamamos a la funcion para guardar el usuario
def Guardar():
    Nombre = entradaName.get()
    Correo = entradaCorreo.get()
    Password = entradaPass.get()
    myControlador.guardarUsuario(Nombre,Correo,Password)

def Consultar1Usuario():
    ID = entradaID.get()
    UsuarioCons = myControlador.consultarUsuario(ID)

    if(len(UsuarioCons) < 1):
        messagebox.showinfo("No se encontraron resultados","Este id no se encontro en la base de datos")
        return
    for usuario in UsuarioCons:
        row = "Id:"+str(usuario[0])+" \nNombre:"+usuario[1]+" \nCorreo:"+usuario[2]+" \nContrasenia:"+str(usuario[3])
       
    txtResult.delete('0.0','end')  
    txtResult.insert("0.0",row)
        
#Para el notebook
panel = ttk.Notebook(ventana)
panel.pack(fill="both",expand=True)
pestania1 = ttk.Frame(panel)
pestania2 = ttk.Frame(panel)
pestania3 = ttk.Frame(panel)
pestania4 = ttk.Frame(panel)

#Pestania 1
#Variables para recuperar los datos de los entry
varName = tk.StringVar()
varCorreo = tk.StringVar()
varPass = tk.StringVar()
#Secciones de la pestania
FrameEntradas = Frame(pestania1)
FrameEntradas.pack(expand=True,fill="both")
FrameCntrls = Frame(pestania1)
FrameCntrls.pack(expand=True,fill="both")
LabelTittle = Label(FrameEntradas,text="Registrarse",font=("Arial", 10, "bold"), fg="#333", bg="#f2f2f2", padx=6, pady=6)
LabelTittle.pack(pady=paddingY)
#Entrada para nombre
labelName = Label(FrameEntradas,text="Nombre:")
labelName.pack(pady=paddingY)
entradaName = Entry(FrameEntradas,textvariable=varName)
entradaName.pack(pady=paddingY)
#Para el correo
lblCorreo = Label(FrameEntradas,text="Correo:")
lblCorreo.pack(pady=paddingY)
entradaCorreo = Entry(FrameEntradas,textvariable=varCorreo)
entradaCorreo.pack(pady=paddingY)
#Para la password
lblPass = Label(FrameEntradas,text="Contraseña:")
lblPass.pack(pady=paddingY)
entradaPass = Entry(FrameEntradas,textvariable=varPass,show="¢")
entradaPass.pack(pady=paddingY)

#Pestania 2(consulta de un usuarios)
btnGuardar = Button(FrameCntrls,text="Guardar usuario",command=Guardar)
btnGuardar.pack(pady=paddingY)

#Seccion de consultas
FrameC = Frame(pestania2)
FrameC.pack(expand=True,fill="both")
FrameBTNC = Frame(pestania2)
FrameBTNC.pack(expand=True,fill="both")

TittleC = Label(FrameC,text="Buscar usuario",font=("Arial", 16, "bold"), fg="#00CC33", bg="#f2f2f2", padx=6, pady=6)
TittleC.pack(pady=paddingY)

LblID = Label(FrameC,text="Identificador del usuario:").pack()
entradaID = Entry(FrameC)
entradaID.pack()
#Para mostrar los resultados
LblResul = Label(FrameC,text="Resultados:")
txtResult = tk.Text(FrameC,height=7,width=35,font=("Aria;",12))
txtResult.pack(pady=paddingY)
#Boton de accion de la pestania
BTNCons = Button(FrameBTNC,text="Buscar",command=Consultar1Usuario).pack()

#agregamos las pestaniias al notebook
panel.add(pestania1,text="Formulario de usuarios")
panel.add(pestania2,text="Buscar usuario")
panel.add(pestania3,text="Buscar usuarios")
panel.add(pestania4,text="Actualizar usuario")


ventana.mainloop()
