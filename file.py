import functions
import os, time

while True:
    os.system("cls")
    print("Menú contactos:")
    print("1. Agregar contacto")
    print("2. Ver contacto")
    print("3. Exportar CVS")
    print("4. Salir")
    print("Ingresa opción")
    try:
        opc = int(input)
    except:
        print("Debe ingresar un número!")
    if opc == 1:
        print("Soy un cacahuate!!!!")
    elif opc == 2:
        print("MEMBRISHO!")
    elif opc == 3:
        print("NYAAAA :3")
    else:
        pass