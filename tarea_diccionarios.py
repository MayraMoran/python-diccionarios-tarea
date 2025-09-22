# Tarea: Trabajando con Diccionarios en Python

# 1. Crear un diccionario con información personal ficticia
informacion_personal = {
    "nombre": "María López",     # Nombre ficticio
    "edad": 28,                  # Edad ficticia (se eliminará más adelante)
    "ciudad": "Guaranda",        # Ciudad inicial
    "profesion": "Estudiante"    # Profesión inicial
}

# 2. Acceder al valor asociado con la clave "ciudad"
print("Ciudad original:", informacion_personal["ciudad"])

# Modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Cuenca"
print("Ciudad modificada a:", informacion_personal["ciudad"])

# 3. Agregar o actualizar la clave "profesion"
informacion_personal["profesion"] = "Docente de Matemáticas"
print("Profesión establecida en:", informacion_personal["profesion"])

# 4. Verificar si existe la clave "telefono"
# Si no existe, se agrega con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "+593987654321"
    print('Clave "telefono" no existía: se añadió el número ficticio.')
else:
    print('Clave "telefono" ya existe con valor:', informacion_personal["telefono"])

# 5. Eliminar la clave "edad" porque no es necesaria
if "edad" in informacion_personal:
    informacion_personal.pop("edad")
    print('Clave "edad" eliminada.')
else:
    print('La clave "edad" no existe; nada que eliminar.')

# 6. Imprimir el diccionario final con los cambios
print("\nDiccionario final:")
print(informacion_personal)
