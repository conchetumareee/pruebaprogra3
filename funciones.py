import csv

def menu(): # Se define la funcion Menu
    print("\nInventario Empresa")
    print("1. Agregar producto")
    print("2. Leer inventario")
    print("3. Clasificar productos y exportar productos")
    print("4. Salir") 


def agregar_producto(): # Se define la funcion Agregar producto
    print("\nAgregar producto")
    id = input("Ingrese el ID del producto: ") # Se pide al usuario ingresar el ID del producto
    nombre = input("Ingrese el nombre del producto: ") # Se pide al usuario ingresar el nombre del producto
    categoria = input("Categorias:\n 1. Electronica\n 2. Textil\n 3. Calzado\nIngresa la categoria del producto: ") #Se pide al usuario ingresar la categoria del producto
    if categoria == "1":
        categoria = "Electronica"
    elif categoria == "2":
        categoria = "Textil"
    elif categoria == "3":
        categoria = "Calzado" # Se asigna la categoria segun la eleccion del usuario
    precio = float(input("Ingrese el precio del producto: ")) # Se pide al usuario ingresar el precio del producto
    print(f"El producto {nombre}, Categoria: {categoria}, Precio: {precio}, con ID: {id} ha sido agregado con éxito.\n") # Se imprime un mensaje de confirmacion
    with open('inventario.csv', 'a', newline='') as inventario:
        escritor = csv.writer(inventario)
        escritor.writerow([id, nombre, categoria, precio]) # Se escribe en el archivo inventario.csv los datos ingresados por el usuario

def leer_inventario(): # Se define la funcion Leer inventario
    print("\nInventario de Productos")
    with open('inventario.csv', 'r', newline='') as inventario: # Se abre el archivo inventario.csv en modo lectura
        leer_archivo = csv.reader(inventario)
        print("ID  Nombre  Categoria  Precio") # Se imprime la cabecera de la tabla
        for row in leer_archivo:
            id, nombre, categoria, precio = row
            print(f"{id}  {nombre}  {categoria}  ${precio}") # Se imprime cada fila del archivo inventario.csv

def clasificarexportar_productos(): # Se define la funcion Clasificar y Exportar Productos
    print("\nClasificar y Exportar Productos") 
    categorias = {
        "Electronica": [],
        "Textil": [],
        "Calzado": []
    } # Se crea un diccionario con las categorias de productos
    with open('inventario.csv', 'r', newline='') as inventario: # Se abre el archivo inventario.csv en modo lectura
        leer_archivo = csv.reader(inventario)
        for row in leer_archivo:
            id, nombre, categoria, precio = row # Se leen los datos de cada fila del archivo inventario.csv
            categorias[categoria].append((id, nombre, precio)) # Se clasifican los productos segun su categoria
    
    with open('clasificacion_productos.txt', 'w') as archivo: # Se crea el archivo clasificacion_productos.txt en modo escritura
        for categoria, productos in categorias.items(): 
            archivo.write(f"{categoria}:\n")
            for producto in productos: # Se escribe en el archivo clasificacion_productos.txt los productos clasificados
                id, nombre, precio = producto
                archivo.write(f"ID: {id}, Nombre: {nombre}, Precio: {precio}\n") 
            archivo.write("\n") # Se agrega un salto de linea entre cada categoria de productos
    
    print("Los productos han sido clasificados y exportados exitosamente en el archivo clasificacion_productos.txt.\n") # Se imprime un mensaje de confirmacion