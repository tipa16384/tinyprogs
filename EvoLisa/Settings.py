activeAddPointMutationRate = 1000
activeAddPolygonMutationRate = 700
activeAlphaMutationRate = 1000
activeAlphaRangeMax = 200
activeAlphaRangeMin = 90
activeBlueMutationRate = 1000
activeBlueRangeMax = 255
activeBlueRangeMin = 0
activeGreenMutationRate = 1000
activeGreenRangeMax = 255
activeGreenRangeMin = 0
activeMovePointMaxMutationRate = 1000
activeMovePointMidMutationRate = 1000
activeMovePointMinMutationRate = 1000

activeMovePointRangeMid = 20
activeMovePointRangeMin = 3
activeMovePolygonMutationRate = 700
activePointsMax = 1000
activePointsMin = 0
activePointsPerPolygonMax = 6
activePointsPerPolygonMin = 6
activePolygonsMax = 50
activePolygonsMin = 50
activeRedMutationRate = 1000
activeRedRangeMax = 255
activeRedRangeMin = 0
activeRemovePointMutationRate = 1000
activeRemovePolygonMutationRate = 1000

# Mutation rates
addPolygonMutationRate = 700
alphaMutationRate = 1000
alphaRangeMax = 60
alphaRangeMin = 30
blueMutationRate = 1000
blueRangeMax = 255
blueRangeMin = 0
greenMutationRate = 1000
greenRangeMax = 255
greenRangeMin = 0
movePointMaxMutationRate = 1000
movePointMidMutationRate = 1000
movePointMinMutationRate = 1000
movePointRangeMid = 20
movePointRangeMin = 3
movePolygonMutationRate = 700
pointsMax = 1000
pointsMin = 0
pointsPerPolygonMax = 10
pointsPerPolygonMin = 3
polygonsMax = 255
polygonsMin = 0
redMutationRate = 1000
redRangeMax = 255
redRangeMin = 0
removePointMutationRate = 1000
removePolygonMutationRate = 1000

def getAddPolygonMutationRate():
	return addPolygonMutationRate

def setAddPolygonMutationRate(value):
	global addPolygonMutationRate
	addPolygonMutationRate = value

def getAlphaMutationRate():
	return alphaMutationRate

def setAlphaMutationRate(value):
	global alphaMutationRate
	alphaMutationRate = value

def getAlphaRangeMax():
	return alphaRangeMax

def setAlphaRangeMax(value):
	global alphaRangeMax
	alphaRangeMax = value
	global alphaRangeMin
	alphaRangeMin = min(alphaRangeMin,value)

def getAlphaRangeMin():
	return alphaRangeMin

def setAlphaRangeMin(value):
	global alphaRangeMin
	alphaRangeMin = value
	global alphaRangeMax
	alphaRangeMax = max(alphaRangeMax,value)

def getBlueMutationRate():
	return blueMutationRate

def setBlueMutationRate(value):
	global blueMutationRate
	blueMutationRate = value

def getBlueRangeMax():
	return blueRangeMax

def setBlueRangeMax(value):
	global blueRangeMax
	blueRangeMax = value
	global blueRangeMin
	blueRangeMin = min(blueRangeMin,value)

def getBlueRangeMin():
	return blueRangeMin

def setBlueRangeMin(value):
	global blueRangeMin
	blueRangeMin = value
	global blueRangeMax
	blueRangeMax = max(blueRangeMax,value)

def getGreenMutationRate():
	return greenMutationRate

def setGreenMutationRate(value):
	global greenMutationRate
	greenMutationRate = value

def getGreenRangeMax():
	return greenRangeMax

def setGreenRangeMax(value):
	global greenRangeMax
	greenRangeMax = value
	global greenRangeMin
	greenRangeMin = min(greenRangeMin,value)

def getGreenRangeMin():
	return greenRangeMin

def setGreenRangeMin(value):
	global greenRangeMin
	greenRangeMin = value
	global greenRangeMax
	greenRangeMax = max(greenRangeMax,value)

def getMovePointMaxMutationRate():
	return movePointMaxMutationRate

def setMovePointMaxMutationRate(value):
	global movePointMaxMutationRate
	movePointMaxMutationRate = value

def getMovePointMidMutationRate():
	return movePointMidMutationRate

def setMovePointMidMutationRate(value):
	global movePointMidMutationRate
	movePointMidMutationRate = value

def getMovePointMinMutationRate():
	return movePointMinMutationRate

def setMovePointMinMutationRate(value):
	global movePointMinMutationRate
	movePointMinMutationRate = value

def getMovePointRangeMid():
	return movePointRangeMid

def setMovePointRangeMid(value):
	global movePointRangeMid
	movePointRangeMid = value
	global movePointRangeMin
	movePointRangeMin = min(movePointRangeMin,value)

def getMovePointRangeMin():
	return movePointRangeMin

