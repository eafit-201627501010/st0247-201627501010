import numpy

  #  @class digraphAl
  #  Descripcion: implementacion  grafo  matrices.
  #  @author David Sanchez Arboleda  - Estefania Zapata
  #  @version 1.0


clase  digraphAM :

    def  __init__ ( auto , tama�o ):
        auto . tama�o = tama�o
       
        self .matriz = numpy.zeros ( forma = (tama�o + 1 , tama�o + 1 ))


    def  add_arc ( self , source , destination , weight = 1 ):
    	
        self .matriz [fuente, destino] = peso


    def  get_successors ( self , v�rtice ):
    	# Creo una lista
        sucesores = []
        # Recorre  los v�rtices de la fila cero
        para i en el  rango ( auto. tama�o + 1 ):
        	# Si el v�rtice especificado tiene un peso diferente de 0 con el v�rtice de la fila significa que hay un arco entre dichos
            si  self .matriz [v�rtice, i] ! =  0 :
            	# AgregAR el v�rtice con que se encuentra el arco a la lista
                successors.append (i)
        # retornAR lista
        retorno sucesores


    def  get_weight ( self , source , destination ):
    	# RetornAR  peso que se encuentra en la posici�n de la matriz dada por LOS v�rtices
        return  self .matriz [fuente] [destino]