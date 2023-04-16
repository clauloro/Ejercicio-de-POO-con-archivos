import csv 
def calificaciones():
    with open ("calificaciones.csv","r") as archivo:
        lista_alumnos=[]
        reader=csv.DictReader(archivo,delimiter=";")
        next(reader)
        for row in reader:
                lista_alumnos.append(row)
        lista_alumnos.sort(key=lambda x: x["Apellidos"])
        return lista_alumnos

calificaciones_alumnos=calificaciones()
for alumno in calificaciones_alumnos:
    print(alumno)