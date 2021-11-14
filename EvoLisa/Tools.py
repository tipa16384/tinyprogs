import random

MaxPolygons = 250
MaxWidth = 200
MaxHeight = 200

def GetRandomNumber(a,b):
	return random.randint(a,b)

def WillMutate(mutationRate):
	return GetRandomNumber(0,mutationRate) == 1

