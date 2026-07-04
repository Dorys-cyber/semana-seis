class Producto:
    """
    Representa un producto general dentro del restaurante.
    Actúa como clase padre para demostrar el concepto de herencia y encapsulación.
    """

    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.__precio = precio  # Atributo privado (Encapsulación)
        self.disponible = disponible  # Atributo común solicitado por la rúbrica

    def obtener_precio(self):
        """Devuelve el precio del producto (Getter)."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """Actualiza el precio validando que sea mayor a cero (Setter)."""
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("\n[Error]: El precio debe ser mayor que cero.")

    def mostrar_informacion(self):
        """Método base que será sobrescrito por las clases hijas."""
        estado = "Disponible" if self.disponible else "No disponible"
        print("\n=== PRODUCTO ===")
        print(f"Nombre       : {self.nombre}")
        print(f"Precio       : ${self.__precio:.2f}")
        print(f"Estado       : {estado}")