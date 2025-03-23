import json

RM =json.load(open("RM.json"))

#En madrid, España se ubica el Real Madrid
print(f"En {RM["ubicacion"]["ciudad"]} ,{RM["ubicacion"]["pais"]} se ubica el {RM["nombre"]}")

print() 

#El Real Madrid es el rey de europa con 15 champions league
print(f"El {RM["nombre"]} es el {RM["apodo"]} con {RM["titulos"]["champions_league"]} Champions league")

print() 

#Desde 1902 en el Santiago Bernabéu han jugado futbolistas míticos como:
#lista de jugadores
print(f"Desde {RM["año_fundacion"]} en el {RM["estadio"]} han jugado futbolistas míticos como:")
for posicion in RM["jugadores_destacados"] :
    print(f"*{posicion}:")
    for jugador in RM["jugadores_destacados"][posicion]:
        print(f"--{jugador}")
 
print()       
        
#Este club presidido por Florentino Pérez y entrenado por Carlo Ancelotti tiene 2 colores, el blanco y el morado
print(f"Este club presidido por{RM["presidente"]} y entrenado por {RM["entrenador_actual"]} tiene {len(RM["colores"])}, el {RM["colores"]["principal"]} y el {RM["colores"]["secundario"]}")        
    
print() 

    