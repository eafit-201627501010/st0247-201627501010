"""
    @clase laboratorio2
    Descripcion: Punto 2 laboratorio 2
    @author David Sanchez Arboleda y Estefania Zapata
    @version 1.0
"""

def n_reinas():
	size=input("Grandor: ")
	pizarra=[]
	for i in range(int(size)):
		print ("fila: ",i)
		pizarra.append(input())
	restriccion=[1459]*int(size)
	for i in range(len(tablero)):
		for n in range(len(pizarra[i])):
			if pizarra[i][n]=="*":
				restriccion[i]=n
	pizarra = [None]*int(size)
	return len(n_reinas_aux([],0,pizarra,restriccion)) 


def puedo_poner_reina(r,tablero):
	for i in range(r):
		if abs(pizarra[i]-pizarra[r])==r-i or pizarra[i]==pizarra[r]:
			return False
	return True

#Metodo que comprueba la combinacion de las reinas en la pizarra es valida
def n_reinas_aux(r,n,pizarra,restriccion):
	if n>=len(pizarra):
		r.append(pizarra)
	else:
		for i in range(len(pizarra)):
			if n<(len(restriccion)):
				if i==restriccion[n]:
					continue
			pizarra[n]=i
			if puedo_poner_reina(n,pizarra):
				n_reinas_aux(r,n+1,pizarra,restriccion)
	return r