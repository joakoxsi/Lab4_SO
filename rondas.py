import time

contador_rondas = 1
tiempo_ronda = 1

while contador_rondas < 5:
    lista_combate = []
    tiempo_inicio=time.monotonic()
    contador=0
    while time.monotonic() - tiempo_inicio < tiempo_ronda:
        print(time.monotonic() - tiempo_inicio)
        ## Logica de Combate
        # tomo las celulas y las bloqueo
        # en su historial escribo con quien se enfretaron y que paso
        # como puede haber más de un combate -> 
        # escirbir directo en archivo
        contador+=1
    print(contador)
    ##termino ronda
    # escribimos lo que sucedio en ronda_X.txt, recuperado del historial de las celulas
    contador_rondas+=1
