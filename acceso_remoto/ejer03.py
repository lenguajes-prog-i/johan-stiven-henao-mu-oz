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

mis_autos = [objeto_auto1, objeto_auto2, objeto_auto3, objeto_auto4, objeto_auto5]



for miauto in mis_autos:
    archivo_auto = open("autos.txt", "wb")
    pickle.dump(mis_autos, archivo_auto)
    archivo_auto.close()

archivo_auto = open("autos.txt", "rb")
autos = pickle.load(archivo_auto)
archivo_auto.close()

print(autos)