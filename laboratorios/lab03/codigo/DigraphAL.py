"" "
    @class digraphAl
    Descripcion: implementacion de grafo con listas.
    @author David Sanchez Arboleda - Estefania Zapata
    @version 1.2
"" "


clase  digraphAL :

    def  __init__ ( auto , tamaño ):
        auto . tamaño = tamaño
        # Creo una lista
        self .lista = []
        # Recorro desde la posición 0 hasta el tamaño asignado creando listas en cada posición
        para i en el  rango (tamaño + 1 ): self .lista.append ([])

    def  add_arc ( self , source , destination , weight = 1 ):
        # Añadimos una tupla en el vértice asignado que contiene el vértice adyacente con el peso de la esquina que por defecto es 1
        self .lista [fuente] .append ((destino, peso))

 
    def  get_successors ( self , vértice ):
        # Creo una lista
        sucesores = []
        # Recorro la lista de mi vértice especificado
        para i en el  rango ( len ( self .lista [vértice])):
            # Añado a mi lista creado todos los vértices adyacentes a mi vértice especificado
            successors.append ( self .lista [vértice] [i] [ 0 ])
        # Retorno mi lista creado
        retorno sucesores


    def  get_weight ( self , source , destination ):
        # Recorro la lista de mi vértice especificado
        para i en el  rango ( len ( self .lista [fuente])):
            # Si en la lista del vértice especificado se encuentra el vértice de destino retorno el peso del arco de los dos
            si  self .lista [fuente] [i] [ 0 ] == destino:
                return  self .lista [fuente] [i] [ 1 ]
        # Retorno cero por defecto
        devolver  0
