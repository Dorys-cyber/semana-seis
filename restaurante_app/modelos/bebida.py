from modelos.producto import Producto

class Bebida(Producto):
    """
    Representa una bebida.
    Hereda de Producto e incorpora el tamaño en mililitros.
    """

    def __init__(self, nombre, precio, tamano_ml):
        # Llama al constructor de la clase padre (Producto)
        super().__init__(nombre, precio)
        self.tamano_ml = tamano_ml  # Atributo específico (Entero)

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase Producto (Polimorfismo)."""
        estado = "Disponible" if self.disponible else "No disponible"
        print("\n=== BEBIDA ===")
        print(f"Nombre    : {self.nombre}")
        print(f"Precio    : ${self.obtener_precio():.2f}")
        print(f"Tamaño    : {self.tamano_ml} ml")
        print(f"Estado    : {estado}")