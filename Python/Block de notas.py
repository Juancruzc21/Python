from tkinter import *
from tkinter import filedialog as f
from io import open

#Ventana del editor
titulo = " || Block de notas en Python"
root = Tk()
root.title(titulo)

#Url de archivo

archivoUrl = ""

#Funciones

def nuevoArchivo():
    global archivoUrl
    texto.delete(1.0, "end")
    archivoUrl = ""
    root.title(archivoUrl + titulo)

def abrirArchivo():
    global archivoUrl
    archivoUrl = f.askopenfilename(initialdir = '.', filetype =(("Archivos de texto","*.txt" ),), title = "Abrir archivo ") 

    if archivoUrl != "":
        file = open(archivoUrl, 'r')
        content = file.read()
        texto.delete(1.0, "end")
        texto.insert('insert', content)
        file.close()
    
    root.title(archivoUrl + titulo)

def guardarArchivo():
    global archivoUrl
    if archivoUrl != "":
        content = texto.get(1.0,"end-1c")
        file = open(archivoUrl, 'w+')
        file.write(content)
        root.title("Archivo guardado " + archivoUrl + titulo)
        file.close()
    else:
        file = f.asksaveasfile(title = "Guardar archivo ", mode = 'w', defaultextension = ".txt")
        if file is not None:
            archivoUrl = file.name
            content = texto.get(1.0,"end-1c")
            file = open(archivoUrl, 'w+')
            file.write(content)
            root.title("Archivo guardado " + archivoUrl + titulo)
            file.close
        else:
            archivoUrl = ""
            root.title("Guardado cancelado " + archivoUrl + titulo)
            
            
           
#Menú

bar = Menu(root)

file_menu = Menu(bar, tearoff = 0)

file_menu.add_command(label = "Nuevo archivo ", command = nuevoArchivo)         #file_menu.add_command() = es para la opcion a elegir
file_menu.add_separator()                              #file_menu.add_separator() = es para el separador de esas opciones 
file_menu.add_command(label = "Abrir archivo ", command = abrirArchivo)
file_menu.add_separator()
file_menu.add_command(label = "Guardar archivo ", command = guardarArchivo)
file_menu.add_separator()
file_menu.add_command(label = "Salir ", command = root.quit)
file_menu.add_separator()

#Se añade el desplegable

bar.add_cascade(menu = file_menu, label = "Archivo")

#Caja de texto

texto = Text(root)
texto.pack(fill = "both", expand = 1)
texto.config(bd = 0, padx = 6, pady = 5, font = ("Arial", 18))

#Run

root.config(menu = bar)


