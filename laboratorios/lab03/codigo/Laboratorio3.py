
 #   @clase laboratorio3
  #  Descripcion: Puntos del laboratorio 3
   # @author Estefania Zapata y David Sanchez Arboleda
    #@versión 1.0

importar DigraphAL, DigraphAM
cola de importación , matemáticas

# Generamos un grafo de matriz y lo llenamos
gmatriz = DigraphAM.digraphAM ( 11 )
gmatriz.add_arc ( 5 , 11 )
gmatriz.add_arc ( 11 , 2 )
gmatriz.add_arc ( 11 , 9 )
gmatriz.add_arc ( 11 , 10 )
gmatriz.add_arc ( 7 , 11 )
gmatriz.add_arc ( 7 , 8 )
gmatriz.add_arc ( 8 , 9 )
gmatriz.add_arc ( 3 , 8 )
gmatriz.add_arc ( 3 , 10 )

# Generamos un grafo de lista y lo llenamos
glista = DigraphAL.digraphAL ( 11 )
glista.add_arc ( 5 , 11 )
glista.add_arc ( 11 , 2 )
glista.add_arc ( 11 , 9 )
glista.add_arc ( 11 , 10 )
glista.add_arc ( 7 , 11 )
glista.add_arc ( 7 , 8 )
glista.add_arc ( 8 , 9 )
glista.add_arc ( 3 , 8 )
glista.add_arc ( 3 , 10 )


def  n_reinas ( n ):
    tablero = [ Ninguno ] * n
    devolver n_reinas_aux ([], 0 , tablero)

def  prueba ( n ):
    tablero = [ Ninguno ] * n
    k = 0
    para i en el  rango (n):
        si puedo_poner_reina (i, tablero):
            tablero [k] = i
            k + = 1
    tablero de retorno



def  n_reinas_aux ( r , n , tablero ):
    si n > = len (tablero):
        r.append (tablero)
        retorno r
    mas :
        para i en el  rango ( len (tablero)):
            tablero [n] = i
            si puedo_poner_reina (n, tablero):
                n_reinas_aux (r, n + 1 , tablero)
    retorno r

def  puedo_poner_reina ( r , tablero ):
    para i en el  rango (r):
        if  abs (tablero [i] - tablero [r]) == r - i o tablero [i] == tablero [r]:
            retorno  falso
    devuelve  verdadero

def  punto1_5 ( gráfico ):
    grafo = transformar_grafo (gráfico)
    llaves = grafo.keys ()
    # recorremos todas las llaves
    para i en teclas:
        # recorremos los elementos de la lista de cada llave
        para k en grafo [i]:
            # si la llave es un elemento del elemento que tiene en su lista
            # o si la llave es un elemento de su propia lista entonces hay ciclo
            si i en grafo [k] o grafo [k] == i:
                devuelve  verdadero
    retorno  falso

   

def  transformar_grafo ( gráfico ):
    grafo = {}
    para i en el  rango (graph.size + 1 ):
        sucesores = graph.get_successors (i)
        # recorremos el tamaño del grafo creando llaves con listas en un diccionario
        grafo [i] = []
        para k en  rango ( len (sucesores)):
            # por cada llave agregamos una lista de sus sucesores
            grafo [i] .append (sucesores [k])
    return grafo



def  punto1_3 ( grafo , inicial ):
  recorrido = []
  q = queue.PriorityQueue ()
  q.put (inicial)
  recorrido.append (inicial)
  mientras que  no es q.empty ():
    actual = q.get ()
    # Mientras la cola no está vacía se revisará cada vértice sucesor del vértice atual
    # si este no se encunetra en el recorrido se agrega
    para i en grafo.get_successors (actual):
      Si i no  en el Recorrido:
        recorrido.append (i)
        q.put (i)
  regreso recorrido


def  punto1_6 ( grafo , inicial , final ):
  # llenar el arreglo de distancias con infinito
  costo = [math.inf] * (grafo.size + 1 )
  # marcar la distancia del nodo inicial como 0
  costo [inicial] =  0
  s_pathA (grafo, inicial, costo)
  costo de retorno [final]

def  punto1_6aux ( grafo , inicial , costo ):
  s = grafo.get_successors (inicial)
  si  len (s) ==  0 :
    pasar
  mas :
    para i en s:
      peso = grafo.get_weight (inicial, i) + costo [inicial]
      
      si costo [i] > peso:
        costo [i] = peso
      punto1_6aux (grafo, i, costo)



def  punto2 ( grafo , nodo ):
    costo = [math.inf] * (grafo.size + 1 )
    recorrido = []
    costo [ 1 ] =  0
    punto2aux (grafo, 1 , nodo, costo, recorrido)
    recorrido.append (nodo)
    si costo [n] == math.inf:
        retorno  - 1
    mas :
        regreso recorrido



def  punto2aux ( grafo , k , nodo , costo , recorrido ):
  kk = grafo.get_successors (k)
  si  len (kk) ==  0 :
    pasar
  mas :
    para i en kk:
      peso = grafo.get_weight (k, i) + costo [k]
      si costo [i] > peso:
        si k no está  en recorrido:
          recorrido.append (k)
        costo [i] = peso
      mas :
        si k en recorrido:
          recorrido.remove (k)
      punto2aux (grafo, i, nodo, costo, recorrido)