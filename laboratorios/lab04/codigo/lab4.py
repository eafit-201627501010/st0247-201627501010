#   @clase lab04   
#   @author Jacobo Henao / David Sánchez / Estefania Zapata


import math


def primerpunto(grafo,inicio):
    vis = [False]*(grafo.size+1)
    sol = [0]*(grafo.size+2)
    index = 0
    act = inicio
    close = -1
    close_weight = math.inf
    vis[act] = True
    successors=grafo.get_successors(act)

    for i in successors:
        if grafo.get_weight(act,i) < close_weight and i != act and not vis[i]:
            close = i
            close_weight = grafo.get_weight(act,i)
    index = index + 1
    act = close
    sol[index] = act

    while index < grafo.size:
        close = -1
        close_weight = math.inf
        vis[act] = True

        successors = grafo.get_successors(act)

        for i in successors:
            if grafo.get_weight(act,i) < close_weight and i != act and not vis[i]:
                close = i
                close_weight = grafo.get_weight(act, i)
        index = index + 1
        act = close
        sol [index] = act

    sol[index] = inicio
    return sol