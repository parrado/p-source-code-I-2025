# Crea una lista de diccionarios
dogs=[
    {
    "name": "Koky", #name: clave, llave, atributo
    "sex": "male",
    "age": 2,
    "color": "golden"  
},

{
    "name": "Candy",
    "sex":"female",
    "age":4,
    "color":"white"
}
]

dogs.append({
    "name":"Negro",
    "age":1,
    "sex":"male",
    "color":"black"
})

for item in dogs:
    #print(item["age"])
    print(item)

print(dogs[2])