import os ,random,threading


nombre_output=["aislamiento","ronda_","diagnostico_final","acciones_anticuerpo"]
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




def archivos_creacion(nombre,Nronda=0):

    if Nronda==0:
        f=open(f"{nombre}.txt","w")
    else:
        f=open(f"{nombre}{Nronda}.txt","w")


numero_alien_inicial=16
arreglo_celular=[]

contador_celulas_humanas=0
numero_celulas_totales=0

for _ in range(516):


    if (numero_alien_inicial > 0) and ((contador_celulas_humanas <= 25) and (contador_celulas_humanas >= 10) ):
        probablidad_tipo=random.randint(0,1)
        if probablidad_tipo == 0:
            arreglo_celular.append(tipo_arreglo[probablidad_tipo])
            numero_alien_inicial-=1
            contador_celulas_humanas=0
        else:
            arreglo_celular.append(tipo_arreglo[1])
            contador_celulas_humanas+=1
    else:
        arreglo_celular.append(tipo_arreglo[1])
        contador_celulas_humanas+=1

print(arreglo_celular)
        



