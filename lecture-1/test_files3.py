
# Abre archivo con manejo de excepción
try:
    # Solicita nombre de archivo al usuario 
    # e intenta abrir para lectura
    file=open(input('Ingrese el nombre del archivo: '))

    # Lee las líneas del archivo
    users=file.readlines()

    # Imprime la líneas leída
    for u in users:
        print(u)

    # Cierra el archivo
    file.close()
except FileNotFoundError:
    # Si se genera excepción
    print('El archivo no existe')


