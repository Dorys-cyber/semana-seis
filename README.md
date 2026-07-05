Estudiante: Dorys Jeaneth Torres Guerrero
Programación Orientada a Objetos

1. Descripción del Sistema: Este sistema es una aplicación modular de consola creada en Python, enfocada en la administración de los productos de un restaurante, ofrece la capacidad de registrar en tiempo real dos categorías de productos: alimentos (`Platillos`) y bebidas (`Bebidas`), guardándolos dentro de un servicio centralizado que manipula el menú del lugar.

2. Estructura del Proyecto: El proyecto se organiza bajo una estructura limpia y modular dividida en diferentes roles: * `modelos/`: Contiene las clases que representan las entidades de negocio (`Producto`, `Platillo`, `Bebida`). * `servicios/`: Contiene la lógica empresarial que gestiona la recopilación de productos mediante la clase `Restaurante`. * `main. py`: Es la puerta de acceso de la aplicación que se comunica con el usuario a través de la consola.

3. Principios de POO Implementados

Herencia: Se estableció una relación jerárquica donde producto sirve como clase base, proporcionando atributos compartidos (nombre, precio, disponible), las clases platillo y bebida heredan de esta clase usando `super(). __init__()` y añaden atributos especializados (es_vegano y tamano_ml respectivamente).

Encapsulación: El atributo precio dentro de producto se definió como privado usando doble guion bajo (__precio), esto limita el acceso directo desde fuera de la clase; se implementaron métodos seguros de acceso (Getter/Setter) obtener_precio() y cambiar_precio(), incluyendo en el segundo una validación lógica que evita que un producto tenga un valor negativo o cero.

Polimorfismo: El polimorfismo se evidencia en el archivo servicios/restaurante. py. El método mostrar_productos() itera sobre una lista heterogénea que almacena objetos de tipo `Platillo` o `Bebida` indistintamente, al llamar a la función producto mostrar_informacion(), el intérprete de Python determina dinámicamente el tipo de objeto en tiempo de ejecución y lleva a cabo el método sobrescrito correspondiente al comportamiento específico.

4. Reflexión: La combinación de modularidad y la programación orientada a objetos en Python facilita la creación de software escalable, organizado y fácil de mantener, al diferenciar las entidades de datos (modelos) de los flujos lógicos (servicios), se consigue un código con bajo acoplamiento, si en el futuro el restaurante desea integrar una nueva categoría (como Postres), solo será necesario crear un nuevo archivo que herede de Producto, evitando cambios en la estructura actual de la aplicación y reduciendo el riesgo de errores en el código que está en producción.
