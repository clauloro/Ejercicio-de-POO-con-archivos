import csv 
import pandas as pd

def leer_calificaciones(ruta_archivo):
    df = pd.read_csv(ruta_archivo)
    df = df.sort_values(by=['apellidos'])
    lista_alumnos = []
    for i in range(len(df)):
        alumno = {}
        alumno['apellidos'] = df['apellidos'][i]
        alumno['nombre'] = df['nombre'][i]
        alumno['asistencia'] = df['asistencia'][i]
        alumno['parcial1'] = df['parcial1'][i]
        alumno['parcial2'] = df['parcial2'][i]
        alumno['practicas'] = df['practicas'][i]
        if df['parcial1'][i] < 4:
            alumno['parcial1_rec'] = df['parcial1_rec'][i]
        if df['parcial2'][i] < 4:
            alumno['parcial2_rec'] = df['parcial2_rec'][i]
        lista_alumnos.append(alumno)
    return lista_alumnos



def calcular_nota_final(lista_alumnos):
    for alumno in lista_alumnos:
        nota_final = 0.3 * (alumno['parcial1'] + alumno['parcial2']) / 2 + 0.4 * alumno['practicas']
        alumno['nota_final'] = nota_final
    return lista_alumnos


def separar_aprobados_suspensos(lista_alumnos):
    aprobados = []
    suspensos = []
    for alumno in lista_alumnos:
        if (alumno['asistencia'] >= 0.75 and 
            alumno['parcial1'] >= 4 and 
            alumno['parcial2'] >= 4 and 
            alumno['practicas'] >= 4 and 
            alumno['nota_final'] >= 5):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)
    return aprobados, suspensos
