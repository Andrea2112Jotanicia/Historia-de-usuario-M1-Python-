from servicios import *
from archivos import *

# ================= VALIDACIONES =================

def validar_string(msg):
    while True:
        val = input(msg)
        if val.strip():
            return val
        print("Error: valor inválido")


def validar_float(msg):
    while True:
        try:
            val = float(input(msg))
            if val >= 0:
                return val
        except:
            pass
        print("Error: número inválido")


def validar_int(msg):
    while True:
        try:
            val = int(input(msg))
            if val >= 0:
                return val
        except:
            pass
        print("Error: número inválido")


# ================= MENÚ =================

def menu():
    print("\n--- INVENTARIO ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")


def main():
    inventario = []
    control = True

    while control:
        menu()
        op = input("Opción: ")

        if op == "1":
            nombre = validar_string("Nombre: ")
            precio = validar_float("Precio: ")
            cantidad = validar_int("Cantidad: ")
            agregar_producto(inventario, nombre, precio, cantidad)

        elif op == "2":
            mostrar_inventario(inventario)

        elif op == "3":
            nombre = validar_string("Buscar: ")
            p = buscar_producto(inventario, nombre)
            print(p if p else "No encontrado")

        elif op == "4":
            nombre = validar_string("Producto: ")
            precio = validar_float("Nuevo precio: ")
            cantidad = validar_int("Nueva cantidad: ")
            if actualizar_producto(inventario, nombre, precio, cantidad):
                print("Actualizado")
            else:
                print("No encontrado")

        elif op == "5":
            nombre = validar_string("Eliminar: ")
            if eliminar_producto(inventario, nombre):
                print("Eliminado")
            else:
                print("No encontrado")

        elif op == "6":
            stats = calcular_estadisticas(inventario)
            if stats:
                print(stats)
            else:
                print("Sin datos")

        elif op == "7":
            ruta = input("Ruta archivo: ")
            guardar_csv(inventario, ruta)

        elif op == "8":
            ruta = input("Ruta archivo: ")
            nuevos, errores = cargar_csv(ruta)

            if nuevos:
                decision = input("¿Sobrescribir inventario? (S/N): ").lower()

                if decision == "s":
                    inventario = nuevos
                    print("Inventario reemplazado")

                else:
                    # Fusión
                    for nuevo in nuevos:
                        existente = buscar_producto(inventario, nuevo["nombre"])
                        if existente:
                            existente["cantidad"] += nuevo["cantidad"]
                            existente["precio"] = nuevo["precio"]
                        else:
                            inventario.append(nuevo)

                    print("Inventario fusionado")

                print(f"Filas inválidas: {errores}")

        elif op == "9":
            control = False

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()