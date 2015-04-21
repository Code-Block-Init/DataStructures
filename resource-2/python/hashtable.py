class hashtable(SearchableContainer):

	def __init__(self):
		super(hashtable, self).__init__()

	def __len__(self):
		pass
	__len__ = abstractmethod(__len__)

	def getLoadFactor(self):
		return self.count / len(self)

	loadFactor = property(
		fget = lambda self: self.getLoadFactor())
