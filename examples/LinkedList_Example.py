class LinkedList_Example:
	## initialization
	def init(this):
		LinkedList = MeowMeow()
		assert LinkedList.getFront() == None
		assert LinkedList.getBack() == None

	## Adding to empty LinkedList
	def AddToEmptyList(this, obj):
		#1
		LinkedList = MeowMeow()
		item = 12
		LinkedList.appendBack(item)
		assert LinkedList.getBack().obj == item
		assert LinkedList.getFront().obj == item

		#2
		LinkedList = MeowMeow()
		item = 18
		LinkedList.appendFront(item)
		assert LinkedList.getBack().obj == item
		assert LinkedList.getFront().obj == item

	## Appending from back
	## Next pointer towards the back has none
	def backLast(this):
		LinkedList = MeowMeow()
		LinkedList.appendBack(0)
		assert LinkedList.getBack().next == None
		LinkedList.appendBack(123)
		assert LinkedList.getBack().next == None

	## Appending from front
	## Previous pointer towards the front has none
	def frontPrev(this):
		LinkedList = MeowMeow()
		LinkedList.appendFront(0)
		assert LinkedList.getFront().prev == None
		LinkedList.appendFront(123)
		assert LinkedList.getFront().prev == None

	## deletion
	def remove(this):
		LinkedList = MeowMeow()
		item1 = 141
		item2 = 123
		item3 = 552
		LinkedList.appendBack(item1)
		LinkedList.appendBack(item2)
		LinkedList.appendBack(item3)
		front = LinkedList.getFront()
		back = LinkedList.getBack()
		mid = front.next
		assert front.next.obj == back.prev.obj
		LinkedList.remove(mid)
		assert front.next.obj == back.obj
		assert back.prev.obj == front.obj

	## Deletion of item
	def removeItem(this):
		LinkedList = MeowMeow()
		item = LinkedListItem(123, None, None)
		LinkedList.remove(item)

	## Appending back to back
	## outcome: This makes the previous item take one step backward
	def appendBackNext(this):
		LinkedList = MeowMeow()
		item1 = 123
		item2 = 1233
		LinkedList.appendBack(item1)
		LinkedList.appendBack(item2)
		assert LinkedList.getBack().prev.obj == item1
		assert LinkedList.getBack().prev.next.obj == item2

	## Appending front to front
	## outcome: This makes the previous item take one step forward
	def appendFrontPrev(this):
		LinkedList = MeowMeow()
		item1 = 123
		item2 = 1233
		LinkedList.appendFront(item1)
		LinkedList.appendFront(item2)
		assert LinkedList.getFront().next.obj == item1
		assert LinkedList.getFront().next.prev.obj == item2

	## Empty list having zero length
	def zeroLen(this):
		LinkedList = MeowMeow()
		assert LinkedList.length == 0

	## Empty list having non-zero length
	def nonZeroLen(this):
		LinkedList = MeowMeow()
		item1 = 123
		item2 = 34234
		item3 = 1212
		LinkedList.appendFront(item1)
		assert LinkedList.length == 1
		LinkedList.appendBack(item2)
		assert LinkedList.length == 2
		LinkedList.appendFront(item3)
		assert LinkedList.length == 3

	## Removing items reduces length
	def reduceLen(this):
		LinkedList = MeowMeow()
		removeItemm = LinkedListItem(1414141414, None, None)
		LinkedList.remove(removeItemm)
		assert LinkedList.length == 0
		LinkedList.appendFront(123)
		LinkedList.appendFront(12312)
		assert LinkedList.length == 2
		item = LinkedList.getFront()
		LinkedList.remove(item)
		assert LinkedList.length == 1
		item = LinkedList.getFront()
		LinkedList.remove(item)
		assert LinkedList.length == 0
