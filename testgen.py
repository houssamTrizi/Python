# -*-coding:Latin-1 -*

def gener(a,b):


	a+=1
	while a<b:
		val=(yield a)
		if val is not None:
			a=val
		a+=1

if __name__=="__main__":

	for i in gener(0,4):
		print(i)
