import json
import os
import random
from datetime import datetime

asigCitas = []
def cargarasigCitas():
    if os.path.exists('Citas.json'):
        with open('Citas.json', 'r') as cala:
            asigCitas.extend(json.load(cala))
def crear_cita():
    citaId = random.randint(1, 1000)
    citaFecha = datetime.now().strftime('%Y-%m-%d')
    citaHora = int(input('Ingrese la hora de la cita: '))
    veterinario = input('Ingrese el nombre del veterinario: ')

    asigCitas.append({
        'citaId': citaId,
        'citaFecha': citaFecha,
        'citaHora': citaHora,
        'veterinario': veterinario
    })

    with open('citas.json', 'w') as cala:
        json.dump(asigCitas, cala, indent=4)
cargarasigCitas()
crear_cita()



    
 
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

        opcion = int(input("Selecciona una opción: "))

        if opcion == 1:
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