def setMovePointRangeMin(value):
	global movePointRangeMin
	movePointRangeMin = value
	global movePointRangeMid
	movePointRangeMid = max(movePointRangeMid,value)

def getMovePolygonMutationRate():
	return movePolygonMutationRate

def setMovePolygonMutationRate(value):
	global movePolygonMutationRate
	movePolygonMutationRate = value

def getPointsMax():
	return pointsMax

def setPointsMax(value):
	global pointsMax
	pointsMax = value
	global pointsMin
	pointsMin = min(pointsMin,value)

def getPointsMin():
	return pointsMin

def setPointsMin(value):
	global pointsMin
	pointsMin = value
	global pointsMax
	pointsMax = max(pointsMax,value)

def getPointsPerPolygonMax():
	return pointsPerPolygonMax

def setPointsPerPolygonMax(value):
	global pointsPerPolygonMax
	pointsPerPolygonMax = value
	global pointsPerPolygonMin
	pointsPerPolygonMin = min(pointsPerPolygonMin,value)

def getPointsPerPolygonMin():
	return pointsPerPolygonMin

def setPointsPerPolygonMin(value):
	global pointsPerPolygonMin
	pointsPerPolygonMin = value
	global pointsPerPolygonMax
	pointsPerPolygonMax = max(pointsPerPolygonMax,value)

def getPolygonsMax():
	return polygonsMax

def setPolygonsMax(value):
	global polygonsMax
	polygonsMax = value
	global polygonsMin
	polygonsMin = min(polygonsMin,value)

def getPolygonsMin():
	return polygonsMin

def setPolygonsMin(value):
	global polygonsMin
	polygonsMin = value
	global polygonsMax
	polygonsMax = max(polygonsMax,value)

def getRedMutationRate():
	return redMutationRate

def setRedMutationRate(value):
	global redMutationRate
	redMutationRate = value

def getRedRangeMax():
	return redRangeMax

def setRedRangeMax(value):
	global redRangeMax
	redRangeMax = value
	global redRangeMin
	redRangeMin = min(redRangeMin,value)

def getRedRangeMin():
	return redRangeMin

def setRedRangeMin(value):
	global redRangeMin
	redRangeMin = value
	global redRangeMax
	redRangeMax = max(redRangeMax,value)

def getRemovePointMutationRate():
	return removePointMutationRate

def setRemovePointMutationRate(value):
	global removePointMutationRate
	removePointMutationRate = value

def getRemovePolygonMutationRate():
	return removePolygonMutationRate

def setRemovePolygonMutationRate(value):
	global removePolygonMutationRate
	removePolygonMutationRate = value

# Ranges

def Activate():
    global activeAddPolygonMutationRate
    activeAddPolygonMutationRate = addPolygonMutationRate
    global activeRemovePolygonMutationRate
    activeRemovePolygonMutationRate = removePolygonMutationRate
    global activeMovePolygonMutationRate
    activeMovePolygonMutationRate = movePolygonMutationRate
    
    global activeAddPointMutationRate
    activeAddPointMutationRate = addPointMutationRate
    global activeRemovePointMutationRate
    activeRemovePointMutationRate = removePointMutationRate
    global activeMovePointMaxMutationRate
    activeMovePointMaxMutationRate = movePointMaxMutationRate
    global activeMovePointMidMutationRate
    activeMovePointMidMutationRate = movePointMidMutationRate
    global activeMovePointMinMutationRate
    activeMovePointMinMutationRate = movePointMinMutationRate
    
    global activeRedMutationRate
    activeRedMutationRate = redMutationRate
    global activeGreenMutationRate
    activeGreenMutationRate = greenMutationRate
    global activeBlueMutationRate
    activeBlueMutationRate = blueMutationRate
    global activeAlphaMutationRate
    activeAlphaMutationRate = alphaMutationRate
    
    #Limits / constraints
    global activeRedRangeMin
    activeRedRangeMin = redRangeMin
    global activeRedRangeMax
    activeRedRangeMax = redRangeMax
    global activeGreenRangeMin
    activeGreenRangeMin = greenRangeMin
    global activeGreenRangeMax
    activeGreenRangeMax = greenRangeMax
    global activeBlueRangeMin
    activeBlueRangeMin = blueRangeMin
    global activeBlueRangeMax
    activeBlueRangeMax = blueRangeMax
    global activeAlphaRangeMin
    activeAlphaRangeMin = alphaRangeMin
    global activeAlphaRangeMax
    activeAlphaRangeMax = alphaRangeMax
    
    global activePolygonsMax
    activePolygonsMax = polygonsMax
    global activePolygonsMin
    activePolygonsMin = polygonsMin
    
    global activePointsPerPolygonMax
    activePointsPerPolygonMax = pointsPerPolygonMax
    global activePointsPerPolygonMin
    activePointsPerPolygonMin = pointsPerPolygonMin
    
    global activePointsMax
    activePointsMax = pointsMax
    global activePointsMin
    activePointsMin = pointsMin
    
    global activeMovePointRangeMid
    activeMovePointRangeMid = movePointRangeMid
    global activeMovePointRangeMin
    activeMovePointRangeMin = movePointRangeMin

