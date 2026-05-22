# ============================================================
# Sistema de inventario de productos electrónicos
# ============================================================
# Este programa permite consultar y administrar el stock de un
# conjunto de productos electrónicos mediante un menú interactivo.
#
# Funcionalidades principales:
# - Consultar el stock de un producto específico.
# - Mostrar el producto con mayor y menor cantidad disponible.
# - Calcular el stock total y el promedio de inventario.
# - Actualizar el stock de un producto, ya sea cambiándolo,
#   sumando unidades o restando unidades.
# - Generar un reporte de productos con bajo stock y con exceso
#   de inventario, ordenados según su cantidad.
#
# El programa trabaja con dos listas relacionadas:
# una para los nombres de los productos y otra para sus cantidades.
# ============================================================

def mayormenor(lista1,lista2,opcion):
    if opcion == "2":
        m = max(lista2)
        index = indice(lista2,m)
        print("El producto con mayor stock es:",lista1[index],"(",m,")")
    elif opcion == "3":
        m = min(lista2)
        index = indice(lista2,m)
        print("El producto con menor stock es:",lista1[index],"(",m,")")
    else:
        pass
    
def indice(lista,objeto):
    index = lista.index(objeto)
    return(index)
    
def reporte(lista1,lista2):
    i = 0
    reabastecimiento = []
    exceso = []

    for x in lista2:
        if x < 5:
            reabastecimiento.append((x,lista1[i]))
            
        elif x > 50:
            exceso.append((x,lista1[i]))

        i += 1

    reabastecimiento.sort()
    exceso.sort()

    print("Reabastecimiento urgente (stock < 5) de: ")
    for x, producto in reabastecimiento:
        print(producto,"(stock:",x,")")

    print("Exceso de inventario (stock > 50) de: ")
    for x, producto in exceso:
        print(producto,"(stock:",x,")")

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Parlantes", "Cargador", "Webcam", "USB"]
cantidad = [12,3,8,2,60,4,55,25]
opcion = "7"
menu = """
1)Ver stock de algun producto.
2)Producto con mayor stock.
3)Producto con menor stock.
4)Stock total de todos los productos.
5)Promedio de stock.
6)Actualizar stock de algun producto.
7)Ver menu.
8)Ver reporte de inventario.
9)Salir
"""

print("Bienvenidos al sistema de busquedas de dispositivos electronicos")
print(menu)
while opcion != "9":
    opcion = input("Ingrese la opcion que desea utilizar osea un valor numerico entre 1 y 9: ")
    print("")
    if opcion == "1":
        while True:
            print("Observe los productos: ")
            for x in productos:
                print(x)
            producto = input("Ingrese el producto al que le quiere ver stock: ")
            if producto in productos:
                numero = indice(productos,producto)
                print("El stock del",producto,"es:",cantidad[numero])
                break
            else:
                print("Ingrese un nombre de los mostrados.")
                print("")
                print("")
    
    elif opcion == "2":
        mayormenor(productos,cantidad,opcion)
        
    elif opcion == "3":
        mayormenor(productos,cantidad,opcion)
        
    elif opcion == "4":
        total = sum(cantidad)
        print("El stock total de todos los productos es:",total)
        
    elif opcion == "5":
        promedio = sum(cantidad)/len(cantidad)
        print("El promedio del stock es de: ", promedio)
        
    elif opcion == "6":
        while True:
            cambio = input("Desea cambiar (c), sumar (s) o restar (r) al stock: ")
            if cambio == "c" or cambio == "C":
                while True:
                    print("Observe los productos: ")
                    for x in productos:
                        print(x)
                    producto = input("Ingrese el nombre del producto al que le desea cambiar el stock: ")
                    if producto in productos:
                        numero = indice(productos,producto)
                        break
                    else: 
                        print("Ingrese un nombre de los mostrados.")
                while True:
                    stock = int(input("Ingrese el stock del producto: "))
                    if stock >= 0:
                        cantidad[numero] = stock
                        break
                    else: 
                        print("Ingrese un stock congruente (no negativo ni caracteres distintos).")
                break
                
            
            elif cambio == "s" or cambio == "S":
                while True:
                    print("Observe los productos: ")
                    for x in productos:
                        print(x)
                    producto = input("Ingrese el nombre del producto al que le desea cambiar el stock: ")
                    if producto in productos:
                        numero = indice(productos,producto)
                        break
                    else: 
                        print("Ingrese un nombre de los mostrados.")
                        
                while True:
                    stock = int(input("Ingrese el stock del producto que desea restar: "))
                    if cantidad[numero] + stock >= 0:
                        cantidad[numero] = cantidad[numero] + stock
                        break
                    elif cantidad[numero] + stock < 0:
                        print("Ingrese un stock que no lo vuelva negativo.")
                    
                    else: 
                        print("Ingrese un stock congruente.")
                    
                break
            
            elif cambio == "r" or cambio == "R":
                while True:
                    print("Observe los productos: ")
                    for x in productos:
                        print(x)
                    producto = input("Ingrese el nombre del producto al que le desea cambiar el stock: ")
                    if producto in productos:
                        numero = indice(productos,producto)
                        break
                    else: 
                        print("Ingrese un nombre de los mostrados.")
                        
                while True:
                    stock = int(input("Ingrese el stock del producto que desea restar: "))
                    if cantidad[numero] - stock >= 0:
                        cantidad[numero] = cantidad[numero] - stock
                        break
                    elif cantidad[numero] - stock < 0:
                        print("Ingrese un stock que no lo vuelva negativo.")
                    
                    else: 
                        print("Ingrese un stock congruente.")
                    
                break        
            else:
                print("Ingrese una opcion adecuada (c,s o r).")
        
    elif opcion == "7":
        print(menu)
        
    elif opcion == "8":
        print("--Reporte de inventario--")
        reporte(productos,cantidad)
    
    elif opcion == "9":
        print("Saliendo del sistema...")
        break
    else: 
        print("Ingrese una opcion valida entre 1 y 9.")
    print("")    
    print("Si desea ver nuevamente el menu ingrese la opcion 7.")