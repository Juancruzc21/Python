from tkinter import *
from math import *

ventana = Tk()
ventana.title("Mi calculadora")
ventana.configure(background="gray25")
ventana.geometry("390x480")
ventana.resizable(0,0)

colorBoton = "steelblue"
colorOperadores = "red"
colorIgualClear = "magenta"
anchoBoton = 10
altoBoton = 3

operador = ""
textoPantalla = StringVar()
def clear():
    global operador
    operador = ""
    textoPantalla.set(0)
    

def click(b):
    global operador
    operador += str(b)
    textoPantalla.set(operador)
    
def resultado():
    global operador
    try:
        r = str(eval(operador))
    except:
        r = "Flasheaste pa"
    textoPantalla.set(r)    

clear()        

#BOTONES PRIMER FILA
boton0 = Button(ventana,text = "0",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(0)).grid(row = 1,column = 0, pady = 10) 
boton1 = Button(ventana,text = "1",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(1)).grid(row = 1,column = 1, pady = 10) 
boton2 = Button(ventana,text = "2",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(2)).grid(row = 1,column = 2, pady = 10)
boton3 = Button(ventana,text = "3",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(3)).grid(row = 1,column = 3, pady = 10)
#BOTONES SEGUNDA FILA
boton4 = Button(ventana,text = "4",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(4)).grid(row = 2,column = 0, pady = 10) 
boton5 = Button(ventana,text = "5",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(5)).grid(row = 2,column = 1, pady = 10) 
boton6 = Button(ventana,text = "6",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(6)).grid(row = 2,column = 2, pady = 10)
boton7 = Button(ventana,text = "7",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(7)).grid(row = 2,column = 3, pady = 10)

#BOTONES Tercera FILA
boton8 = Button(ventana,text = "8",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(8)).grid(row = 3,column = 0, pady = 10) 
boton9 = Button(ventana,text = "9",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(9)).grid(row = 3,column = 1, pady = 10) 
botonPi = Button(ventana,text = "π",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click("pi")).grid(row = 3,column = 2, pady = 10)
botonPunto = Button(ventana,text = ".",bg = colorBoton, width = anchoBoton, height = altoBoton, command = lambda:click(".")).grid(row = 3,column = 3, pady = 10)

#BOTONES Cuarta FILA
botonSuma = Button(ventana,text = "+",bg = colorOperadores, width = anchoBoton, height = altoBoton, command = lambda:click("+")).grid(row = 4,column = 0, pady = 10) 
botonResta = Button(ventana,text = "-",bg = colorOperadores, width = anchoBoton, height = altoBoton, command = lambda:click("-")).grid(row = 4,column = 1, pady = 10) 
botonMulti = Button(ventana,text = "x",bg = colorOperadores, width = anchoBoton, height = altoBoton, command = lambda:click("*")).grid(row = 4,column = 2, pady = 10)
botondivi = Button(ventana,text = "/",bg = colorOperadores, width = anchoBoton, height = altoBoton, command = lambda:click("/")).grid(row = 4,column = 3, pady = 10)

#BOTONES Quinta FILA
botonClear = Button(ventana,text = "C",bg = colorIgualClear, width = anchoBoton, height = altoBoton, command = clear).grid(row = 5,column = 1, pady = 10)
botonIgual = Button(ventana,text = "=",bg = colorIgualClear, width = anchoBoton, height = altoBoton, command = resultado).grid(row = 5,column = 2, pady = 10)



Pantalla = Entry(ventana,font=("chiller", 20,"bold"),width = 22, borderwidth = 5,background = "steelblue", textvariable = textoPantalla)
Pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 32, pady = 20)


ventana.mainloop()
