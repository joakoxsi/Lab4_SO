import threading, random, time

class Celula:
    def __init__(self, id: int, tipo: str, historial: dict):
        """
        id       : identificador único de la célula
        tipo     : "Alien", "Humano" o "Infectado"
        historial: diccionario que guarda eventos, p.ej.
                   {'combates': [(ronda, oponente_id, resultado), ...]}
        """
        self.id = id
        self.tipo = tipo
        self.historial = historial.copy()
        # candado propio para proteger cambios concurrentes
        self.lock = threading.Lock()

    def __str__(self):
        return f"Célula(ID={self.id}, Tipo={self.tipo})"

    def registrar_combate(self, ronda: int, oponente_id: int, resultado: str):
        """
        Guarda en el historial un tupla (ronda, oponente_id, resultado),
        p.ej. resultado puede ser "victoria" o "derrota".
        """
        with self.lock:
            self.historial.setdefault('combates', []).append(
                (ronda, oponente_id, resultado)
            )

    def actualizar_tipo(self, nuevo_tipo: str):
        """Cambia el tipo (“Alien”, “Humano”, “Infectado”), de forma segura."""
        with self.lock:
            self.tipo = nuevo_tipo

    def obtener_tipo(self) -> str:
        """Devuelve el tipo actual de la célula."""
        with self.lock:
            return self.tipo

    def obtener_historial(self) -> dict:
        """Devuelve una copia del historial."""
        with self.lock:
            return self.historial.copy()


def celula_worker(cel: Celula):
    for ronda in range(5):
        start_barrier.wait()   # espera main
        opp = id_map[pairings[cel.id]]
        # adquiere locks y resuelve el combate...
        end_barrier.wait()
    return

def escribir_archivo(nombre_archivo, diccio_celulas):
    archivo = open(nombre_archivo, "w")
    for tipo in diccio_celulas:
        archivo.write(f"{tipo}:\n")
        for celula in diccio_celulas[tipo]:
            archivo.write(f"\tCelula {celula}\n")
    archivo.close()
    return


## Crear archivos de rondas
for cont_archivo  in range(5):
    archivo = open(f"Ronda_{cont_archivo+1}.txt", "w")
    archivo.close()

## Iniciacion de las celulas 
num_alien  = 0
num_humano = 0
historial_inicial = {}
diccio_celulas = {}

celulas = []
for i in range(512):
    tipo = "Alien" if (random.randint(0,1)==0 and num_alien<16) else "Humano" #como el operador ternario ( ? :)
    if tipo == "Alien": 
        num_alien += 1
    else: 
        num_humano += 1

    celulas.append(Celula(i+1, tipo, historial_inicial))

    if tipo not in diccio_celulas:
            diccio_celulas[tipo] = []
    diccio_celulas[tipo].append(id)

## Enlazar cada celula con su respectivo hilo
threads = []
id_map = { c.id: c for c in celulas }
for cel in celulas:
    t = threading.Thread(target=celula_worker, args=(cel))
    t.start()
    threads.append(t)

## Escribir configuración inicial
escribir_archivo("aislamiento.txt", diccio_celulas)

tiempo_ronda = 10 #segundos
## Rondas
for ronda in range(1,6):
    random.shuffle(celulas)
    tiempo_inicio=time.monotonic()
    while time.monotonic() - tiempo_inicio < tiempo_ronda:
        for i in range(0, len(celulas), 2):
            a, b = celulas[i], celulas[i+1]
            pairings[a.id] = b.id
            pairings[b.id] = a.id

        # 2) Desatar combates
        start_barrier.wait()
        # 3) Esperar a que todas terminen
        end_barrier.wait()


