from parte1 import *
def calcular_notas(calificaciones_alumnos):
    for alumno in calificaciones_alumnos:
    #calculamos la media dos parciales
     nota_parciales=((float(alumno["Parcial1"])+float(alumno["Parcial2"]))/2)*0.3
    #calculamos la nota de las practicas
    if alumno["Practicas"]==" " or float(alumno["Practicas"])<5:
        nota_practicas=float(alumno["OrdinarioPracticas"])*0.4
    else:
        nota_practicas=float(alumno["Practicas"])*0.4
    #calculamos la nota final
    nota_final=nota_parciales+nota_practicas
    alumno["NotaFinal"]=round(nota_final,2)
    return calificaciones_alumnos

print(calificaciones_alumnos)