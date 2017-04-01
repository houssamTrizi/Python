# -*-coding:Latin-1 -*

class RevStr(str):

	def __iter__(self):

		return ItRevStr(self)

class ItRevStr:

	def __init__(self, chaine_a_parcourir):

		self.chaine=chaine_a_parcourir
		self.position =len(chaine_a_parcourir)

	def next(self):

		if self.position==0:
			raise StopIteration
		self.position-=1
		return self.chaine[self.position]

if __name__=="__main__":

	chaine="bonjour"
	ma_chaine=RevStr(chaine)
	print ma_chaine
	for lettre in ma_chaine:
		print lettre


