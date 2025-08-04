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
def recorrer_cursos(id):
    if id in estudiante:
        cursos=estudiante[id]["cursos"]
        print("---CURSOS DE ESTUDIATE---")
        for curso in cursos:
            print(f"Curso:{curso} Nota: {cursos[curso]}")

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
        recorrer_cursos(id)

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
    for clave,dato in estudiante.items():
        print("---Estudiante---")
        print(f"Nombre:{dato["nombre"]}")
        print(f"Carrera:{dato["carrera"]}")
        print("---CURSOS DE ESTUDIATE---")
        recorrer_cursos(id)


#Programa principal
while True:
    menu_principal()
    opcion= input("Ingrese una ocpion:")
    match opcion:
        case "1":
            agregar_estudiante()
        case "2":
            agregar_curso()
        case "3":
            consultar_estudiante()
        case "4":
            promedio()
        case "5":
            verificar_aprobar()
        case "6":
            mostrar_estudiantes()
        case "7":
            print("Saliendo del programa...")
            break
        case _:
            print("Opcion no valida...")