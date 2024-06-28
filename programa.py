from funciones import menu, agregar_producto, leer_inventario, clasificarexportar_productos

while True: 
    menu()
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        leer_inventario()
    elif opcion == 3:
        clasificarexportar_productos()
    elif opcion == 4:
        print("Hasta luego")
        break