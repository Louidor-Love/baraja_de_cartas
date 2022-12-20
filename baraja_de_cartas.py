import random

def mazo_nuevo():
    
    trebol     = [str(x).zfill(2) for x in range(1,14)]
    picas      = [str(x).zfill(2) for x in range(1,14)]
    diamantes  = [str(x).zfill(2) for x in range(1,14)]
    corazones  = [str(x).zfill(2) for x in range(1,14)]

    mazo = trebol + picas + diamantes + corazones

    
    random.shuffle(mazo)
    
    return mazo

def siguiente_carta_del_lomo():
    siguiente = mazo.pop()
    return siguiente

def reparto_cartas():
    
    for cada in range(1,14):
        if  dic_mesa[cada] == [] :
            
            proxima = siguiente_carta_del_lomo()
            
            dic_mesa[cada] = [proxima]
            
            
        elif int(dic_mesa[cada][-1]) == cada:
            #hay una carta bien colocada, saltamos esta pila
            pass

        else:
            proxima = siguiente_carta_del_lomo()
            dic_mesa[cada].append(proxima)
            
        if len(mazo)==0:
            #No hay mas cartas en el mazo, el juego termina
            return False
        
    return True



def mostrar_mesa():
    cuantas_bien = 0  
    cuales_busco = [] 
    
    for f in range(1,14):
        if dic_mesa[f]:
            if int(dic_mesa[f][-1]) == f:
                print(str(f).zfill(2),"Good :",end="") #Si la pila esta terminada
                cuantas_bien += 1 # Contamos las pilas finalizadas
                
            else:
                print(str(f).zfill(2),"Wrong  :",end="") 
                cuales_busco.append(str(f).zfill(2)) 
            print(f"In the pile of number{f} is: {dic_mesa[f]}" ) 
    return cuantas_bien, list(set(cuales_busco))
    
    
def recoger_cartas():
    
    lista = []
    for f in dic_mesa:
        if int(dic_mesa[f][-1] )== f:
            #la ultima carta es la correcta, esta pila no la toco
            pass
        else:
            lista += dic_mesa[f] 
            dic_mesa[f] = list() 
    
    print(f"Cards to shuffle: {lista}") # Muestro las cartas que seran recicladas
    return lista    

def verifica_final_posible(disponibles, buscados):
    #Verificamos que las cartas disponibles nos permitan finalizar el juego
    print(f"\nWe need: {buscados}")
    posible = True
    for f in buscados:
        if not f in disponibles:
            return False
    return True

mazo = mazo_nuevo()


dic_mesa =  dict.fromkeys([x for x in range(1,14)], list())

intentos = 0
continuar = True
while continuar:
    
    sigo = True
    while sigo:
        sigo = reparto_cartas()
        cuantas_bien, cuales_busco = mostrar_mesa()
        print(f"\n--------------{cuantas_bien} Right--------------\n")
        
        if cuantas_bien > 12: # Si hay 13 pilas completas ganamos el juego
            print("Successfully Completed Game")
            
            continuar=False
            break
    
    if continuar:
        mazo = recoger_cartas() # Juntamos las cartas de las pilas incompletas
        if not verifica_final_posible(mazo, cuales_busco):
            print("I got you bro,Imposible to complete")
            continuar = False
            break

        intentos +=1
        print(f"\nWe mix and Continue ({intentos})\n")
    



