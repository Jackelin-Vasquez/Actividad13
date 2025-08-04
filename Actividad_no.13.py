estudiante={}

#SISTEMA DE GESTIÓN ACADEMICA
def menu_principal():
    print("---MENÚ---")
    print("1.Agregar estudiante.\n2.Agregar curso con nota.\n3.Consultar Estudiante.")
    print("4.Calcular promedio de estudiante\n5.Verificar si aprueba.\n6.Mostrar todos los estudiantes.\nSalir del programa")

#Función para agregar estudiante
def agregar_estudiante():
    id=input("Ingrese ID de estudiante:")
    nombre=input("Ingrese nombre de estudiante:")
    carrera=input("Ingrese carrera o programa academico:")

    estudiante[id]={
        "nombre":nombre,
        "carrera":carrera,
        "cursos":{}
    }