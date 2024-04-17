# Crea un diccionario donde cada clave es un género literario y su valor es otro diccionario con libros y sus respectivas cantidades en stock. Añade al menos tres géneros con dos libros cada 
# uno. Implementa una función para actualizar la cantidad de un libro específico y otra para imprimir el stock total de la librería.

libreria = {
    "Fantasía": {"El Señor de los Anillos": 10, "Harry Potter y la Piedra Filosofal": 15},
    "Ciencia Ficción": {"Dune": 5, "El Juego de Ender": 8},
    "Misterio": {"El Código Da Vinci": 20, "Sherlock Holmes: Estudio en Escarlata": 12}
}

def actualizar_stock(genero, libro, cantidad):
    if genero in libreria and libro in libreria[genero]:
        libreria[genero][libro] = cantidad
        print(f"Stock actualizado para '{libro}' en el género '{genero}' a {cantidad}.")
    else:
        print(f"El libro '{libro}' en el género '{genero}' no existe en la librería.")

def imprimir_stock_total():
    print("Stock total de la librería:")
    for genero, libros in libreria.items():
        print(f"Género: {genero}")
        for libro, cantidad in libros.items():
            print(f"- {libro}: {cantidad}")
        print()

# Ejemplo de uso
print("Stock inicial:")
imprimir_stock_total()

actualizar_stock("Fantasía", "El Señor de los Anillos", 8)
actualizar_stock("Ciencia Ficción", "Dune", 3)

print("\nStock actualizado:")
imprimir_stock_total()
