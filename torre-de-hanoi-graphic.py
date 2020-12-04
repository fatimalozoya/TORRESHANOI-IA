from copy import deepcopy
from numpy import random


class Nodo:
  def __init__(self):
    self.estado = [[], [], []]
    self.numeroNodo = 0
    self.padre = None
    self.hijos = []
    self.puntos = 0


def evaluar(nodo):
    global numDiscos, columnas

    disco = numDiscos
    nodo.puntos = numDiscos * columnas

    calificar(nodo, disco)


def calificar(nodo, disco):
    global estadoMeta

    if disco > 0:
        for col in estadoMeta:
            if disco in col:

                posCol = estadoMeta.index(col)
                if disco in nodo.estado[posCol]:

                    posFila = estadoMeta[posCol].index(disco)
                    if nodo.estado[posCol][posFila] != None:

                        if disco == nodo.estado[posCol][posFila]:
                            nodo.puntos = nodo.puntos - 1

                            calificar(nodo, disco - 1)             


def movimiento(pila1, pila2):
    p1 = pila1[:]
    p2 = pila2[:]

    if len(p1) > 0:
        disco = p1[len(p1) - 1]
        ultimoP2 = len(p2) - 1

        if len(p2) == 0 or p2[ultimoP2] > disco:
            p2.append(disco)
            p1.pop()

            return p1, p2
        else:
            return None
    else:
        return None


def movimientos(nodo):
    global columnas, estados
    pila = []

    for x in range(0, columnas):
        for y in range(0, columnas):

            pila = movimiento(nodo.estado[x], nodo.estado[y])

            if pila != None:
                nodoSig = Nodo()
                nodoSig = deepcopy(nodo)
                nodoSig.estado[x] = deepcopy(pila[0])
                nodoSig.estado[y] = deepcopy(pila[1])

                if not nodoSig.estado in estados:
                    numeroNodo = nodoSig.numeroNodo
                    estados.append(nodoSig.estado)
                    return nodoSig
    return None


def DFS(nodo):
    global numeroNodo
    esEstadoMeta = False

    if esEstadoMeta == False:
        padre = deepcopy(nodo)
        nodo = movimientos(nodo)

        if nodo != None:
            numeroNodo += 1
            nodo.numeroNodo = numeroNodo
            nodo.padre = padre
            print('Nodo ', nodo.numeroNodo, nodo.estado, '\n')

            if nodo.estado == estadoMeta:
                print('\n\nEstado Meta Alcanzado')
                dibujarSolucion(nodo)
                esEstadoMeta = True

                return True

            DFS(nodo)
        else:
            nodo = padre.padre
            print('Volviendo al Nodo', nodo.numeroNodo, 'Estado', nodo.estado)

            DFS(nodo)


def BFS(nodo):
    global padresList, numeroNodo, hijosList, nivel
    esEstadoMeta = False

    print('\nNivel : ', nivel)
    nivel += 1

    for nodo in padresList:
        if esEstadoMeta == False:
            print('Nodo Padre:', nodo.numeroNodo, ' Estado :', nodo.estado)
            tieneHijos = False
            padre = deepcopy(nodo)

            i = 1
            while tieneHijos == False:

                i += 1
                hijo = movimientos(nodo)

                if hijo != None:
                    numeroNodo += 1
                    hijo.numeroNodo = numeroNodo
                    hijo.padre = nodo
                    padre.hijos.append(hijo)
                    hijosList.append(hijo)
                    print('└--Nodo Hijo:', hijo.numeroNodo,
                          'Estado:', hijo.estado)
                    if hijo.estado == estadoMeta:
                        print('\n\nEstado Meta Alcanzado')
                        dibujarSolucion(hijo)
                        esEstadoMeta = True
                        return True
                else:
                    tieneHijos = True

    padresList = deepcopy(hijosList)
    hijosList = []

    if esEstadoMeta == False:
        BFS(padresList)


