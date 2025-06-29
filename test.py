import os ,random,threading,time

class Celula:
    #constructor de la clase celula
    def __init__(self,id,tipo,historial):
        self.id =id
        self.tipo=tipo #Alien, Humano, Infectado
        self.historial=historial #Infectado: {0-4} | No-infectado: {-1}
        self.lock = threading.Lock()
    
    def __str__(self):
        return f"Célula(ID={self.id}, Tipo={self.tipo})"
    
    def datos(self):
        return (self.id,self.tipo)

    def registra_historial(self,llave,valor):
        historial=self.historial
        historial[llave]=valor
        self.historial=historial

    #se espera que ronda actual es un int
    def infeccion(self,ronda_actual):
        tipo=[]
        if ronda_actual >= 2:
            if (self.tipo == "Infectado"):
                historial=self.historial
                contador=0
                while contador <2:
                    ronda_actual-=1
                    tipo.append(historial[ronda_actual])
                    contador+=1
                contador = tipo.count("Infectado")

                print(tipo,contador)
                if contador == 2:
                    self.tipo="Alien"

            

    def setter_tipo(self,tipo):
        self.tipo=tipo
    
    # Getter 
    def getter_tipo(self):
        return self.tipo
    def getter_numero(self):
        return self.id
    def getter_historial(self):
        return self.historial

lock = threading.Lock()

def crear_celula(id,tipo,historial, diccio_celulas):
    print(f"[Hilo {threading.current_thread().name}] Creando célula ID={id}, tipo={tipo}")
    cel = Celula(id, tipo, historial.copy())
    with lock:
        if tipo not in diccio_celulas:
            diccio_celulas[tipo] = []
        diccio_celulas[tipo].append(id)

def escribir_archivo(nombre_archivo, diccio_celulas):
    archivo = open(nombre_archivo, "w")
    for tipo in diccio_celulas:
        archivo.write(f"{tipo}:\n")
        for celula in diccio_celulas[tipo]:
            archivo.write(f"\tCelula {celula}\n")
    archivo.close()
    return

threads = []
diccio_celulas = {}

num_alien = 0
num_humano = 0
id = 0

historial = []

## Crear archivos de rondas
for cont_archivo  in range(5):
    archivo = open(f"Ronda_{cont_archivo+1}.txt", "w")
    archivo.close()

## Iniciacion de las celulas 
for _ in range(512):
    id += 1
    probablidad_tipo=random.randint(0,1)
    if probablidad_tipo == 0 and (num_alien < 16):
        t = threading.Thread(
            target=crear_celula,
            args=(id, "Alien", historial, diccio_celulas)
        )
        t.start()
        threads.append(t)
        num_alien += 1
    else:
        t = threading.Thread(
            target=crear_celula,
            args=(id, "Humano", historial, diccio_celulas)
        )
        t.start()
        threads.append(t)
        num_humano+=1

## Escribir configuración inicial
# Escribimos lista inicial de celulas y su tipo en el archivo aislamiento.txt
escribir_archivo("aislamiento.txt", diccio_celulas)


## Logica de Rondas
contador_rondas = 0
tiempo_ronda = 0

while contador_rondas < 5:
    lista_combate = []
    tiempo_inicio=time.monotonic()
    while time.monotonic() - tiempo_inicio < tiempo_ronda:
        ## Logica de Combate
        # tomo las celulas y las bloqueo
        # en su historial escribo con quien se enfretaron y que paso
        # como puede haber más de un combate -> 
        # escirbir directo en archivo
        print("termino ronda")
    ##termino ronda
    # escribimos lo que sucedio en ronda_X.txt, recuperado del historial de las celulas
    contador_rondas+=1

## Termino del juego
# escribimos en diagnostico_final.txt lista de celulas alienigenas y lista de celulas humanas
for t in threads:
    t.join()