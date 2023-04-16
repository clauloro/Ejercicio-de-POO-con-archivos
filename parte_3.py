from todo_codigo import  leer_calificaciones, calcular_nota_final

def separar_aprobados_suspensos(lista_alumnos):
    aprobados = []
    suspensos = []

    for alumno in lista_alumnos:
        asistencia = int(alumno["Asistencia"].replace("%", ""))
        p1 = float(alumno["Parcial1"].replace(",", ".")) if alumno["Parcial1"] else 0
        p2 = float(alumno["Parcial2"].replace(",", ".")) if alumno["Parcial2"] else 0
        practicas = float(alumno["Practicas"].replace(",", ".")) if alumno["Practicas"] else 0
        nota_final = float(alumno["NotaFinal"])
        
        if asistencia >= 75 and p1 >= 4 and p2 >= 4 and practicas >= 4 and nota_final >= 5:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)

    return aprobados, suspensos

archivo = "calificaciones.csv"
lista_alumnos = leer_calificaciones(archivo)
calcular_nota_final(lista_alumnos)
aprobados, suspensos = separar_aprobados_suspensos(lista_alumnos)

print("Aprobados:")
for alumno in aprobados:
    print(alumno["Apellidos"], alumno["Nombre"], alumno["NotaFinal"])

print("\nSuspensos:")
for alumno in suspensos:
    print(alumno["Apellidos"], alumno["Nombre"], alumno["NotaFinal"])
    