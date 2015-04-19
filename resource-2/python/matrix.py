class matrix(object):

	#initialize
	def __init__(self, numberOfRows, numberOfColumns):
		assert numberOfRows >= 0
		assert numberOfColumns >= 0
		super(matrix, self).__init__()
		self._numberOfRows = numberOfRows
		self._numberOfColumns = numberOfColumns

	# Fetching number of rows
	def getNumberOfRows(self):
		return self._numberOfRows

	numberOfRows = property(
		fget = lambda self: self.getNumberOfRows())

	# Fetching number of columns
	def getNumberOfColumns(self):
		return self._numberOfColumns

	numberOfColumns = property(
		fget = lambda self: self.getNumberOfColumns())
