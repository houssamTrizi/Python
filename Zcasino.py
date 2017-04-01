# -*-coding:Latin-1 -*
import os
from random import randrange
from math import ceil

argent=1000
continuer_partie=True


print("vous commencez la parie avec  "+str(argent)+" dirhams en main\n")
while continuer_partie:
	nombre_mise=-1

	while nombre_mise<0 or nombre_mise>49:
		nombre_mise=input("saisissez le le nombre mise entre 0 et 49\n")

		try:
			nombre_mise=int(nombre_mise)
		except ValueError:
			print("vous n'avez pas saisi un nombre\n")
			nombre_mise=-1
			continue
		if nombre_mise<0:
			print("vous avez saisi un nombre negatif\n")
		if nombre_mise>49:
			print("le nombre saisi est superieur a 49\n")




	mise=0
	while mise<=0 or mise>argent:
		mise=input("saisissez la somme d'argent a miser\n")
		try:
			mise=int(mise)
		except ValueError:
			print("vous n'avez pas saisi un nombre\n")
			mise=0
			continue
		if mise<0:
			print("vous avez saisi une somme negative\n")
		if mise>argent:
			print("vous n'avez pas cette somme\n")

	numero_gagnant=randrange(50)

	print("la roulette tourne est s'arrete sur  "+str(numero_gagnant)+" .\n")

	if numero_gagnant==nombre_mise:
		print("felicitation votre mise correspond au numéro gagnant\n")
		argent+=mise*3
	if numero_gagnant%2==numero_gagnant%2:
		print("votre nombre mise et le numero gagnant sont de meme couleur vous gagnez  "+str(ceil(mise/2)))
		argent+=ceil(mise/2)
	else:
		print("vous perdez votre somme misee\n")
		argent-=mise

	if argent<=0:
		print("vous etes ruine vous ne pouvez plus continuer\n")
		continuer_partie=False
	else:
		print("vous avez a present "+str(argent)+".")
		quitter=input("voulez vous partir avec cette somme (o/n):\n")
		quitter=str(quitter)

	if quitter=='o' or quitter=='O':
		print("a la prochaine :)\n")
		continuer_partie=False


os.system("pause")









