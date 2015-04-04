class ArraySortedList < ArrayOrderedList
	# find
	def find(obj)
		offset = findOffset(obj)
		if offset >= 0
			return @array[offset]
		else
			return nil
		end
	end
	# Cursor
	class Cursor < ArrayOrderedList::Cursor
		def init(list, offset)
			super
		end
		undef_method :insertAfter
		undef_method :insertBefore
	end
	# find position
	def findPosition(obj)
		Cursor(self, findOffset(obj))
	end
end
