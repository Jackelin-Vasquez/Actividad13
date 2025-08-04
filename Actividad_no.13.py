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
#Función agregar curso y nota
def agregar_curso():
    id=input("Ingrese ID de estudiante:")
    nombre_curso=input("Ingrese nombre de curso a agregar:")
    nota= float(input("Ingrese nota de curso:"))
    estudiante[id]["cursos"][nombre_curso]=nota   #Se agrega curso y nota en diccionario de cursos :)

#Función Consultar Estudiante
def consultar_estudiante():
    id=input("Ingrese estudiante a consultar:")
    if id in estudiante:
        dato=estudiante[id]
        print(f"Nombre:{dato["nombre"]}\nCarrera:{dato["carrera"]}")
        for clave,dato in estudiante.items():
            print(f"Cursos:{dato["cursos"]}")

#Función calcular promedio
def promedio():
    if id in estudiante: #Busca id en diccionario estudiantes
        dato = estudiante[id]
        curso= dato["cursos"]
        if len(curso) == 0: #Cuenta cantidad de cursos en diccionario
            print("El estudiante no tiene cursos...")
        else:
            suma= 0
            for nota in curso.values():
                suma += nota
            promedio = suma/ len(curso)
            return promedio
    else:
        print("Estudiante no encontrado...")
#Función que verifica si estudiante aprueba:
def verificar_aprobar():
    id= input("Ingrese id de estudiante para verificar si aprobo:")
    if id in estudiante:
        dato= estudiante[id]
        curso= dato["cursos"]
        for nota in curso.values():
            if nota < 61:
                print(f"{dato["nombra"]} no aprobado...")
            else:
                print(f"{dato["nombre"]} aprobado...")
    else:
        print("Estudiante no encontrado...")

#función mostrar estudiantes
def mostrar_estudiantes():
    for clave,valor in estudiante.items():
        print("---Estudiante---")
        print(f"Nombre:{valor["nombre"]}")
        print(f"Carrera:{valor["carrera"]}")
        print("---CURSOS DE ESTUDIATE---")
        for curso_name,nota in valor["cursos"].items():
            print(f"Curso:{curso_name}: {nota}")


agregar_estudiante()
agregar_curso()
consultar_estudiante()
promedio()
verificar_aprobar()
mostrar_estudiantes()

