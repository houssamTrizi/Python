# -*-coding:Latin-1 -*
class Duree(object):

	def __init__(self,min=0,sec=0):

		self.min=min
		self.sec=sec

	def __str__(self):

		return "{0:02}:{1:02}".format(self.min,self.sec)
	def __add__(self,i):

		nouv_duree=Duree()
		nouv_duree.min=self.min
		nouv_duree.sec=self.sec
		nouv_duree.sec+=i
		if nouv_duree.sec>=60:
			nouv_duree.min+=nouv_duree.sec//60
			nouv_duree.sec=nouv_duree.sec%60
		return nouv_duree

if __name__=="__main__":

	d1=Duree(1,2)
	print(d1)
	d2=58
	print(d1+d2)

