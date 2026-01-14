##Menú de analista de control de gastos
import json

def agregar_gasto(lista_de_gasto):
    print("NUEVO GASTO")
    nombre = input("Qué compraste? ").upper()
    monto = float(input("Cuánto costó? "))
        
    nuevo_gasto = {
        "concepto": nombre,
        "precio": monto
    }    
    lista_de_gasto.append(nuevo_gasto)    
    print("Gasto guardado con exito")
    
    
def ver_gasto(lista_de_gasto):
    print("TUS GASTOS")
    if len(lista_de_gasto) == 0:
        print("No tienes gastos registrados todavia")
        return
    for g in lista_de_gasto:
        print(f"Gasto: {g['concepto']} | Costo: {g['precio']}")
        print("---------------------------")
        
def totalizar_gastos(lista_de_gastos):
    total = 0
    for recibo in lista_de_gastos:
        if recibo['precio'] > 50:
            total += recibo['precio']
    print(f"Total gastado: {total}")

def buscar_gasto(lista_de_gastos):
    nombre_buscado = input("Qué gasto buscas? ").upper()
    encontrado = False
    for recibo in lista_de_gastos:
        if recibo['concepto'] == nombre_buscado:
            print(f"Gasto encontrado: ")
            print(f"Gasto: {recibo['concepto']} | Costo: {recibo['precio']}")
            encontrado = True
            break
    if encontrado == False:
        print("Dato no encontrado o inexistente")

def eliminar_gasto(lista_de_gastos):
    nombre_buscado = input("Qué gasto buscas? ").upper()
    encontrado = False
    for recibo in lista_de_gastos:
        if recibo['concepto'] == nombre_buscado:
            print(f"Gasto encontrado: ")
            print(f"Gasto: {recibo['concepto']} | Costo: {recibo['precio']}")
            lista_de_gastos.remove(recibo)
            print("Gasto eliminado correctamente")
            encontrado = True
            break
    if encontrado == False:
        print("Dato no encontrado o inexistente")          
        
def guardar_datos(lista_de_gastos):
    with open("base_datos.json", "w")as archivo:
        json.dump(lista_de_gastos, archivo) #Traduce a texto JSON y los mete a un archivo
    print("Datos guardados correctamente")
    
def cargar_datos():
    try:
        # Intentamos abrir el archivo en modo "r" (read/leer)
        with open("base_datos.json", "r") as archivo:
            # 1. Usa json.load(archivo) y guarda el resultado en una variable llamada 'datos'
            # TU CÓDIGO AQUÍ:
            datos = json.load(archivo)
            
            print("¡Datos cargados correctamente!")
            # 2. Retorna esa variable 'datos' para que el programa la use
            # TU CÓDIGO AQUÍ:
            return datos
            
    except FileNotFoundError:
        print("No se encontró archivo. Iniciando desde cero.")
        # 3. Si falló porque no existe, retorna una lista vacía []
        # TU CÓDIGO AQUÍ:  
        return []
    
gastos = cargar_datos()
    
while True:
    print("""
          MENÚ DE CONTROL DE GASTOS
          1. AGREGAR GASTOS
          2. VER GASTOS
          3. BUSCAR GASTO
          4. ELIMINAR GASTO
          5. GUARDAR GASTO
          6. SALIR DEL PROGRAMA
          """)
    menu=int(input("Ingresa tu opción: "))
    if menu == 1:
         agregar_gasto(gastos)     
    elif menu == 2:
        ver_gasto(gastos)
        totalizar_gastos(gastos)
    elif menu == 3:
        buscar_gasto(gastos) 
    elif menu == 4:
        eliminar_gasto(gastos)
    elif menu == 5:
        guardar_datos(gastos)
    elif menu == 6:
        print("Saliendo...")
        break
    else:
        print("Seleccione una opción valida (1, 2, 3, 4)")
        
