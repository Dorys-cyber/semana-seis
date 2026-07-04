class Restaurante:
    """
    Gestiona el menú del restaurante.
    Administra la información almacenada en el sistema mediante una lista.
    """

    def __init__(self):
        # Lista genérica para almacenar tanto Platillos como Bebidas
        self.productos = []

    def registrar_producto(self, producto):
        """Registra cualquier objeto que herede de Producto."""
        self.productos.append(producto)
        print(f"\n[Éxito]: '{producto.nombre}' registrado correctamente.")

    def mostrar_productos(self):
        """Muestra todos los productos utilizando el concepto de Polimorfismo."""
        print("\n========== PRODUCTOS EN EL MENÚ ==========")

        if not self.productos:
            print("No existen productos registrados en el menú.")
            return

        # Bucle polimórfico: Llama al método correspondiente según el tipo de objeto
        for producto in self.productos:
            producto.mostrar_informacion()
        print("\n==========================================")