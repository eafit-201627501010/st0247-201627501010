
   # @clase laboratorio2
   # Descripcion: Punto 1.1 del laboratorio 2
   # @author David Sanchez Arboleda y Estefania Zapata
   # @version 1


def es_valido(pizarra):
	for i in range(len(pizarra)-1):
		for k in range(i+1,len(pizarra)):
			if abs(int(pizarra[i])-int(pizarra[k]))==k-i or pizarra[i]==pizarra[k]:
				return False
	return True

def queens_aux(pre, pos, resultado):
	if len(pos)==0:
		resultado.append(pre)
	for i in range(len(pos)):
		queens_aux(pre+pos[i],pos[:i]+pos[i+1:],resultado)
	return resultado


def queens(n):
	pos=[str(i) for i in range(n)]
	permutaciones=queens_aux("",pos,[])
	cont=0
	for i in range(len(permutaciones)):
		opcion=list(permutaciones[i])
		if es_valido(opcion):
			cont+=1
	return cont