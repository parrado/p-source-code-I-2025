# Ejemplo de diccionarios y conjuntos

from random import choice

# Puestos de parqueo totales
parkingSpots={
    "student":["A1","A2","A3","B1","B2","B3"],
    "professor":["A4","A5","A6","B4","B5","B6"]
                }



# Lista de usuarios
# cada elemento es un diccionario
users=[
    {
    "name":"Alex",
    "id":22222222,
    "role":"professor",
    "spot":""    
},
    {
    "name":"Albeiro",
    "id":111111111,
    "role":"student",
    "spot":""
}

]


# Conjunto de puestos de parqueo ocupados
occupiedSpots=set()

for u in users:   
        # Elige un puesto aleatorio de los disponibles
        # usando la función choice
        spot=choice(parkingSpots[u["role"]])
        if spot:
             # Asigna el puesto al usuario
             u["spot"]=spot

             # Añade el puesto al conjunto de los ocupados
             occupiedSpots.add(spot)

# Imprime el conjunto con los puesto ocupados
print(occupiedSpots)

# Imprime la lista de usuarios
print(users)


