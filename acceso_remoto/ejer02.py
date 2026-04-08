import pickle

datos = {
    "nombre": "Johan Stiven Henao Muñoz",
    "materia": "programacion 1",
    "notas": [5.0, 5.0, 5.0]
}

with open("data.txt", "wb") as archivo:
    pickle.dump(datos, archivo)


with open("data.txt", "rb") as archivo:
    datos_estudiantes = pickle.load(archivo)

print(datos_estudiantes)
