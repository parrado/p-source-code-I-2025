  # Crea archivo my_data.txt
    #file=open('C:\\Users\\samae\\Documents\\docencia-uq\\II-2024\\Programming\\slides\\lecture-1-sources\\my_data.txt','xt')
file=open('my_data.txt','x')


# Solicita datos al usuario
name=input('Ingrese su nombre: ')
id=int(input('Ingrese su cédula: '))

data={"name":name,"id":id}

# Escribe el texto en el archivo
file.write(dumps(data)+"\n")

# Cierra el archivo
file.close()