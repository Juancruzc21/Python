print("#### Hola... Aqui calcularemos el promedio de los alumnos####")

nombre = input("Ingrese el nombre del alumno: ")

matematica = float(input("Ingresa la nota del matematica: "))
quimica = float(input("Ingresa la nota de quimica: "))            
biologia = float(input("Ingresa la nota de biologia: "))
ingles = float(input("Ingresa la nota de ingles: \n"))

print("Tu nota en matematica es: ", matematica)
print("Tu nota en quimica es: ", quimica)
print("Tu nota en biologia es: ", biologia)
print("Tu nota en ingles es: ", ingles, "\n")

promedio = (matematica + quimica + biologia + ingles) /3
print("Tu promedio es de: ", promedio, "\n")

if promedio >= 7 :
      print("Felicidades " + nombre , "aprobaste!")
else:
    print("Lamentablemente, desaprobaste")

input('Press ENTER to continue...')
