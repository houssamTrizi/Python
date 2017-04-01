# -*-coding:Latin-1 -*

class Personne(object):
	"""classe définissant un modèle de personne"""
	nbre_personne=0
	def __init__(self,nom):
		"""constructeur de l'objet personne"""
		self._nom=nom
		Personne.nbre_personne+=1
	def __getitem__(self,index):
		"""méthode modifiant le comportement du l'operateur [] sur personne:"""
		return self._nom

	def _get_nom(self):
		"""méthode donnant accés à l'attribue nom"""
		print("accés au nom de mr {}".format(self._nom))
		return self._nom
	def _set_nom(self,nom):
		"""méthode permettant de modifier l'attribut nom"""
		print("modification du nom de Mr {}".format(self._nom))
		self._nom=nom
	def affich_personne(self):
		"""méthode permettant d'afficher une personne par son nom"""
		print("cette personne a pour nom: {}".format(self._nom))
	def affich_objet(cls):
		"""méthode de class affichant le nombre d'objets crées"""
		print("nous avons défini {} personne".format(cls.nbre_personne))
	def __str__(self):
		"""modification de la méthode speciale pour transformer notre objet ne chaine de caractères"""
		return "notre objet personne a pour nom : {}".format(self._nom)
	def affich():
		"""méthode static affichant une description de la class"""
		print("ceci est la class personne")
	nom=property(_get_nom,_set_nom)
	affich_objet=classmethod(affich_objet)
	affich=staticmethod(affich)

if __name__=="__main__":

	personne=Personne("houssam")


	print(personne[0])
	personne[0]="trizi"
	print(personne[0])


