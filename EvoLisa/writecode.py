vars = """def getAddPolygonMutationRate():
	return addPolygonMutationRate

def setAddPolygonMutationRate(value):
	addPolygonMutationRate = value

def getAlphaMutationRate():
	return alphaMutationRate

def setAlphaMutationRate(value):
	alphaMutationRate = value

def getAlphaRangeMax():
	return alphaRangeMax

def setAlphaRangeMax(value):
	alphaRangeMax = value
	alphaRangeMin = min(alphaRangeMin,value)

def getAlphaRangeMin():
	return alphaRangeMin

def setAlphaRangeMin(value):
	alphaRangeMin = value
	alphaRangeMax = max(alphaRangeMax,value)

def getBlueMutationRate():
	return blueMutationRate

def setBlueMutationRate(value):
	blueMutationRate = value

def getBlueRangeMax():
	return blueRangeMax

def setBlueRangeMax(value):
	blueRangeMax = value
	blueRangeMin = min(blueRangeMin,value)

def getBlueRangeMin():
	return blueRangeMin

def setBlueRangeMin(value):
	blueRangeMin = value
	blueRangeMax = max(blueRangeMax,value)

def getGreenMutationRate():
	return greenMutationRate

def setGreenMutationRate(value):
	greenMutationRate = value

def getGreenRangeMax():
	return greenRangeMax

def setGreenRangeMax(value):
	greenRangeMax = value
	greenRangeMin = min(greenRangeMin,value)

def getGreenRangeMin():
	return greenRangeMin

def setGreenRangeMin(value):
	greenRangeMin = value
	greenRangeMax = max(greenRangeMax,value)

def getMovePointMaxMutationRate():
	return movePointMaxMutationRate

def setMovePointMaxMutationRate(value):
	movePointMaxMutationRate = value

def getMovePointMidMutationRate():
	return movePointMidMutationRate

def setMovePointMidMutationRate(value):
	movePointMidMutationRate = value

def getMovePointMinMutationRate():
	return movePointMinMutationRate

def setMovePointMinMutationRate(value):
	movePointMinMutationRate = value

def getMovePointRangeMid():
	return movePointRangeMid

def setMovePointRangeMid(value):
	movePointRangeMid = value
	movePointRangeMin = min(movePointRangeMin,value)

def getMovePointRangeMin():
	return movePointRangeMin

def setMovePointRangeMin(value):
	movePointRangeMin = value
	movePointRangeMid = max(movePointRangeMid,value)

def getMovePolygonMutationRate():
	return movePolygonMutationRate

def setMovePolygonMutationRate(value):
	movePolygonMutationRate = value

def getPointsMax():
	return pointsMax

def setPointsMax(value):
	pointsMax = value
	pointsMin = min(pointsMin,value)

def getPointsMin():
	return pointsMin

def setPointsMin(value):
	pointsMin = value
	pointsMax = max(pointsMax,value)

def getPointsPerPolygonMax():
	return pointsPerPolygonMax

def setPointsPerPolygonMax(value):
	pointsPerPolygonMax = value
	pointsPerPolygonMin = min(pointsPerPolygonMin,value)

def getPointsPerPolygonMin():
	return pointsPerPolygonMin

def setPointsPerPolygonMin(value):
	pointsPerPolygonMin = value
	pointsPerPolygonMax = max(pointsPerPolygonMax,value)

def getPolygonsMax():
	return polygonsMax

def setPolygonsMax(value):
	polygonsMax = value
	polygonsMin = min(polygonsMin,value)

def getPolygonsMin():
	return polygonsMin

def setPolygonsMin(value):
	polygonsMin = value
	polygonsMax = max(polygonsMax,value)

def getRedMutationRate():
	return redMutationRate

def setRedMutationRate(value):
	redMutationRate = value

def getRedRangeMax():
	return redRangeMax

def setRedRangeMax(value):
	redRangeMax = value
	redRangeMin = min(redRangeMin,value)

def getRedRangeMin():
	return redRangeMin

def setRedRangeMin(value):
	redRangeMin = value
	redRangeMax = max(redRangeMax,value)

def getRemovePointMutationRate():
	return removePointMutationRate

def setRemovePointMutationRate(value):
	removePointMutationRate = value

def getRemovePolygonMutationRate():
	return removePolygonMutationRate

def setRemovePolygonMutationRate(value):
	removePolygonMutationRate = value

# Ranges

def Activate():
    activeAddPolygonMutationRate = addPolygonMutationRate
    activeRemovePolygonMutationRate = removePolygonMutationRate
    activeMovePolygonMutationRate = movePolygonMutationRate
    
    activeAddPointMutationRate = addPointMutationRate
    activeRemovePointMutationRate = removePointMutationRate
    activeMovePointMaxMutationRate = movePointMaxMutationRate
    activeMovePointMidMutationRate = movePointMidMutationRate
    activeMovePointMinMutationRate = movePointMinMutationRate
    
    activeRedMutationRate = redMutationRate
    activeGreenMutationRate = greenMutationRate
    activeBlueMutationRate = blueMutationRate
    activeAlphaMutationRate = alphaMutationRate
    
    #Limits / constraints
    activeRedRangeMin = redRangeMin
    activeRedRangeMax = redRangeMax
    activeGreenRangeMin = greenRangeMin
    activeGreenRangeMax = greenRangeMax
    activeBlueRangeMin = blueRangeMin
    activeBlueRangeMax = blueRangeMax
    activeAlphaRangeMin = alphaRangeMin
    activeAlphaRangeMax = alphaRangeMax
    
    activePolygonsMax = polygonsMax
    activePolygonsMin = polygonsMin
    
    activePointsPerPolygonMax = pointsPerPolygonMax
    activePointsPerPolygonMin = pointsPerPolygonMin
    
    activePointsMax = pointsMax
    activePointsMin = pointsMin
    
    activeMovePointRangeMid = movePointRangeMid
    activeMovePointRangeMin = movePointRangeMin

def Discard():
    addPolygonMutationRate = activeAddPolygonMutationRate
    removePolygonMutationRate = activeRemovePolygonMutationRate
    movePolygonMutationRate = activeMovePolygonMutationRate
    
    addPointMutationRate = activeAddPointMutationRate
    removePointMutationRate = activeRemovePointMutationRate
    movePointMaxMutationRate = activeMovePointMaxMutationRate
    movePointMidMutationRate = activeMovePointMidMutationRate
    movePointMinMutationRate = activeMovePointMinMutationRate
    
    redMutationRate = activeRedMutationRate
    greenMutationRate = activeGreenMutationRate
    blueMutationRate = activeBlueMutationRate
    alphaMutationRate = activeAlphaMutationRate
    
    #Limits / constraints
    redRangeMin = activeRedRangeMin
    redRangeMax = activeRedRangeMax
    greenRangeMin = activeGreenRangeMin
    greenRangeMax = activeGreenRangeMax
    blueRangeMin = activeBlueRangeMin
    blueRangeMax = activeBlueRangeMax
    alphaRangeMin = activeAlphaRangeMin
    alphaRangeMax = activeAlphaRangeMax
    
    polygonsMax = activePolygonsMax
    polygonsMin = activePolygonsMin
    
    pointsPerPolygonMax = activePointsPerPolygonMax
    pointsPerPolygonMin = activePointsPerPolygonMin
    
    pointsMax = activePointsMax
    pointsMin = activePointsMin
    
    movePointRangeMid = activeMovePointRangeMid
    movePointRangeMin = activeMovePointRangeMin

def Reset():
    activeAddPolygonMutationRate = 700
    activeRemovePolygonMutationRate = 1500
    activeMovePolygonMutationRate = 700
    
    activeAddPointMutationRate = 1500
    activeRemovePointMutationRate = 1500
    activeMovePointMaxMutationRate = 1500
    activeMovePointMidMutationRate = 1500
    activeMovePointMinMutationRate = 1500
    
    activeRedMutationRate = 1500
    activeGreenMutationRate = 1500
    activeBlueMutationRate = 1500
    activeAlphaMutationRate = 1500
    
    #Limits / constraints
    activeRedRangeMin = 0
    activeRedRangeMax = 255
    activeGreenRangeMin = 0
    activeGreenRangeMax = 255
    activeBlueRangeMin = 0
    activeBlueRangeMax = 255
    activeAlphaRangeMin = 30
    activeAlphaRangeMax = 60
    
    activePolygonsMax = 255
    activePolygonsMin = 0
    
    activePointsPerPolygonMax = 10
    activePointsPerPolygonMin = 3
    
    activePointsMax = 1500
    activePointsMin = 0
    
    activeMovePointRangeMid = 20
    activeMovePointRangeMin = 3
    
    discard()
"""

for l in vars.split('\n'):
	w = l.strip().split()
	if len(w) >= 3 and w[1] == '=':
		i = l.index(w[0])
		print "%sglobal %s" % (l[:i],w[0])
	print l

