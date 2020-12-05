from copy import deepcopy
from numpy import random
import pandas
import time


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


def movimientos(nodo):
    global columnas, numeroNodo, estados
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


def movimiento(pila1, pila2):
    p1 = pila1[:]
    p2 = pila2[:]

    if len(p1) > 0:
        disco = p1[len(p1) - 1]
        indexP2 = len(p2) - 1

        if len(p2) == 0 or p2[indexP2] > disco:
            p2.append(disco)
            p1.pop()

            return p1, p2
        else:
            return None
    else:
        return None


def DFS(nodo):
    global numeroNodo, nodoActual
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
                nodoActual = nodo
                esEstadoMeta = True

                return True

            DFS(nodo)
        else:
            nodo = padre.padre
            print('Volviendo al Nodo', nodo.numeroNodo, 'Estado', nodo.estado)

            DFS(nodo)


def BFS(nodo):
    global padresList, numeroNodo, hijosList, nivel, nodoActual
    esEstadoMeta = False

    print('\nNivel : ', nivel)
    nivel += 1

    for nodo in padresList:
        if esEstadoMeta == False:
            print('Nodo Padre:', nodo.numeroNodo, ' Estado :', nodo.estado)
            tieneHijos = False

            while tieneHijos == False:

                hijo = movimientos(nodo)

                if hijo != None:
                    numeroNodo += 1
                    hijo.numeroNodo = numeroNodo
                    hijo.padre = nodo
                    hijosList.append(hijo)

                    print('└--Nodo Hijo:', hijo.numeroNodo, 'Estado:', hijo.estado)

                    if hijo.estado == estadoMeta:
                        print('\n\nEstado Meta Alcanzado')
                        nodoActual = hijo
                        esEstadoMeta = True

                        return True
                else:
                    tieneHijos = True

    padresList = deepcopy(hijosList)
    hijosList = []

    if esEstadoMeta == False:
        BFS(padresList)


def BFS_enhanced(nodo):
    global padresList, numeroNodo, hijosList, numDiscos, nodoActual

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
                        esEstadoMeta = True
                        nodoActual = hijo

                        return True
                else:
                    tieneHijos = True

    padresList = deepcopy(hijosList)
    hijosList = []

    if esEstadoMeta == False:
        BFS_enhanced(nodo)


def obtenerIntentos(nodo):
    estados = deepcopy(nodo)

    i = 0
    while True:
        if nodo.padre != None:
            i += 1
            nodo = nodo.padre
        else:
            break
    return i


def estadoAleatorio(numDiscos):
    global columnas
    discos = []

    for i in range(numDiscos):
        discos.append(i + 1)

    random.shuffle(discos)

    estadoInicial = [[], [], []]

    while len(discos) > 0:         
        columnaAleatoria = int(random.randint(columnas))
        indexDiscoAleatorio = random.randint(len(discos))

        estadoInicial[columnaAleatoria].append(discos.pop(indexDiscoAleatorio))

    random.shuffle(estadoInicial)

    return estadoInicial


def prepararNodo():
    global estadoInicial

    estados[:] = [estadoInicial]

    numeroNodo = 1 
    nodo = Nodo()
    nodo.estado = estadoInicial
    nodo.numeroNodo = numeroNodo
    padresList = [nodo]
    hijosList = []

    nivel = 1

    padresList = [nodo]
    hijosList = []


columnas = 3
numDiscos = 4

estadosList = []

tiempoBFS = []
tiempoDFS = []
tiempoBFS_e = []

movimientosBFS = []
movimientosDFS = []
movimientosBFS_e = []

estadoInicial = [[2], [3], [1, 4]]
estadoMeta = [[],[],[4,3,2,1]]

for i in range(40):

    while True:
        estadoInicial = estadoAleatorio(numDiscos)
        
        if not estadoInicial in estadosList:
            estadosList.append(estadoInicial)
            break
    
    print("\n" * 3, "-" * 10, "Numero de iteración: ", i + 1, " ", "-" * 10)
    print('Estado Inicial: ', estadoInicial)


    estados = [estadoInicial]

    numeroNodo = 1 
    nodo = Nodo()
    nodo.estado = estadoInicial
    nodo.numeroNodo = numeroNodo
    padresList = [nodo]
    hijosList = []

    nivel = 1

    padresList = [nodo]

    nodoActual = Nodo()


    prepararNodo()
    inicioTiempo = time.time()
    DFS(nodo)
    finTiempo = time.time()

    tiempoDFS.append(finTiempo - inicioTiempo)
    movimientosDFS.append(obtenerIntentos(nodoActual))


    prepararNodo()
    inicioTiempo = time.time()
    BFS(nodo)
    finTiempo = time.time()

    tiempoBFS.append(finTiempo - inicioTiempo)
    movimientosBFS.append(obtenerIntentos(nodoActual))


    prepararNodo()
    inicioTiempo = time.time()
    BFS_enhanced(nodo)
    finTiempo = time.time()

    tiempoBFS_e.append(finTiempo - inicioTiempo)
    movimientosBFS_e.append(obtenerIntentos(nodoActual))


csv = {'Estado Inicial': estadosList,
        'Tiempo DFS': tiempoDFS,
        'Movimientos DFS': movimientosDFS,
        'Tiempo BFS': tiempoBFS,
        'Movimientos BFS': movimientosBFS,
        'Tiempo BFS_e': tiempoBFS_e,
        'Movimientos BFS_e': movimientosBFS_e}

df = pandas.DataFrame(csv, columns=['Estado Inicial',
                                    'Tiempo DFS',
                                    'Movimientos DFS',
                                    'Tiempo BFS',
                                    'Movimientos BFS',
                                    'Tiempo BFS_e',
                                    'Movimientos BFS_e'])

print("\n"*10)
print(df)
df.to_csv(r'plot.csv', index = False, header=True)
input("\nPresiona Enter para continuar...")