# -*-coding:Latin-1 -*
class DictionnaireOrdonne:

	def __init__(self, base={},**donnees):

		self._cles=[]
		self._valeurs=[]

		if type(base) not in (dict, DictionnaireOrdonne):
			raise TypeError("le type attendu est un dictionnaire usuel ou ordonné")

		for cle in base:
			self[cle]=base[cle]

		for cle in donnees:
			self[cle]=donnees[cle]

	def __setitem__(self, cle, valeur):

		if cle in self._cles:
			indice= self._cles.index(cle)
			self._valeurs[indice]=valeur
		else:
			self._cles.append(cle)
			self._valeurs.append(valeur)
	def __delitem__(self, cle):

		if cle in self._cles:
			indice= self._cles.index()
			del self._cles[indice]
			del self._valeurs[indice]
		else:
			raise KeyError("le dictionnaire ne contient pa cette cle")
	def __getitem__(self,cle):
		if cle not in self._cles:
			raise KeyError("le dictionnaire ne contient pas la cle {}".format(cle))
		else:
			indice=self._cles.index(cle)
			return self._valeurs[indice]
	def __contains__(self,cle):
		return cle in self._cles

	def __len__(self):
		return len(self._cles)
	def __repr__(self):

		chaine="{"
		premier_passage=True
		for cle,elt in self.items():
			if not premier_passage:
				chaine+=","
			else:
				premier_passage=False
				chaine+=repr(cle)+": "+repr(elt)
		chaine+="}"
		return chaine
	def keys(self):
		return list(self._cles)

	def values(self):
		return list(self._valeurs)

	def items(self):
		for i,elt in enumerate(self._cles):
			valeur=self._valeurs[i]
			yield (elt,valeur)

	def sort(self):
		cle_triees=sorted(self._cles)
		valeurs=[]

		if elt in cle_triees:
			valeur=self[elt]
			valeurs.append(valeur)

		self._cles=cle_triees
		self._valeurs=valeurs
	def __iter__(self):
		return iter(self._cles)

	def reverse(self):

		cles=[]
		valeurs=[]

		for elt,valeur in self.items():

			cles.insert(0,elt)
			valeurs.insert(0,valeur)

		self._cles=cles
		self._valeurs=valeurs
	def __add__(self,d):

		if type(self) is not type(d):
			raise TypeError("deux types différent")

		else:
			nouv=DictionnaireOrdonne()
			for i,elt in self.items():
				nouv[i]=elt
			for i,elt in d.items():
				nouv[i]=elt
			return nouv






