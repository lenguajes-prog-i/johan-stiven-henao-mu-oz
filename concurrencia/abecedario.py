import threading
import time


# a, m cada letra imprimir 5 veces la letra

abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]

lista_hilos = []


def hilos(letra):
    for i in range(5):
        print(letra)


for letra in abecedario:
    hilo_letras = threading.Thread(target=hilos, args=(letra,))
    lista_hilos.append(hilo_letras)
    hilo_letras.start()

for hilo in lista_hilos:
    hilo.join()


