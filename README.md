<em>Ejercicio-de-POO-con-archivos</em>
# Datos

    Calificaciones de un curso

    Contribuidores: Martina García, Enrique Pardo, Claudia López.

##Índice







### Ejercicio de procesamiento de datos en Python

    •En este ejercicio se solicita la creación de varias funciones que procesan datos de un fichero CSV que contiene las calificaciones de un curso. 
     Los requisitos de las funciones son los siguientes:
 
        •La primera función debe leer el fichero de calificaciones y devolver una lista de diccionarios con la información de los exámenes y la asistencia de cada alumno, ordenados por apellidos.

        •La segunda función debe recibir la lista de diccionarios anterior y añadir a cada diccionario un nuevo par con la nota final del curso. El peso de cada parcial de teoría en la nota final es del 30%, mientras que el peso del examen de prácticas es del 40%.

        •La tercera función debe recibir la lista de diccionarios actualizada con las notas finales y devolver dos listas, una con los alumnos aprobados y otra con los alumnos suspensos. Para aprobar el curso, la asistencia tiene que ser mayor o igual que el 75%, la nota de los exámenes parciales y de prácticas mayor o igual que 4, y la nota final mayor o igual que 5.

### Solución

    Para resolver este ejercicio, se puede utilizar la librería csv de Python para leer el fichero CSV y crear una lista de diccionarios con la información de cada alumno. 
    Luego, se pueden utilizar estructuras de control y operaciones aritméticas para calcular las notas finales y separar a los alumnos aprobados de los suspensos.

    A continuación, se presentan las soluciones a cada uno de los requisitos del ejercicio.
