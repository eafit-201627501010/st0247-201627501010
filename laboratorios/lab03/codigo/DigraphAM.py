import numpy

  #  @class digraphAl
  #  Descripcion: implementacion  grafo  matrices.
  #  @author David Sanchez Arboleda  - Estefania Zapata
  #  @version 1.0


clase  digraphAM :

    def  __init__ ( auto , tamaño ):
        auto . tamaño = tamaño
       
        self .matriz = numpy.zeros ( forma = (tamaño + 1 , tamaño + 1 ))


    def  add_arc ( self , source , destination , weight = 1 ):
    	
        self .matriz [fuente, destino] = peso


    def  get_successors ( self , vértice ):
    	# Creo una lista
        sucesores = []
        # Recorre  los vértices de la fila cero
        para i en el  rango ( auto. tamaño + 1 ):
        	# Si el vértice especificado tiene un peso diferente de 0 con el vértice de la fila significa que hay un arco entre dichos
            si  self .matriz [vértice, i] ! =  0 :
            	# AgregAR el vértice con que se encuentra el arco a la lista
                successors.append (i)
        # retornAR lista
        retorno sucesores


    def  get_weight ( self , source , destination ):
    	# RetornAR  peso que se encuentra en la posición de la matriz dada por LOS vértices
        return  self .matriz [fuente] [destino]