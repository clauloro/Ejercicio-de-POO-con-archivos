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


def main():
    calificaciones_alumnos = calificaciones()
    lista_alumnos_con_notas = calcular_notas(calificaciones_alumnos)
    aprobados, suspensos = separar_alumnos(lista_alumnos_con_notas)
    print('La lista de alumnos aprobados es: \n')
    print(aprobados)
    print('==================================================')
    print('La lista de alumnos suspensos es: \n')
    print(suspensos)

main()
