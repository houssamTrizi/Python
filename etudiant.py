# -*-coding:Latin-1 -*
class Etudiant(object):

	def __init__(self,nom,age,moyenne):

		self.nom=nom
		self.age=age
		self.moyenne=moyenne


	def __repr__(self):

		return "etudiant {0} agé de {1} a eu {2} ".format(self.nom,self.age,self.moyenne)



if __name__=="__main__":

	etudiants=[Etudiant("houssam",26,18),Etudiant("hamza",23,15),Etudiant("ouardi",24,17)]
	etudiants_tri=sorted(etudiants,key= lambda etudiant: etudiant.moyenne, reverse=True)
	print(etudiants_tri)
