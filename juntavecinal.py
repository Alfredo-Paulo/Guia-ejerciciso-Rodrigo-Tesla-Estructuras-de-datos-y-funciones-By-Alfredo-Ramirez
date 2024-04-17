# Desarrolla un diccionario que almacene la información de los miembros de una junta vecinal, usando su número de identificación como clave y un diccionario con su nombre y dirección como 
# valor. Implementa la adición de nuevos miembros y la eliminación de miembros existentes del registro

class JuntaVecinal:
    def __init__(self):
        self.miembros = {}

    def agregar_miembro(self, id, nombre, direccion):
        if id not in self.miembros:
            self.miembros[id] = {'nombre': nombre, 'direccion': direccion}
            print(f"Se ha agregado al miembro con ID {id}")
        else:
            print("El miembro ya existe en el registro.")

    def eliminar_miembro(self, id):
        if id in self.miembros:
            del self.miembros[id]
            print(f"Se ha eliminado al miembro con ID {id}")
        else:
            print("El miembro no existe en el registro.")

    def mostrar_miembros(self):
        print("Miembros de la Junta Vecinal:")
        for id, info in self.miembros.items():
            print(f"ID: {id}, Nombre: {info['nombre']}, Dirección: {info['direccion']}")


# Ejemplo de uso:
junta = JuntaVecinal()

# Agregar miembros
junta.agregar_miembro(1, 'Juan Pérez', 'Calle A #123')
junta.agregar_miembro(2, 'María Gómez', 'Calle B #456')
junta.agregar_miembro(3, 'Luis Rodríguez', 'Calle C #789')

# Mostrar miembros
junta.mostrar_miembros()

# Eliminar miembro
junta.eliminar_miembro(2)

# Mostrar miembros actualizados
junta.mostrar_miembros()