def Discard():
    global addPolygonMutationRate
    addPolygonMutationRate = activeAddPolygonMutationRate
    global removePolygonMutationRate
    removePolygonMutationRate = activeRemovePolygonMutationRate
    global movePolygonMutationRate
    movePolygonMutationRate = activeMovePolygonMutationRate
    
    global addPointMutationRate
    addPointMutationRate = activeAddPointMutationRate
    global removePointMutationRate
    removePointMutationRate = activeRemovePointMutationRate
    global movePointMaxMutationRate
    movePointMaxMutationRate = activeMovePointMaxMutationRate
    global movePointMidMutationRate
    movePointMidMutationRate = activeMovePointMidMutationRate
    global movePointMinMutationRate
    movePointMinMutationRate = activeMovePointMinMutationRate
    
    global redMutationRate
    redMutationRate = activeRedMutationRate
    global greenMutationRate
    greenMutationRate = activeGreenMutationRate
    global blueMutationRate
    blueMutationRate = activeBlueMutationRate
    global alphaMutationRate
    alphaMutationRate = activeAlphaMutationRate
    
    #Limits / constraints
    global redRangeMin
    redRangeMin = activeRedRangeMin
    global redRangeMax
    redRangeMax = activeRedRangeMax
    global greenRangeMin
    greenRangeMin = activeGreenRangeMin
    global greenRangeMax
    greenRangeMax = activeGreenRangeMax
    global blueRangeMin
    blueRangeMin = activeBlueRangeMin
    global blueRangeMax
    blueRangeMax = activeBlueRangeMax
    global alphaRangeMin
    alphaRangeMin = activeAlphaRangeMin
    global alphaRangeMax
    alphaRangeMax = activeAlphaRangeMax
    
    global polygonsMax
    polygonsMax = activePolygonsMax
    global polygonsMin
    polygonsMin = activePolygonsMin
    
    global pointsPerPolygonMax
    pointsPerPolygonMax = activePointsPerPolygonMax
    global pointsPerPolygonMin
    pointsPerPolygonMin = activePointsPerPolygonMin
    
    global pointsMax
    pointsMax = activePointsMax
    global pointsMin
    pointsMin = activePointsMin
    
    global movePointRangeMid
    movePointRangeMid = activeMovePointRangeMid
    global movePointRangeMin
    movePointRangeMin = activeMovePointRangeMin

def Reset():
    global activeAddPolygonMutationRate
    activeAddPolygonMutationRate = 700
    global activeRemovePolygonMutationRate
    activeRemovePolygonMutationRate = 1000
    global activeMovePolygonMutationRate
    activeMovePolygonMutationRate = 700
    
    global activeAddPointMutationRate
    activeAddPointMutationRate = 1000
    global activeRemovePointMutationRate
    activeRemovePointMutationRate = 1000
    global activeMovePointMaxMutationRate
    activeMovePointMaxMutationRate = 1000
    global activeMovePointMidMutationRate
    activeMovePointMidMutationRate = 1000
    global activeMovePointMinMutationRate
    activeMovePointMinMutationRate = 1000
    
    global activeRedMutationRate
    activeRedMutationRate = 1000
    global activeGreenMutationRate
    activeGreenMutationRate = 1000
    global activeBlueMutationRate
    activeBlueMutationRate = 1000
    global activeAlphaMutationRate
    activeAlphaMutationRate = 1000
    
    #Limits / constraints
    global activeRedRangeMin
    activeRedRangeMin = 0
    global activeRedRangeMax
    activeRedRangeMax = 255
    global activeGreenRangeMin
    activeGreenRangeMin = 0
    global activeGreenRangeMax
    activeGreenRangeMax = 255
    global activeBlueRangeMin
    activeBlueRangeMin = 0
    global activeBlueRangeMax
    activeBlueRangeMax = 255
    global activeAlphaRangeMin
    activeAlphaRangeMin = 90
    global activeAlphaRangeMax
    activeAlphaRangeMax = 200
    
    global activePolygonsMax
    activePolygonsMax = 255
    global activePolygonsMin
    activePolygonsMin = 0
    
    global activePointsPerPolygonMax
    activePointsPerPolygonMax = 10
    global activePointsPerPolygonMin
    activePointsPerPolygonMin = 3
    
    global activePointsMax
    activePointsMax = 1000
    global activePointsMin
    activePointsMin = 0
    
    global activeMovePointRangeMid
    activeMovePointRangeMid = 20
    global activeMovePointRangeMin
    activeMovePointRangeMin = 3
    
    discard()
    
    activeMovePointRangeMid = 20
    activeMovePointRangeMin = 3
    
    discard()

