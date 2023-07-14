import json
import random
from datetime import datetime
import os

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
