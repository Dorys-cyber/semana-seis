from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def mostrar_menu():
    print("\n========================================")
    print("      SISTEMA DE GESTIÓN DE RESTAURANTE")
    print("========================================")
    print("1. Registrar platillo")
    print("2. Registrar bebida")
    print("3. Mostrar todos los productos")
    print("4. Salir")
    print("========================================")

def main():
    restaurante = Restaurante()
    print("\n[Sistema Inicializado Correctamente]")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            print("\n=== REGISTRAR PLATILLO ===")
            nombre = input("Nombre del platillo: ").strip()
            try:
                precio = float(input("Precio ($): "))
                opcion_vegano = input("¿Es vegano? (s/n): ").strip().lower()
                es_vegano = opcion_vegano == 's'
                platillo = Platillo(nombre, precio, es_vegano)
                restaurante.registrar_producto(platillo)
            except ValueError:
                print("\n[Error]: Ingrese un precio válido.")

        elif opcion == "2":
            print("\n=== REGISTRAR BEBIDA ===")
            nombre = input("Nombre de la bebida: ").strip()
            try:
                precio = float(input("Precio ($): "))
                tamano_ml = int(input("Tamaño (en ml): "))
                bebida = Bebida(nombre, precio, tamano_ml)
                restaurante.registrar_producto(bebida)
            except ValueError:
                print("\n[Error]: Ingrese valores numéricos válidos.")

        elif opcion == "3":
            restaurante.mostrar_productos()

        elif opcion == "4":
            print("\nGracias por utilizar el sistema. ¡Hasta luego!")
            break
        else:
            print("\n[Opción no válida]: Intente nuevamente.")

if __name__ == "__main__":
    main()