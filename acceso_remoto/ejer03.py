import pickle

class Auto:
    def __init__(self, modelo, placa):
        self.modelo = modelo
        self.placa = placa

    def __repr__(self):
        return f"El auto {self.modelo} tiene placa {self.placa}"
    
objeto_auto1 = Auto("Mazda", "HUB83H")
objeto_auto2 = Auto("TOYOTA", "HUB84H")
objeto_auto3 = Auto("FERRARI", "HUB85H")
objeto_auto4 = Auto("LAMBO", "HUB86H")
objeto_auto5 = Auto("CADILA", "HUB88H")


archivo_auto = open("autos.txt", "wb")
pickle.dump(objeto_auto1, archivo_auto)
pickle.dump(objeto_auto2, archivo_auto)
pickle.dump(objeto_auto3, archivo_auto)
pickle.dump(objeto_auto4, archivo_auto)
pickle.dump(objeto_auto5, archivo_auto)
archivo_auto.close()

archivo_auto = open("autos.txt", "rb")
autos = pickle.load(archivo_auto)
archivo_auto.close()

print(autos)