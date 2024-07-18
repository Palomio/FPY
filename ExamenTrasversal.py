import random
import csv
trabajadores = ["Juan Pérez", "Maria Garcia", "Carlos López", "Ana Martinez", "Pedro Rodriguez", "Laura Hemández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def menuPrincipal():
    print("")
    print("1.- Asignar sueldo Aleatorio")
    print("2.- Clasificar sueldo")
    print("3.- Ver estadisticas")
    print("4.- Reportar sueldo")
    print("5.- Salir del programa")
    print("")

def sueldoleatorio(trabajadores):
    porcentaje_salud = 0.07  # 7%
    porcentaje_afp = 0.12    # 12%

    nueva_lista_empleados = []

    for empleado in trabajadores:
        # Generar saldo bruto aleatorio entre 300000 y 2500000 en pasos de 50000
        saldo_bruto = random.randrange(300000, 2500000 + 1, 50000)
        
        # Calcular descuentos
        descuento_salud = saldo_bruto * porcentaje_salud
        descuento_afp = saldo_bruto * porcentaje_afp
        
        # Calcular sueldo líquido
        sueldo_liquido = saldo_bruto - descuento_salud - descuento_afp
        
        # Crear lista con los datos del empleado
        empleado_datos = [empleado, saldo_bruto, descuento_salud, descuento_afp, sueldo_liquido]
        
        # Agregar a la nueva lista de empleados
        nueva_lista_empleados.append(empleado_datos)
    
    # Agregar nueva_lista_empleados a lista_empleados global
    global lista_empleados
    lista_empleados.extend(nueva_lista_empleados)

    # Imprimir la nueva lista de empleados
    print("Nombre Empleado | Saldo Bruto")
    print("-" * 80)
    for empleado_datos in nueva_lista_empleados:
        print(f"{empleado_datos[0]:<15} | {empleado_datos[1]:<11}")

def clasificarSueldo(lista_empleados):
    if not lista_empleados:
        print("La lista de empleados está vacía.")
        return
    
    # Inicializar contadores y listas para clasificación
    sueldos_menores_800k = []
    sueldos_entre_800k_y_2m = []
    sueldos_superiores_2m = []
    total_sueldos = 0

    # Clasificar los sueldos según las categorías
    for empleado in lista_empleados:
        nombre_empleado = empleado[0]
        sueldo = empleado[1]

        if sueldo < 800000:
            sueldos_menores_800k.append((nombre_empleado, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            sueldos_entre_800k_y_2m.append((nombre_empleado, sueldo))
        elif sueldo > 2000000:
            sueldos_superiores_2m.append((nombre_empleado, sueldo))
        
        total_sueldos += sueldo
    
    # Imprimir resultados
    print(f"Sueldos menores a $800.000 TOTAL: {len(sueldos_menores_800k)}")
    print("Nombre empleado | Sueldo")
    print("-" * 80)
    for nombre, sueldo in sueldos_menores_800k:
        print(f"{nombre:<15} | ${sueldo:,.0f}")

    print("")
    print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(sueldos_entre_800k_y_2m)}")
    print("Nombre empleado | Sueldo")
    print("-" * 80)
    for nombre, sueldo in sueldos_entre_800k_y_2m:
        print(f"{nombre:<15} | ${sueldo:,.0f}")

    print("")
    print(f"Sueldos superiores a $2.000.000 TOTAL: {len(sueldos_superiores_2m)}")
    print("Nombre empleado | Sueldo")
    print("-" * 80)
    for nombre, sueldo in sueldos_superiores_2m:
        print(f"{nombre:<15} | ${sueldo:,.0f}")

    print("")
    print(f"TOTAL SUELDOS: ${total_sueldos:,.0f}")

def verEstadisticas(lista_empleados):
    if not lista_empleados:
        print("La lista de empleados está vacía.")
        return
    
    # Inicializar variables para los sueldos
    sueldos = [empleado[4] for empleado in lista_empleados]
    sueldo_mas_alto = max(sueldos)
    sueldo_mas_bajo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(lista_empleados)

    # Imprimir resultados
    print(f"Sueldo más alto: {sueldo_mas_alto}")
    print(f"Sueldo más bajo: {sueldo_mas_bajo}")
    print(f"Promedio de sueldos: {promedio_sueldos}")

def reportarSueldos(lista_empleados):

    
    print("Nombre Empleado | Saldo Bruto | Descuento Salud | Descuanto AFP | Sueldo Liquido")
    print("-" * 80)
    for empleado in lista_empleados:
        print(f"{empleado[0]:<15} | {empleado[1]:<12}| {empleado[2]:<12}| {empleado[3]:<12}| {empleado[4]:<14} ")

    with open("sueldosEmpresa.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Empleado", "Saldo Bruto", "Descuento Salud", "Descuento AFP", "Sueldo Liquido"])
        writer.writerows(lista_empleados)


# Lista global para almacenar empleados
lista_empleados = []

while True:
    menuPrincipal()
    opcion = int(input("Ingrese la opción que desea: "))
    
    if opcion == 1:
        sueldoleatorio(trabajadores)
    elif opcion == 2:
        clasificarSueldo(lista_empleados)
    elif opcion == 3:
        verEstadisticas(lista_empleados)
    elif opcion == 4:
        reportarSueldos(lista_empleados)
    elif opcion == 5:
        print("Saliendo del programa")
        break
