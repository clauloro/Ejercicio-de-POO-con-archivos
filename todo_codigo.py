import csv

def leer_calificaciones(archivo):
    lista_alumnos = []
    with open(archivo, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';', fieldnames=["Apellidos", "Nombre", "Asistencia", "Parcial1", "Parcial2", "Ordinario1", "Ordinario2", "Practicas", "OrdinarioPracticas"])
        for row in reader:
            lista_alumnos.append(row)
    lista_alumnos.sort(key=lambda x: x["Apellidos"])
    return lista_alumnos

def calcular_nota_final(lista_alumnos):
    for alumno in lista_alumnos:
        p1 = float(alumno["Parcial1"].replace(",", ".")) if alumno["Parcial1"] else 0
        p2 = float(alumno["Parcial2"].replace(",", ".")) if alumno["Parcial2"] else 0
        o1 = float(alumno["Ordinario1"].replace(",", ".")) if alumno["Ordinario1"] else 0
        o2 = float(alumno["Ordinario2"].replace(",", ".")) if alumno["Ordinario2"] else 0
        practicas = float(alumno["Practicas"].replace(",", ".")) if alumno["Practicas"] else 0
        ordinario_practicas = float(alumno["OrdinarioPracticas"].replace(",", ".")) if alumno["OrdinarioPracticas"] else 0
        
        p1 = max(p1, o1)
        p2 = max(p2, o2)
        practicas = max(practicas, ordinario_practicas)

        nota_final = p1 * 0.3 + p2 * 0.3 + practicas * 0.4
        alumno["NotaFinal"] = round(nota_final, 2)

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
