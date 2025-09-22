# Tarea: Trabajando con Diccionarios en Python

# 1. Crear un Diccionario
# Se crea un diccionario llamado informacion_personal con datos ficticios.
informacion_personal = {
    "nombre": "María López",
    "edad": 28,
    "ciudad": "Guaranda",
    "profesion": "Estudiante"
}

# 2. Acceder y Modificar Valores
# Se accede y se modifica el valor de la clave "ciudad".
print("Ciudad original:", informacion_personal["ciudad"])
informacion_personal["ciudad"] = "Cuenca"

# 3. Agrega una nueva clave-valor (en este caso, se actualiza la existente)
# Se actualiza el valor de la clave "profesion".
informacion_personal["profesion"] = "Docente de Matemáticas"

# 4. Verificar Existencia de Claves
# Se verifica si la clave "telefono" existe y, si no, se agrega.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593987654321"

# 5. Eliminar una Clave
# Se elimina la clave "edad" del diccionario.
informacion_personal.pop("edad", None)

# 6. Imprimir el Diccionario Final
# Se imprime el diccionario resultante después de todas las operaciones.
print("Diccionario final:")
print(informacion_personal)
