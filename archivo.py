datos="""yo cree el archivo y tendra lindo texto
cd d:\ se ocupa para cambiar la ruta
"""

# w escritura
# r lectura
# r+ lectura/escritura

with open('texto.txt', 'w') as archivo:
    archivo.write(datos)

# opcion leer

archivo=open('texto.txt','r')
contenido=archivo.read()
print(contenido)
archivo.close


# opcion 2 leer aprender esta opcion

with open('texto.txt', 'r') as archivo:
    contenido=archivo.read()
print(contenido)