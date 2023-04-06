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
ventana.geometry("510x360")

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
    
def ConultarAllUsers():
    ResultadoUsers = myControlador.consultaAllUsuarios() 
    
    for i in tree.get_children():
        tree.delete(i)
     
    for Usuario in ResultadoUsers:
        tree.insert("",END,values=(Usuario[0],Usuario[1],Usuario[2],Usuario[3]))

def buscarIDActualizar():
    ID = IDAct.get()
    Resultado = myControlador.consultarUsuario(ID)
    if(len(Resultado) < 1):
        messagebox.showinfo("No se encontraron resultados","Este id no se encontro en la base de datos")
        return
    
    activaCampos()
    for usuarioAct in Resultado:
        #print(str(usuarioAct[1])+str(usuarioAct[2]+str(usuarioAct[3])))
        EntradaNameAct.insert(0,usuarioAct[1])
        EntradaCorreoAct.insert(0,usuarioAct[2])
        #EntradaPasswordAct.insert(0,usuarioAct[3])
    myControlador.varAux = ID
    IDAct.config(state="readonly")   
    activaBtnAct()


def activaCampos():
    EntradaNameAct.config(state="normal")
    EntradaCorreoAct.config(state="normal")
    EntradaPasswordAct.config(state="normal")

def activaBtnAct():
    BtnActualizar.config(state="normal")    
def activaBtnDel():
    BtnEliminar.config(state="normal")   
def actualizaUser():
    ID = myControlador.varAux
    NombreAct = EntradaNameAct.get()
    CorreoAct = EntradaCorreoAct.get()
    PasswordAct = EntradaPasswordAct.get()

    #print(ID,NombreAct,CorreoAct,PasswordAct)
    
    myControlador.actualizaUsuario(ID,NombreAct,CorreoAct,PasswordAct)      
def habilitaCamposDEL():
    txtNameDEL.config(state="normal")
    txtCorreoDEL.config(state="normal")
def deshabilitaCampos():
    txtNameDEL.config(state="disabled")
    txtCorreoDEL.config(state="disabled")
    
def buscaEliminacion():
    ID = IDDel.get()
    Resultado = myControlador.consultarUsuario(ID)
    if(len(Resultado) < 1):
        messagebox.showinfo("No se encontraron resultados","Este id no se encontro en la base de datos")
        return
    
    habilitaCamposDEL()    
    for Usuario in Resultado:
        txtNameDEL.insert(0,Usuario[1])
        txtCorreoDEL.insert(0,Usuario[2])
    deshabilitaCampos()   
    activaBtnDel() 
 
def eliminarUsuario():   
    ID = IDDel.get()
    myControlador.eliminaUsuario(ID)   

def restablecePestAct():
    EntradaNameAct.delete(0,END)
    EntradaCorreoAct.delete(0,END)
    EntradaPasswordAct.delete(0,END)
    EntradaNameAct.config(state="disabled")
    EntradaCorreoAct.config(state="disabled")
    EntradaPasswordAct.config(state="disabled")  
    IDAct.config(state="normal") 
    IDAct.delete(0,END)
    BtnActualizar.config(state="disabled")
       
#Para el notebook
panel = ttk.Notebook(ventana)
panel.pack(fill="both",expand=True)
pestania1 = ttk.Frame(panel)
pestania2 = ttk.Frame(panel)
pestania3 = ttk.Frame(panel)
pestania4 = ttk.Frame(panel)
pestania5 = ttk.Frame(panel)



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

btnGuardar = Button(FrameCntrls,text="Guardar usuario",command=Guardar)
btnGuardar.pack(pady=paddingY)

#Pestania 2(consulta de un usuarios)
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

#Elementos de la pestania 3

FrameC2 = Frame(pestania3)
FrameC2.pack(expand=True,fill="both")
FrameContC2 = Frame(pestania3)
FrameContC2.pack(expand=True,fill="both")
window_width = ventana.winfo_width()

LblTituloC2 = Label(FrameC2,text="Buscar usuarios",font=("Arial", 16, "bold"), fg="#00CC33", bg="#f2f2f2", padx=6, pady=6)
LblTituloC2.pack()
btnConsAll =  Button(FrameC2,command=ConultarAllUsers,text='Listar')
btnConsAll.pack()

#Scrollbar vertical
scrollbar = tk.Scrollbar(FrameContC2,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)

