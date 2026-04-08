import pickle

#crea mensaje
data = {"mensaje": "hola"}

#lo envia
serializacion = pickle.dumps(data)

#lo trae
mesaje = pickle.loads(serializacion)

print(mesaje)