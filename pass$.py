# -*-coding:Latin-1 -*# -*-coding:Latin-1 -*
from getpass import getpass
import signal
import os
def fermer(signal, frame):

	print("le programme se fermera")
	os._exit(0)

signal.signal(signal.SIGINT,fermer)

m=getpass("tapez votre pass ici\n")
print(m)
os.system("pause")




