import json
datos={
    "nombre":"esteban",
    "edad":25,
    "comuna":"santiago",
    "estudios":["colegio Arturo Prat","liceo el bosques",
                "DuocUc","Diplomados DuocUC","Cato"]
}
with open ('archicojson','w')as archivo:
    json.dump(datos,archivo)
with open ('archicojson','r')as archivo:
    leer=json.load(archivo)
    print(leer)
