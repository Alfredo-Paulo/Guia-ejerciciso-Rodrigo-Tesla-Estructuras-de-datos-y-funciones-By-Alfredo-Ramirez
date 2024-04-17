# Crea una lista de diccionarios, donde cada diccionario representa un dispositivo IoT con atributos como ID, tipo, ubicación, estado (activo/inactivo), y temperatura. Escribe un bloque de 
# código que recorra esta lista y actualice el estado de los dispositivos basándose en su temperatura: si es mayor a 75 grados, el estado debe cambiar a "inactivo". Además, imprime la lista de  # dispositivos que requieren mantenimiento (aquellos con estado "inactivo"). La temperatura deberá ser asignada mediante el uso de la librería Random.

import random

# Crear una lista de diccionarios de dispositivos IoT
dispositivos = [
    {"ID": 1, "tipo": "sensor", "ubicación": "oficina", "estado": "activo", "temperatura": random.randint(70, 80)},
    {"ID": 2, "tipo": "cámara", "ubicación": "exterior", "estado": "activo", "temperatura": random.randint(70, 80)},
    {"ID": 3, "tipo": "sensor", "ubicación": "sala de servidores", "estado": "activo", "temperatura": random.randint(70, 80)}
]

# Función para actualizar el estado de los dispositivos basado en la temperatura
def actualizar_estado(dispositivos):
    dispositivos_mantenimiento = []
    for dispositivo in dispositivos:
        temperatura = dispositivo["temperatura"]
        if temperatura > 75:
            dispositivo["estado"] = "inactivo"
            dispositivos_mantenimiento.append(dispositivo)
    return dispositivos_mantenimiento

# Actualizar estados
dispositivos_mantenimiento = actualizar_estado(dispositivos)

# Imprimir lista de dispositivos que requieren mantenimiento
print("Dispositivos que requieren mantenimiento:")
for dispositivo in dispositivos_mantenimiento:
    print("ID:", dispositivo["ID"], "- Tipo:", dispositivo["tipo"], "- Ubicación:", dispositivo["ubicación"])
