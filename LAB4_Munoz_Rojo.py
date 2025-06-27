import os ,random,threading


class Celula:

    def __init__(self,id,tipo):
        self.id =id
        self.tipo=tipo
    
    def __str__(self):
        return f"Célula(ID={self.id}, Tipo={self.tipo})"
    
    def datos(self):
        return (self.id,self.tipo)



nombre_archivo=["aislamiento","ronda_","diagnostico_final","acciones_anticuerpo"]
tipo={"Alien":0,"Humano":1,"Infectado":3}
tipo_arreglo=["Alien","Humano"]

historia={"1":4,"2":4,"3":4,"4":4,"5":4}



def probablidad_infeccion():
    probablidad_infeccion = random.randint(1, 10)

    if (probablidad_infeccion >= 7): #Probalididad de que no se infecte 30%
        return False
    else:
        return True


def combate(celula1,celula2):
    #
    if ((celula1+celula2) == 1):
        ##hay pelea entere las personas 
        if (probablidad_infeccion()):
            print(probablidad_infeccion())




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
for _ in range(512):
    id_celula+=1

    if (numero_alien_inicial > 0) and ((contador_celulas_humanas <= 25) and (contador_celulas_humanas >= 10) ):
        probablidad_tipo=random.randint(0,1)
        if probablidad_tipo == 0:
            arreglo_celulas.append(Celula(id_celula,tipo_arreglo[probablidad_tipo]))
            numero_alien_inicial-=1
            contador_celulas_humanas=0
        else:
            arreglo_celulas.append(Celula(id_celula,tipo_arreglo[1]))
            contador_celulas_humanas+=1
    else:
        arreglo_celulas.append(Celula(id_celula,tipo_arreglo[1]))
        contador_celulas_humanas+=1
    


for celula_propia in arreglo_celulas:
    print(celula_propia.datos())


archivos_creacion(nombre_archivo[0],arreglo_celulas)





