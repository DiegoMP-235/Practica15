from tkinter import *
from tkinter import ttk
import tkinter as tk

def Guardar():
    Nombre = entradaName.get()
    Correo = entradaCorreo.get()
    Password = entradaPass.get()
#Instancia ventana
paddingY = 5
ventana = Tk()
ventana.title("CRUD users")
ventana.geometry("420x360")
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
entradaPass = Entry(FrameEntradas,textvariable=varPass)
entradaPass.pack(pady=paddingY)

#Seccion de controles de la pestania
btnGuardar = Button(FrameCntrls,text="Guardar usuario",command=Guardar)
btnGuardar.pack(pady=paddingY)

#agregamos las pestaniias al notebook
panel.add(pestania1,text="Formulario de usuarios")
panel.add(pestania2,text="Buscar usuario")
panel.add(pestania3,text="Buscar usuarios")
panel.add(pestania4,text="Actualizar usuario")


ventana.mainloop()
