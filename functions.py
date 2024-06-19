contacts = []
def contactx():
    print("Agrega contacto: ")
    name = input("Nombre: ")
    cellphone = input("Teléfono: ")
    email = input("Correo: ")
    contact = {"Name": name, 
               "Cellphone": cellphone,
               "E-Mail" : email}
    contacts.append(contact)

def read():
    if len(contacts) == 0:
        print(f"Wuaja no tiene amigos q luser\nIngrese uno en la primera opción")
    else:
        for c in contacts:
            print(f"Nombre: {c["Name"]}")
            print(f"Teléfono: {c["Cellphone"]}")
            print(f"Correo: {c["E-Mail"]}")