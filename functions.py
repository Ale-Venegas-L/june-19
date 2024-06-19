contacts = []

def Validator_T(x):
    while len(x) < 2:
        x = input

def contactx():
    print("Agrega contacto: ")
    name = input("Nombre: ")
    cellphone = input("Teléfono: ")
    email = input("Correo: ")
    contact = {"Name": name, 
               "Cellphone": cellphone,
               "E-Mail" : email}
    contacts.append(contact)