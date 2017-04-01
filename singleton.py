# -*-coding:Latin-1 -*

def singleton(classe_definie):
	instances={}
	def get_instance(nom):

		if classe_definie not in instances:
			instances[classe_definie]=classe_definie(nom)
		return instances[classe_definie]
	return get_instance

@singleton
class test():
	def __init__(self,nom):
		self.nom=nom
	def __repr__(self):
		return "le nom est:{}".format(self.nom)

if __name__=="__main__":
	a=test("houssam")
	del a

	b=test("tr")
	print(b)


