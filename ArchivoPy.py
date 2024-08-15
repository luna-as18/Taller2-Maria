#Funcion que salude a una persona
def saludar(nombre):
    return "Hola " + nombre + "!"

#funcion que se despida de una persona
def despedir(nombre):
    return "Adios " + nombre + "!"

def main():
    print(saludar("Juan"))
    print(despedir("Juan"))

main()