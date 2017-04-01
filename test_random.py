# -*-coding:Latin-1 -*
import random
import unittest
class RandomTest(unittest.TestCase):
	"""test case utilisé pour tester les fonctions du module Random"""
	def setUp(self):
		self.liste=range(10)
	def test_choice(self):
		"""test de la fonction choice du module random"""
		choice=random.choice(self.liste)
		self.assertIn('choice',self.liste)
	def test_shuffle(self):
		"""test de la fonction shuffle du module random"""
		random.shuffle(self.liste)
		self.liste.sort()
		self.assertEqual(self.liste,range(10))
	def test_sample(self):
		"""test de la fonction sample du module random"""
		extrait=random.sample(self.liste,5)
		for element in extrait:
			self.assertIn(element,self.liste)
		with self.assertRaises(ValueError):
			random.sample(self.liste,20)
