# -*-coding:Latin-1 -*

import os

def chercher_lettre(lettre,mot):
	liste=list(mot)
	n=liste.count(lettre)
	liste_indice=[]
	while n!= 0:
		liste_indice.append(liste.index(lettre))
		liste.remove(lettre)
		n-=1
	return liste_indice


