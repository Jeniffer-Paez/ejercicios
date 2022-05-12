"""Costo_de_una_llamada"""

print("---------------------")
print("----costo llamada----")
print("---------------------")

#input
duracion_llamada = input("digite la duracion de la llamada")
duracion_llamada = int(duracion_llamada)

#processing 
if duracion_llamada > 3:
    costo_llamada = 300 + 50*(duracion_llamada - 3)
else:
    costo_llamada = 300 

#output 
print("el costo de la llamada es" + str(costo_llamada))

#fin 