from modelos.producto import Producto

class Platillo(Producto):
    """
    Representa un platillo de comida.
    Hereda de Producto e incorpora si es vegano o no.
    """

    def __init__(self, nombre, precio, es_vegano):
        # Llama al constructor de la clase padre (Producto)
        super().__init__(nombre, precio)
        self.es_vegano = es_vegano  # Atributo específico (Booleano)

    def mostrar_informacion(self):
        """Sobrescribe el método de la clase Producto (Polimorfismo)."""
        estado = "Disponible" if self.disponible else "No disponible"
        print("\n=== PLATILLO ===")
        print(f"Nombre    : {self.nombre}")
        print(f"Precio    : ${self.obtener_precio():.2f}")
        print(f"¿Vegano?  : {'Sí' if self.es_vegano else 'No'}")
        print(f"Estado    : {estado}")