import Graph
import vertices
import math

Graph = Graph.Graph()
Graph.create_graph()

vertices= vertices.vertices()
vertices.hash_coor()
vertices.hash_id()


#Implementacion del Algoritmo de Dijkstra en Python (Tomado de Wikipedia)

def dijsktra(graph, initial, end):
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = list(graph.grafo[current_node].keys())
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.grafo[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
                    
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
        
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
        path = path[::-1]
    return path

def distancia(recorrido):
    distancia=0

    for i in range(len(recorrido)-1):
        distancia+=Graph.Graph[recorrido[i]][recorrido[i+1]]

    return distancia

def recorrido2(inicial,coordenadas):
    hash1=vertices.hash_coor
    temp=hash1[inicial[0],inicial[1]]
    recorrido=[]

    while coordenadas:

        inicial_id=hash1[inicial[0],inicial[1]]
        proximo=coordenadas.pop()
        proximo_id=hash1[proximo[0],proximo[1]]

        diji=dijsktra(Graph,inicial_id,proximo_id)
        recorrido+=diji[:len(diji)-1]

        inicial=proximo

    inicial_id=hash1[inicial[0],inicial[1]]
    diji=dijsktra(Graph,inicial_id,temp)
    recorrido+=diji

    return recorrido
