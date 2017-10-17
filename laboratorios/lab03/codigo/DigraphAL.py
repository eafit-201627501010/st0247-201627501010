"" "
    @class digraphAl
    Descripcion: implementacion de grafo con listas.
    @author David Sanchez Arboleda - Estefania Zapata
    @version 1.2
"" "


clase  digraphAL :

    def  __init__ ( auto , tama�o ):
        auto . tama�o = tama�o
        # Creo una lista
        self .lista = []
        # Recorro desde la posici�n 0 hasta el tama�o asignado creando listas en cada posici�n
        para i en el  rango (tama�o + 1 ): self .lista.append ([])

    def  add_arc ( self , source , destination , weight = 1 ):
        # A�adimos una tupla en el v�rtice asignado que contiene el v�rtice adyacente con el peso de la esquina que por defecto es 1
        self .lista [fuente] .append ((destino, peso))

 
    def  get_successors ( self , v�rtice ):
        # Creo una lista
        sucesores = []
        # Recorro la lista de mi v�rtice especificado
        para i en el  rango ( len ( self .lista [v�rtice])):
            # A�ado a mi lista creado todos los v�rtices adyacentes a mi v�rtice especificado
            successors.append ( self .lista [v�rtice] [i] [ 0 ])
        # Retorno mi lista creado
        retorno sucesores


    def  get_weight ( self , source , destination ):
        # Recorro la lista de mi v�rtice especificado
        para i en el  rango ( len ( self .lista [fuente])):
            # Si en la lista del v�rtice especificado se encuentra el v�rtice de destino retorno el peso del arco de los dos
            si  self .lista [fuente] [i] [ 0 ] == destino:
                return  self .lista [fuente] [i] [ 1 ]
        # Retorno cero por defecto
        devolver  0
