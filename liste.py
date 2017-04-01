# -*-coding:Latin-1 -*
from threading import Thread
import sys
import random
import time
class afficheur(Thread):

	def __init__(self,l):
		Thread.__init__(self)
		self.lettre=l
	def run(self):


		for i in range(0,19):
			sys.stdout.write(self.lettre)
			sys.stdout.flush()
			attente=0.2
			attente=attente+random.randint(1,60)/100
			time.sleep(attente)

if __name__=='__main__':
	thread_1=afficheur('*')
	thread_2=afficheur('_')
	thread_1.start()
	thread_2.start()



