def agregar_producto(inventario, nombre, precio, stock, categoria):
    if nombre in inventario:
        return False
    inventario[nombre] = {
        "precio": precio,
        "stock": stock,
        "categoria": categoria,
    }
    return True


def vender_producto(inventario, nombre, cantidad):
    if nombre not in inventario:
        return False
    if cantidad <= 0 or inventario[nombre]["stock"] < cantidad:
        return False
    inventario[nombre]["stock"] -= cantidad
    return True


def reabastecer_producto(inventario, nombre, cantidad):
    if nombre not in inventario or cantidad <= 0:
        return False
    inventario[nombre]["stock"] += cantidad
    return True


def productos_con_bajo_stock(inventario, limite):
    if limite < 0:
        return []
    return [nombre for nombre, datos in sorted(inventario.items()) if datos["stock"] < limite]


def valor_total_inventario(inventario):
    total = 0.0
    # Recorremos cada producto y acumulamos su valor (precio * stock)
    for datos in inventario.values():
        precio = datos.get("precio", 0)
        stock = datos.get("stock", 0)
        total += precio * stock
    return total


def mostrar_inventario(inventario):
    if not inventario:
        print("No hay productos en el inventario.")
        return

    fila = "{:<15} | {:>8} | {:>5} | {:<12} | {:>12}"
    print("--- Inventario completo ---")
    print(fila.format("Producto", "Precio", "Stock", "Categoría", "Valor total"))
    print("-" * 64)
    # Recorremos el inventario ordenado por nombre de producto.
    # inventario.items() devuelve una vista de tuplas (clave, valor),
    # donde la clave es el nombre del producto y el valor es otro diccionario
    # con los datos del producto (precio, stock y categoría).
    # El for desestructura cada tupla en 'nombre' y 'datos'.
    for nombre, datos in sorted(inventario.items()):
        # 'datos' es un diccionario con las propiedades del producto.
        # Accedemos a precio y stock usando las claves correspondientes.
        valor = datos["precio"] * datos["stock"]
        print(fila.format(
            nombre,
            f"{datos['precio']:.2f}",
            datos["stock"],
            datos["categoria"],
            f"{valor:.2f}",
        ))


def solicitar_entero(texto):
    # Usamos try / except para intentar convertir la entrada a entero y manejar
    # el caso en que el usuario escriba algo que no se pueda convertir.
    # try ejecuta el código que puede generar un error; si ocurre ValueError,
    # except lo captura y evita que el programa se detenga, devolviendo None.
    try:
        valor = int(input(texto).strip())
        return valor
    except ValueError:
        return None


def solicitar_flotante(texto):
    try:
        valor = float(input(texto).strip())
        return valor
    except ValueError:
        return None


def menu():
    inventario = {}
    while True:
        print("--- Sistema de Inventario ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Reabastecer producto")
        print("4. Ver productos con bajo stock")
        print("5. Valor total del inventario")
        print("6. Mostrar inventario completo")
        print("7. Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            if not nombre:
                print("Nombre inválido.")
                continue

            precio = solicitar_flotante("Precio: ")
            if precio is None or precio < 0:
                print("Precio inválido.")
                continue

            stock = solicitar_entero("Stock: ")
            if stock is None or stock < 0:
                print("Stock inválido.")
                continue

            categoria = input("Categoría: ").strip()
            if not categoria:
                print("Categoría inválida.")
                continue

            if agregar_producto(inventario, nombre, precio, stock, categoria):
                print(f"Producto {nombre} agregado.")
            else:
                print(f"El producto {nombre} ya existe.")

        elif opcion == "2":
            nombre = input("Producto: ").strip()
            cantidad = solicitar_entero("Cantidad: ")
            if cantidad is None or cantidad <= 0:
                print("Cantidad inválida.")
                continue

            if nombre not in inventario:
                print("Producto no encontrado.")
                continue

            if vender_producto(inventario, nombre, cantidad):
                print(f"Venta exitosa. Stock restante: {inventario[nombre]['stock']}")
            else:
                print("No hay stock suficiente o cantidad inválida.")

        elif opcion == "3":
            nombre = input("Producto: ").strip()
            cantidad = solicitar_entero("Cantidad a reabastecer: ")
            if cantidad is None or cantidad <= 0:
                print("Cantidad inválida.")
                continue

            if reabastecer_producto(inventario, nombre, cantidad):
                print(f"Producto {nombre} reabastecido. Stock actual: {inventario[nombre]['stock']}")
            else:
                print("Producto no encontrado o cantidad inválida.")

        elif opcion == "4":
            limite = solicitar_entero("Límite de stock: ")
            if limite is None or limite < 0:
                print("Límite inválido.")
                continue

            bajos = productos_con_bajo_stock(inventario, limite)
            print("Productos con bajo stock:")
            if not bajos:
                print("Ninguno")
            else:
                for nombre in bajos:
                    print(f"- {nombre} (stock: {inventario[nombre]['stock']})")

        elif opcion == "5":
            total = valor_total_inventario(inventario)
            print(f"Valor total del inventario: {total:.2f}")

        elif opcion == "6":
            mostrar_inventario(inventario)

        elif opcion == "7":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

        print()


if __name__ == "__main__":
    menu()
