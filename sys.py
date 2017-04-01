# -*-coding:Latin-1 -*
import signal
import os

def fermer_prog(signal,frame):

	print("le programme se fermera")
	os._exit(0)
signal.signal(signal.SIGINT,fermer_prog)

print("le programme va boucler")
while True:
	continue