#scrollbar horizontal
scrollbar2 = tk.Scrollbar(FrameContC2,orient="horizontal")
scrollbar2.pack(side="bottom",fill=X)

#Ponemos encabezados de los campos de la bd
Columnas = ('ID','Nombre','Correo','Password')
tree = ttk.Treeview(FrameContC2,columns=Columnas,show='headings',yscrollcommand=scrollbar.set,xscrollcommand=scrollbar2.set)
tree.heading('ID', text='ID')
tree.heading('Nombre', text='Nombre')
tree.heading('Correo', text='Correo')
tree.heading('Password', text='Contrasenia')
tree.pack(fill='both', expand=True)

#Configuramos el scroll
scrollbar.config(command=tree.yview)
scrollbar2.config(command=tree.xview)

#pestania de actualizacion
FActEnt = Frame(pestania4)
FActEnt.pack(expand=True,fill="both")

FActBtn = Frame(pestania4)
FActBtn.pack(expand=True,fill="both")

TittleAct = Label(FActEnt,text="Actualizar usuario",font=("Arial", 14, "bold"), fg="#00CC33", bg="#f2f2f2", padx=6, pady=6)
TittleAct.pack()

LblIdAct = Label(FActEnt,text="ID a actualizar")
LblIdAct.pack(pady=paddingY)

#Entrada para el texto a actualizar
IDAct = Entry(FActEnt)
IDAct.pack()

BtnCons = Button(FActEnt,text="Buscar",command=buscarIDActualizar)
BtnCons.pack(pady=paddingY)
BtnRestCamp = Button(FActEnt,text="Restablecer",command=restablecePestAct)
BtnRestCamp.pack()

#Campos donde se cargaran los datos a actualizar
LblName = Label(FActEnt,text="Nombre")
LblName.pack()
EntradaNameAct = Entry(FActEnt)
EntradaNameAct.pack()
EntradaNameAct.config(state="disabled")


LblCorreoAct = Label(FActEnt,text="Correo")
LblCorreoAct.pack()
EntradaCorreoAct = Entry(FActEnt)
EntradaCorreoAct.pack()
EntradaCorreoAct.config(state="disabled")

LblPassAct = Label(FActEnt,text="Contraseña")
LblPassAct.pack()

EntradaPasswordAct = Entry(FActEnt,show="*")
EntradaPasswordAct.pack()
EntradaPasswordAct.config(state="disabled")

#Boton de accion para actualizar
BtnActualizar = Button(FActBtn,text="Actualizar",command=actualizaUser)
BtnActualizar.pack()
BtnActualizar.config(state="disabled")

#Pestania 5, Eliminacion
FEliEnt = Frame(pestania5)
FEliEnt.pack(expand=True,fill="both")

FEliBtn = Frame(pestania5)
FEliBtn.pack(expand=True,fill="both")

TittleDel = Label(FEliEnt,text="Eliminar usuario",font=("Arial", 14, "bold"), fg="#00CC33", bg="#f2f2f2", padx=6, pady=6)
TittleDel.pack()

LblIdDel = Label(FEliEnt,text="ID a eliminar")
LblIdDel.pack(pady=paddingY)

#Entrada para el ID a eliminar
IDDel = Entry(FEliEnt)
IDDel.pack()

BtnBuscaEliminar = Button(FEliEnt,text="Buscar",command=buscaEliminacion)
BtnBuscaEliminar.pack(pady=paddingY)


#Muestra la informacion asociada al ID a eliminar
LblNameDEL = Label(FEliEnt,text="Nombre")
LblNameDEL.pack()
txtNameDEL = Entry(FEliEnt)
txtNameDEL.pack()
txtNameDEL.config(state="disabled")


LblCorreoDEL = Label(FEliEnt,text="Correo")
LblCorreoDEL.pack()
txtCorreoDEL = Entry(FEliEnt)
txtCorreoDEL.pack()
txtCorreoDEL.config(state="disabled")

#Boton de la accion eliminar
BtnEliminar = Button(FEliBtn,text="Eliminar",command=eliminarUsuario)
BtnEliminar.pack(pady=paddingY)
BtnEliminar.config(state="disabled")



#agregamos las pestaniias al notebook
panel.add(pestania1,text="Formulario de usuarios")
panel.add(pestania2,text="Buscar usuario")
panel.add(pestania3,text="Buscar usuarios")
panel.add(pestania4,text="Actualizar usuario")
panel.add(pestania5,text="Eliminar usuario")


ventana.mainloop()
