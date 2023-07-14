
asigCitas = []
citas = {}


def crear_cita():
    print("Opción 1: Crear cita")
    
 
def cancelar_cita():
    print("Opción 2: Cancelar cita")

def consultarFech():
    print("Opción 3: Consultar citas por fecha")
  
def consultarPorV():
    print("Opción 4: Consultar citas por veterinario")

def menuCitas():
    while True:
        print("----- Menú Citas-----")
        print("1. Crear cita")
        print("2. Cancelar cita")
        print("3. Consultar citas por fecha")
        print("4. Consultar citas por veterinario")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            crear_cita()
        elif opcion == "2":
            cancelar_cita()
        elif opcion == "3":
            consultarFech()
        elif opcion == "4":
            consultarPorV()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")

menuCitas()


