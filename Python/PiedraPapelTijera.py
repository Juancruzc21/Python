import random
import tkinter as tk


ventana = tk.Tk()
ventana.title('PPT BETA')
ventana.geometry('480x480')
ventana.configure(background = 'steelblue')

ventana.mainloop()


respuesta = "si"
while respuesta == 'si':
        opciones = ['Piedra','Papel','Tijera']
        eleccionRival = random.randint(0,2)
        rival = opciones[eleccionRival]
        jugador = input("Elegi que queres hacer (Solo la primer letra en mayuscula): ")
        print("tu eleccion fue: " ,jugador)
        print("El rival hizo: ", rival)

        if (jugador == rival):
                print("Empate")

        if (jugador == "Piedra"):
            if(rival == "Papel"):
                print("Gana el rival")
            elif(rival == "Tijera"):
                print("Gana el jugador")
               
        if (jugador == "Papel"):
            if(rival == "Tijera"):
                print("Gana el rival")
            elif(rival == "Piedra"):
                print("Gana el jugador")

        if (jugador == "Tijera"):
            if(rival == "Piedra"):
                print("Gana el rival")
            elif(rival == "Papel"):
                print("Gana el jugador")
                        
        respuesta = input("Queres seguir jugando? ")

        
