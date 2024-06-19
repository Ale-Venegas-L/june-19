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
    opc = int(input())
    if opc == 1:
       os.system("cls")
       functions.contactx()
    elif opc == 2:
        os.system("cls")
        functions.read()
    elif opc == 3:
        os.system("cls")
        print("NYAAAA :3")
    else:
        pass