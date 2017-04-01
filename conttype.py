# -*-coding:Latin-1 -*
def controler_type(*a_args,**a_kwargs):

	def decorateur(fonction):

		def fonction_mod(*args,**kwargs):
			if len(a_args)!=len(args):

				raise TypeError("le nombre d'argument passé ne correspond pa a la fonction0")

			for i,elt in enumerate(args):

				if a_args[i] is not type(elt):
					raise TypeError("l'argument {0} ne correspond pas au type {1}".format(i,a_args[i]))

			for cle in kwargs:
				if cle not in a_kwargs:
					raise TypeError("l'argument {} n'a aucun type précisé".format(__repr__(cle)))

				if a_kwargs[cle] not in type(kwargs[cle]):

					raise TypeError("l'agument {0} n'est pas de type{1}".format(__repr__(cle),a_kwargs[cle]))

			return fonction(*args,**kwargs)
		return fonction_mod
	return decorateur

@controler_type(i=int)
def aff(i=1):
	print(str(i)+"  ")


if __name__=="__main__":
	aff(i=1)
