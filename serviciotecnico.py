# Crea un sistema que almacene órdenes de servicio técnico en una lista, donde cada orden está representada por un diccionario con detalles como ID de orden, descripción del problema, y estado 
# de la reparación. Implementa la actualización del estado de cada orden basado en la entrada del usuario y muestra las órdenes pendientes y completadas.

class OrdenServicio:
    def __init__(self, id_orden, descripcion, estado):
        self.id_orden = id_orden
        self.descripcion = descripcion
        self.estado = estado

class SistemaServicioTecnico:
    def __init__(self):
        self.ordenes = []

    def agregar_orden(self, id_orden, descripcion, estado):
        orden = OrdenServicio(id_orden, descripcion, estado)
        self.ordenes.append(orden)

    def actualizar_estado(self, id_orden, nuevo_estado):
        for orden in self.ordenes:
            if orden.id_orden == id_orden:
                orden.estado = nuevo_estado
                return True
        return False

    def mostrar_ordenes_pendientes(self):
        print("Órdenes Pendientes:")
        for orden in self.ordenes:
            if orden.estado == "pendiente":
                print(f"ID: {orden.id_orden}, Descripción: {orden.descripcion}, Estado: {orden.estado}")

    def mostrar_ordenes_completadas(self):
        print("Órdenes Completadas:")
        for orden in self.ordenes:
            if orden.estado == "completada":
                print(f"ID: {orden.id_orden}, Descripción: {orden.descripcion}, Estado: {orden.estado}")

# Ejemplo de uso del sistema
sistema = SistemaServicioTecnico()

# Agregar algunas órdenes
sistema.agregar_orden(1, "Pantalla rota", "pendiente")
sistema.agregar_orden(2, "Problemas de sonido", "pendiente")

# Mostrar órdenes pendientes
sistema.mostrar_ordenes_pendientes()

# Actualizar estado de una orden
sistema.actualizar_estado(1, "completada")

# Mostrar órdenes completadas
sistema.mostrar_ordenes_completadas()
