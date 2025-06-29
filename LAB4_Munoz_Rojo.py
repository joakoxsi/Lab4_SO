import os ,random,threading


class Celula:

    def __init__(self,id,tipo,historia):
        self.id =id
        self.tipo=tipo
        self.historia=historia
    
    def __str__(self):
        return f"Célula(ID={self.id}, Tipo={self.tipo})"
    
    def datos(self):
        return (self.id,self.tipo)

    def registra_historial(self,llave,valor):
        historial=self.historia
        historial[llave]=valor
        self.historia=historial

    #se espera que ronda actual es un int
    def infeccion(self,ronda_actual):
        tipo=[]
        if ronda_actual >= 2:
            if (self.tipo == "Infectado"):
                historial=self.historia
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
        return self.historia
    





nombre_archivo=["aislamiento","ronda_","diagnostico_final","acciones_anticuerpo"]
tipo=["Alien","Humano","Infectado"]
tipo_arreglo=["Alien","Humano"]

historia={0:"",1:"",2:"",3:"",4:"",5:""}


#Funciones AUXILIARES

def crear_celula(id,tipo,historial):
    print(f"[Hilo {threading.current_thread().name}] Creando célula ID={id}, tipo={tipo}")
    celula=Celula(id,tipo,historial)



def probablidad_infeccion():
    probablidad_infeccion = random.randint(1, 10)

    if (probablidad_infeccion >= 7): #Probalididad de que no se infecte 30%
        return False
    else:
        return True


def combate(celula1,celula2,n_ronda):
    lista=[celula1.getter_tipo,celula2.getter_tipo]
    if (( "Humano" in lista ) and (("Alien" in lista ) or ("Infectado" in lista ))):
        ##hay pelea entere las personas 
        if (probablidad_infeccion()):
            if (celula1.getter_tipo == "Humano"):
                celula1.tipo="Infectado"
            else:
                celula2.tipo="Infectado"




def archivos_creacion(nombre,lista_celulas,Nronda=0,):

    if Nronda==0 or Nronda==6:
        f=open(f"{nombre}.txt","w")
    else:
        f=open(f"{nombre}{Nronda}.txt","w")

    for celula in lista_celulas:
        celula_n=celula.datos()

        f.write(f"La célula número {celula_n[0]} es del tipo {celula_n[1]} \n")


numero_alien_inicial=16
arreglo_celulas=[]

contador_celulas_humanas=0
numero_celulas_totales=0
id_celula=0

#Iniciacion de las celulas 
# Falta Incorporal el Hilo 

for _ in range(512):
    id_celula+=1
    if (numero_alien_inicial > 0) and ((contador_celulas_humanas <= 25) and (contador_celulas_humanas >= 10) ):
        probablidad_tipo=random.randint(0,1)
        if probablidad_tipo == 0:
            arreglo_celulas.append(threading.Thread(target=crear_celula, args=(id_celula,tipo_arreglo[probablidad_tipo],historia)))
            numero_alien_inicial-=1
            contador_celulas_humanas=0
        else:
            arreglo_celulas.append(threading.Thread(target=crear_celula, args=(id_celula,tipo_arreglo[probablidad_tipo],historia)))
            contador_celulas_humanas+=1
    else:
        arreglo_celulas.append(threading.Thread(target=crear_celula, args=(id_celula,tipo_arreglo[1],historia)))
        contador_celulas_humanas+=1
    



for t in arreglo_celulas:
    t.start()





"""
tipo=["Alien","Humano","Infectado"]

historia_t={0:"Humano",1:"Infectado",2:"Infectado",3:4,4:4,5:4}

test=Celula(12,tipo[2],historia_t)

print(test.historia)
print(test.getter_tipo())
test.infeccion(5)
print(test.getter_tipo())

#archivos_creacion(nombre_archivo[0],arreglo_celulas)
"""





