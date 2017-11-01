"""
@class Vertices
Build the graphs Hashs.
by: Jacobo Henao, David Sanchez, Estefania Zapata
@version 1
"""

class vertices:
    def __init__(self):
        #creo los hash
        self.hash_id={}
        self.hash_coor={}
        self.hash_name={}
        
    #La explicacion del codigo es similar a la de "Graph.py"
    def hash_name(self):
        with open("vertices.txt", encoding="utf-8") as file:
            for line in file:
               a = line.split(" ")
               #La key del hash es la id
               self.hash_name[a[3][:-1]]=a[0]

    def hash_coor(self):
        with open("vertices.txt", encoding = "utf-8") as file:
            for line in file:
                g = line.split(" ")
                #Mapea la tupla de coordenadas con la id.
                self.hash_coor[(g[1],g[2])]=a[0]

               
    def hash_id(self):
        with open("vertices.txt", encoding = "utf-8") as file:
            for line in f:
                g = line.split(" ")
                self.hash_id[a[0]] = (a[1],a[2])
