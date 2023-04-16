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




def calcular_notas(alumnos):
    for alumno in alumnos:
        # Calcular nota final de teoría como el promedio de los dos parciales ponderado al 30%
        nota_teorica = ((float(alumno['Parcial1'].replace(',', '.')) + float(alumno['Parcial2'].replace(',', '.'))) / 2) * 0.3

        
        # Calcular nota final de prácticas tomando la nota de ordinario si no hay nota de prácticas o si es suspendida
        if alumno['Practicas'] == '' or float(alumno['Practicas'].replace(',', '.')) < 5:
            if alumno['OrdinarioPracticas'] == '':
                nota_practicas = 0  # o el valor que quieras asignar
            else:
                nota_practicas = float(alumno['OrdinarioPracticas'].replace(',', '.'))
        else:
            nota_practicas = float(alumno['Practicas'].replace(',', '.')) * 0.4

        
        # Calcular nota final como la suma de la nota final de teoría y prácticas
        nota_final = nota_teorica + nota_practicas
        
        # Añadir la nota final al diccionario del alumno
        alumno['NotaFinal'] = round(nota_final, 2)
    
    return alumnos

def main():
    calificaciones_alumnos=calificaciones()
    lista_alumnos = calificaciones()
    lista_alumnos_con_notas = calcular_notas(lista_alumnos)

    for alumno in lista_alumnos:
        print(alumno)


main()
