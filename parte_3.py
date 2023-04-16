from parte_1 import calcular_notas, calificaciones


def separar_alumnos(lista_alumnos_con_notas):
    aprobados = []
    suspensos = []
    for alumno in lista_alumnos_con_notas:
        if float(alumno['Asistencia'].replace(',', '.').replace('%', '')) / 100 >= 0.75 and float(alumno['Parcial1'].replace(',', '.')) >= 4 and float(alumno['Parcial2'].replace(',', '.')) >= 4 and float(alumno['NotaFinal']) >= 5:
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos
