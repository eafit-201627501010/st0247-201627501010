"""
@class Graph

Creates the Graph

by: Jacobo Henao, David Sanchez, Stefania Zapata

@v1
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        #This dictionary is a representation of the graph itself.
        self.Graph = defaultdict(dict)

    def create_graph(self): #Defines the graph-creating function.
        with open ("arcos.txt", encoding="utf-8") as file:
            #Opens the file with the needed information.
            
            for line in file:
            #Splits each line found in file, saving it in an array.
                g = line.split(" ")

                self.Graph[g[0]][g[1]] = float(g[2])                
