"""
crear un diccionario que tenga dos registros de un alumo
1. crear un funcion que me imprima los registro,
2. crear una funcion que me ´permita editar uno de los campos del registro
"""
alumnos= {
    "nombre":"erick",
    "apellido":"huamani",
    "edad":20,
    "especialidad":"APSTI"
    
},
{
    "nombre":"willian",
    "apellido":"barrientos",
    "edad":19,
    "especialidad":"APSTI"
}
def mostrar_valores(alumnos):
    print("valores del alumno: ")
    valores=diccionario.values()
    for valor in valores:
        print(valor)
mostrar_valores(alumnos)
    