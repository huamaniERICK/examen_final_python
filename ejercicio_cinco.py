"""
Crear una funcion que me me retorne un diccionario con los datos personales de un alumno
ejm:
entrada: ("jose","alvarez","30","APSTI","III")
salida: {nombre:"jose",apellido:"alvarez",edad:"30",programa_estudio:"APSTI",semestre:"III"}
"""
def datos_personales(nombre,apellido,edad,especialidad,periodo):
    alumno={
        "nombre":nombre,
        "apellido":apellido,
        "edad":edad,
        "especialidad":especialidad,
        "periodo":periodo

    }
    return alumno
alumno=datos_personales("erick","huamani",20,"APSTI","III")
print(alumno)

   