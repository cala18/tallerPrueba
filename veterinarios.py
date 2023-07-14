'''
import json

veterinarios = []

def addVeterinario():
    idV = input('ID del veterinario: ')
    nameV = input('Nombre del veterinario: ')
    tituloV = input('Título del veterinario: ')

    veterinarios.append({
        'id': idV,
        'name': nameV,
        'titulo': tituloV
    })
    print(veterinarios)

    with open('veterinarios.json', 'w') as archivo:
        json.dump(veterinarios, archivo, indent=3)

addVeterinario()


def buscarVeterinario():
    buscar = input('ingrese el nombre del veterinario')

    


'''
import json
import os

veterinarios = []

def cargarVeterinarios():
    if os.path.exists('veterinarios.json'):
        with open('veterinarios.json', 'r') as archivo:
            veterinarios.extend(json.load(archivo))

def guardarVeterinarios():
    with open('veterinarios.json', 'w') as archivo:
        json.dump(veterinarios, archivo, indent=3)

def addVeterinario():
    idV = input('ID del veterinario: ')
    nameV = input('Nombre del veterinario: ')
    tituloV = input('Título del veterinario: ')

    veterinarios.append({
        'id': idV,
        'name': nameV,
        'titulo': tituloV
    })
    print(veterinarios)
    guardarVeterinarios()

cargarVeterinarios()
addVeterinario()
