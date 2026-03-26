"""
Sistema de Inventario con menú interactivo
Permite agregar productos, visualizar inventario y calcular estadísticas
"""

# =========================
# VALIDACIONES
# =========================

def validate_string(message):
    while True:
        value = input(message)
        if value.replace(" ", "").isalpha():
            return value
        else:
            print("Error: Solo se permiten letras.")


def validate_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Error: Ingresa un número decimal válido.")


def validate_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Error: Ingresa un número entero válido.")


# =========================
# FUNCIONES PRINCIPALES
# =========================

def agregar_producto(inventario):
    """
    Permite agregar un producto al inventario
    """
    print("\n--- AGREGAR PRODUCTO ---")

    nombre = validate_string("Nombre del producto: ")
    precio = validate_float("Precio del producto: ")
    cantidad = validate_integer("Cantidad: ")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("✅ Producto agregado correctamente.")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos almacenados
    """
    print("\n--- INVENTARIO ---")

    if len(inventario) == 0:
        print("⚠️ El inventario está vacío.")
        return

    for producto in inventario:
        print(f"Producto: {producto['nombre']} | "
              f"Precio: {producto['precio']} | "
              f"Cantidad: {producto['cantidad']}")


def calcular_estadisticas(inventario):
    """
    Calcula estadísticas del inventario
    """
    print("\n--- ESTADÍSTICAS ---")

    if len(inventario) == 0:
        print("⚠️ No hay datos para calcular.")
        return

    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print(f"💰 Valor total del inventario: {valor_total}")
    print(f"📦 Cantidad total de productos: {total_productos}")


# =========================
# MENÚ PRINCIPAL
# =========================

def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE INVENTARIO")
    print("="*40)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")


def main():
    inventario = []
    control = True

    while control:

        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto(inventario)

        elif opcion == "2":
            mostrar_inventario(inventario)

        elif opcion == "3":
            calcular_estadisticas(inventario)

        elif opcion == "4":
            print("👋 Saliendo del sistema...")
            control = False

        else:
            print("❌ Opción inválida. Intente nuevamente.")


# =========================
# EJECUCIÓN
# =========================

if __name__ == "__main__":
    main()


"""
RESUMEN:
Este programa implementa un sistema de inventario interactivo usando:
- Listas y diccionarios para almacenar productos
- Validación de datos robusta
- Estructuras condicionales (if/elif/else)
- Bucles (while y for)
- Modularización mediante funciones

Permite agregar productos, visualizar el inventario y calcular estadísticas básicas.
"""