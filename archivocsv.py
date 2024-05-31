import csv
with open('archivocsv.csv','w', newline='') as archivo:
    escritor=csv.writer(archivo)
    # Comentar esta fila si se ocupan [0],[1],[2]
    escritor.writerow(['Nombre','Edad','Comuna'])
    escritor.writerows([
        ['Esteban',25,'Santiago'],
        ['María',30,'Valapaíso'],
        ['Carlos',17,'Osorno'],
        ['Sigrid',25,'Santiago'],
        ['Daniela',30,'La Cisterna'],
        ['Aylen',10,'La Florida']
    ])
# encoding=utf-8 lectura de alfabeto español latino
with open('archivocsv.csv','r', newline='') as archivo:
    lector=csv.reader(archivo)
    for fila in lector:
        print(fila)

# OJO aca chicos

# with open('archivocsv.csv','r')as archivo:
#     lector=csv.reader(archivo)
    
#     for fila in lector:
#         nombre=fila[0]
#         edad=int(fila[1])
#         comuna=fila[2]
#         estado_edad="Mayot de edad" if edad>= 18 else "Menor edad"
#         print(f"{nombre} tiene {edad} año, es {estado_edad} y vive en {comuna}")

with open('archivocsv.csv','r')as archivo:
    lector=csv.DictReader(archivo)
    for fila in lector:
        nombre=fila['Nombre']
        edad=int(fila['Edad'])
        comuna=fila['Comuna']
        estado_edad="Mayot de edad" if edad>= 18 else "Menor edad"
        print(f"{nombre} tiene {edad} año, es {estado_edad} y vive en {comuna}")