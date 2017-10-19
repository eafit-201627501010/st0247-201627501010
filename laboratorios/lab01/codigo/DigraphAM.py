import numpy

   # @clase digraphAl
   # Descripcion: implementacion de grafo con matrices.
   # @author Jacobo Henao - David Sanchez Arboleda - Estefania Zapata
   # @version 1.0


class digraphAM:

    def __init__(self,size):
        self.size = size
        self.matriz = numpy.zeros(shape=(size+1,size+1))


    def add_arc(self,source,destination,weight=1):
        self.matriz[source,destination]=weight


    def get_successors(self,vertex):
    	#Crear una lista
        successors=[]
       
        for i in range(self.size+1):
        	
            if self.matriz[vertex,i] != 0:
            	#Agrego el vertice con el que se encontro el arco a la lista
                successors.append (i)
        #retorno la lista
        return successors


    def get_weight(self,source,destination):
        return self.matriz[source][destination]