def BFS_enhanced(nodo):
    global padresList, numeroNodo, hijosList, numDiscos

    esEstadoMeta = False
    puntosMin = numDiscos * columnas

    for nodo in padresList:
        evaluar(nodo)

        if nodo.puntos < puntosMin:
            puntosMin = nodo.puntos

    for nodo in padresList:
        if esEstadoMeta == False and nodo.puntos == puntosMin:
            print('\nNodo Padre:', nodo.numeroNodo, ' Estado :', nodo.estado, 'Costo = ', nodo.puntos)
            tieneHijos = False
            padre = deepcopy(nodo)

            i = 1
            while tieneHijos == False:

                i += 1
                hijo = movimientos(nodo)

                if hijo != None:
                    numeroNodo += 1
                    hijo.numeroNodo = numeroNodo
                    hijo.padre = nodo
                    hijosList.append(hijo)
                    print('└--Nodo Hijo:', hijo.numeroNodo, 'Estado:', hijo.estado)

                    if hijo.estado == estadoMeta:
                        print('\n\nEstado Meta alcanzado')
                        dibujarSolucion(hijo)
                        esEstadoMeta = True
                        return True
                else:
                    tieneHijos = True

    padresList = deepcopy(hijosList)
    hijosList = []

    if esEstadoMeta == False:
        BFS_enhanced(nodo)


def leerEstado():
    global columnas
    estado=[]
    for x in range(0,columnas):
        print('Discos en la columna ',x+1,': ',)
        a = [int(x) for x in input().split()]
        estado.append(a)

    return estado


def dibujarSolucion(nodo):
    global numDiscos, columnas
    
    while True:
        estado = nodo.estado
        print('\nNodo Numero: ', nodo.numeroNodo, '  Estodo:  ', estado)
        print("\n ", imprimirDisco(None), end="")
        print(" ", imprimirDisco(None), end="")
        print(" ", imprimirDisco(None))
        
        for fila in range(numDiscos).__reversed__():
            for col in range(columnas):
                try:
                    print(" ", imprimirDisco(estado[col][fila]), end="")
                except:
                    print(" ", imprimirDisco(None), end="")
            print("")

        print("#" * int(((numDiscos * 2) + 2) * 4))

        if nodo.padre != None:
            nodo = nodo.padre
        else:
            break


def imprimirDisco(numDisco):
    espacio = (numDiscos * 2) + 1
    disco = ""

    if numDisco == 0 or numDisco == None:
        for i in range(espacio):
            if i == int(espacio / 2):
                disco += "|"
            else:
                disco += " "

        return disco
    
    espacios = espacio - ((numDisco * 2) + 1)
    for i in range(int(espacios / 2)):
        disco += " "

    for i in range((numDisco * 2) + 1):
        disco += "○"

    for i in range(int(espacios / 2)):
        disco += " "
    
    return disco


# def estadoAleatorio(numDiscos):
#     global columnas
#     discos = []

#     for i in range(numDiscos):
#         discos.append(i + 1)

#     random.shuffle(discos)

#     estadoInicial = [[], [], []]

#     while len(discos) > 0:         
#         columnaAleatoria = int(random.randint(columnas))
#         indexDiscoAleatorio = random.randint(len(discos))

#         estadoInicial[columnaAleatoria].append(discos.pop(indexDiscoAleatorio))

#     random.shuffle(estadoInicial)

#     return estadoInicial

columnas = 3
numDiscos = 4

for i in range(20):
    print('\n\t1. Depth First Search')
    print('\t2. Breadth First Search')
    print('\t3. Best First Search')
    print('\t4. Salir')

    opcion = input("\nSelecciona un algoritmo--> ")

    if opcion == '4':
        print('\nSaliendo...')
        break

    estadoInicial = [[2], [3], [1, 4]]
    estadoMeta = [[],[],[4,3,2,1]]    

    # columnas = int(input("\nIngresa el numero de columnas--> "))

    print('\nIngresa el esatdo inicial: ')
    estadoInicial = leerEstado()
    # print('\nIngresa el estado meta: ')
    # estadoMeta = leerEstado()


    print("\n" * 30)
    print('Estado Inicial: ', estadoInicial)
    print('Estado Meta: ', estadoMeta)

    estados = [estadoInicial]

    numeroNodo = 1 
    nodo = Nodo()
    nodo.estado = estadoInicial
    nodo.numeroNodo = numeroNodo
    padresList = [nodo]
    hijosList = []

    nivel = 1

    padresList = [nodo]
    hijosList = []


    if opcion == '1':
        print('\n--Depth First Search')
        DFS(nodo)

    elif opcion == '2':
        print('\n--Breadth First Search')
        BFS(nodo)

    elif opcion == '3':
        print('\n--Best First Search')
        BFS_enhanced(nodo)
    else:
        print('Opcion invalida')
        continue