import threading
import time

def tarea(numero):
    print(f"Numero de hilo {numero}")
    


hilos = []

for i in range (1,8):
    hilo = threading.Thread(target=tarea , args=(i,))
    hilos.append(hilo)
    hilo.start()
    

for hilo in hilos:
    hilo.join()