import threading, random, time

class Celula(threading.Thread):
    lock_archivo = threading.Lock()

    # Constructor:
    def __init__(self,id,tipo):
        super.__init__()
        self.id = id
        self.tipo = tipo                # "Alien", "Humano", "Infectado"
        self.historial = {}             # {ronda: estado}
        self.lock = threading.Lock()
        #self.ronda_infeccion = None    # Para el bonus
    
    def __str__(self):
        return f"Célula(ID={self.id}, Tipo={self.tipo})"
    
    #Aqui se hace 
    def registra_historial(self,llave,valor):
        historial=self.historial
        historial[llave]=valor
        self.historial=historial

    def actualizar_tipo(self, nuevo_tipo: str):
        """Cambia el tipo (“Alien”, “Humano”, “Infectado”), de forma segura."""
        with self.lock:
            self.tipo = nuevo_tipo

    def obtener_tipo(self) -> str:
        """Devuelve el tipo actual de la célula."""
        with self.lock:
            return self.tipo


    def escribir_archivo_inicial(self):
        self.candado_archivo.acquire()
        try:
            archivo=open("aislamiento.txt","a")
            archivo.write(f"La Celula {self.getter_numero()} es del tipo {self.getter_tipo()} \n")
            archivo.close()
        finally:
            self.candado_archivo.release()

        

    def setter_tipo(self,tipo):
        self.tipo=tipo
    
    # Getter 
    def getter_tipo(self):
        return self.tipo
    def getter_numero(self):
        return self.id
    def getter_historial(self):
        return self.historial

    celulas.append(Celula(i+1, tipo, historial_inicial))

## Crear archivos de rondas
for cont_archivo  in range(5):
    archivo = open(f"Ronda_{cont_archivo+1}.txt", "w")
    archivo.close()
## Crear archivos iniciales y finales 
for nombre in ["aislamiento","diagnostico_final"]:
    archivo = open(f"{nombre}.txt", "w")
    archivo.close()



## Enlazar cada celula con su respectivo hilo
threads = []
id_map = { c.id: c for c in celulas }
for cel in celulas:
    t = threading.Thread(target=celula_worker, args=(cel))
    t.start()
    threads.append(t)

#Logica para poder escribir las cosas 
def escribir_archivo(nombre_archivo, diccio_celulas):
    archivo = open(nombre_archivo, "w")
    for tipo in diccio_celulas:
        archivo.write(f"{tipo}:\n")
        for celula in diccio_celulas[tipo]:
            archivo.write(f"\tCelula {celula}\n")
    archivo.close()
    return

def combate(celula1,celula2):

    primero, segundo = [celula1, celula2]
    acquired1 = acquired2 = False
    try:
        frase=f"La Celula {celula1.getter_numero()} se enfrentara con la Celula {celula2.getter_numero()}"
        resultado=""
        # Adquirimos candados en orden
        acquired1 = primero.candado.acquire(timeout=1)
        acquired2 = segundo.candado.acquire(timeout=1)
        lista=[celula1.getter_tipo(),celula2.getter_tipo()]
        if (( "Humano" in lista ) and (("Alien" in lista ) or ("Infectado" in lista ))):
            ##hay pelea entere las personas 
            if (probablidad_infeccion()):
                if (celula1.getter_tipo() == "Humano"):
                    celula1.setter_tipo("Infectado")
                    resultado=f"La Celula {celula1.getter_numero()} fue infectada"
                else:
                    celula2.setter_tipo("Infectado")
                    resultado=f"La Celula {celula2.getter_numero()} fue infectada"
            else:
                if (celula1.getter_tipo() == "Humano"):  
                    resultado=f"La Celula {celula1.getter_numero()} no fue infectada"
                else:
                    resultado=f"La Celula {celula2.getter_numero()} no fue infectada"
        else:
            contador=lista.count("Humano")
            if contador ==2:
                resultado=f"La Celula {celula1.getter_numero()} y {celula2.getter_numero()} no hacen nada  "
            else:
                resultado = f"La Celula {celula1.getter_numero()} y {celula2.getter_numero()} van a coperaran  "
    finally:
        if acquired2:
            segundo.candado.release()
        if acquired1:
            primero.candado.release()
    frase_final=f"{frase} -- El resultado es: {resultado}"
    return frase_final
    
def probablidad_infeccion(probabilidad: int = 70) -> bool:
    return random.random() < (probabilidad/100)

arreglo_celulas=[]
num_alien = 0
num_humano = 0
id_celula=0
historial=[]
diccio_celulas = {}

for _ in range(512):
    id_celula += 1
    tipo=""
    probablidad_tipo=random.randint(0,1)
    if probablidad_tipo == 0 and (num_alien < 16):
        tipo="Alien"
        t = Celula(id_celula, "Alien", historial,)

        arreglo_celulas.append(t)
        num_alien += 1
    else:
        tipo="Humano"
        t = Celula(id_celula, "Humano", historial)
        arreglo_celulas.append(t)
        num_humano+=1

    if tipo not in diccio_celulas:
        diccio_celulas[tipo] = []
    diccio_celulas[tipo].append(id_celula)



for celulas in arreglo_celulas:
    celulas.start()

escribir_archivo("aislamiento.txt", diccio_celulas)




## Logica de Rondas
contador_rondas=1

while contador_rondas <= 5:
    lista_enfrentaminetos = []
    tiempo_ronda = 10 #segundos
    tiempo_inicio = time.monotonic()
    numero_combate = 0
    
    while time.monotonic() - tiempo_inicio < tiempo_ronda:
        #logica de Combate 
        random1 = random.randint(0,511)
        random2 = random.randint(0,511)
        # Se encuentran 2 celulas
        celula_1 = arreglo_celulas[random1]
        celula_2 = arreglo_celulas[random2]

        resultado = combate(celula_1,celula_2)
        lista_enfrentaminetos.append(f'Enfrentamiento {numero_combate} - {resultado}')
        
        numero_combate += 1
    
    # Volcar resultados en el archivo 'rondas_X.txt'
    archivo = open(f"Ronda_{contador_rondas}.txt","w")
    for iteracion in lista_enfrentaminetos:
        archivo.write(f"{iteracion}  \n")
    archivo.close()

    contador_rondas += 1
    print(numero_combate)

# Diagnostico Final
diccio_celulas={}
for celulas in arreglo_celulas:
    tipo=celulas.getter_tipo()
    if tipo not in diccio_celulas:
        diccio_celulas[tipo] = []
    diccio_celulas[tipo].append(celulas.getter_numero())

# Volcar el diagnostico en el archivo 'diagnostico_final.txt'
escribir_archivo("diagnostico_final.txt", diccio_celulas)

