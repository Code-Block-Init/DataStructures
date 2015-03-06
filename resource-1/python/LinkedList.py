## defining class LinkedListItem
## declaring object
class LinkedListItem(object):
	def __init__(this, obj, prev, next):
		this.prev = prev
		this.next = next
		this.obj = obj

## defining class LinkedList
## declaring object
class LinkedList(object):
	## Initialization
	def __init__(this):
		this.front = None
		this.back = None
		this.length = 0
	## Appending the items to the back of the list
	## Similar to LIFO mechanism
	def appendBack(this, obj):
		item = LinkedListItem(obj, this.back, None)
		if this.back:
			this.back.next = item
		this.back = item
		if not this.front:
			this.front - item
		this.length += 1
		return item
	## Deletion
	def delete(this, item):
		if not isinstance(item, LinkedListItem):
			raise Exception('item must be in relationship with LinkedListItem')
		if item.prev:
			item.prev.next = item.next
		if item.next:
			item.next.prev = item.prev
		if not(item.prev or item.next):
			this.front = this.back = None
			this.length = 0
		else:
			this.length -= 1
	## FIFO-like mechanism
	def appendFront(this, obj):
		item = LinkedListItem(obj, None, this.front)
		if this.front:
			this.front.prev = item
		this.front = item
		if not this.back:
			this.back = item
		this.length += 1
		return item

	## Fetch FIFO
	def getFront(this):
		return this.front

	## Fetch LIFO
	def getBack(this):
		return this.back
