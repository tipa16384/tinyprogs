class DnaPolygon:
	def __init__(self):
		self.points = []
		self.brush = DnaBrush()
		origin = DnaPoint()
		for i in range(Settings.ActivePointsPerPolygonMin):
			point = DnaPoint()
			point.X = min(max(0,origin.X+Tools.GetRandomNumber(-3, 3)),Tools.MaxWidth-1)
			point.Y = min(max(0,origin.Y+Tools.GetRandomNumber(-3, 3)),Tools.MaxHeight-1)
			self.points.append(point)

	def clone(self):
		return deepcopy(self)

	def mutate(self,drawing):
		if Tools.WillMutate(Settings.ActiveAddPointMutationRate):
			self.addPoint(drawing);

		if Tools.WillMutate(Settings.ActiveRemovePointMutationRate):
			self.removePoint(drawing);
		
		self.brush.mutate(drawing)
		for p in self.points:
			p.mutate(drawing)

	def removePoint(self,drawing):
		if len(self.points) > Settings.ActivePointsPerPolygonMin:
			if drawing.pointCount > Settings.ActivePointsMin:
				self.points.remove(random.choice(self.points))
				drawing.setDirty()

	def addPoint(self,drawing):
		if len(self.points) < Settings.ActivePointsPerPolygonMax:
			if drawing.pointCount < Settings.ActivePointsMax:
				newPoint = DnaPoint()
				index = random.randint(1,len(self.points)-1)
				prev = self.points[index-1]
				next = self.points[index]
				newPoint.x = (prev.x+next.x)/2
				newPoint.y = (prev.y+next.y)/2
				self.points.insert(index,newPoint)
				drawing.setDirty()

