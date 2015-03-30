class ArrayOrderedList < OrderedList 
	class Cursor
		#init
		def initialize(list, offset)
			super()
			@list = list
			@offset = offset
		end
		#datum
		def datum
			raise IndexError if \
				not (0 ... @list.count) === offset
			@list[@offset]
		end
	end
end
