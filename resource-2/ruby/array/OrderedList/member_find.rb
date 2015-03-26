class ArrayOrderedList < OrderedList
	#member
	def member?(obj)
		for i in 0 ... @count
			return true if @array[i].equal?(obj)
		end
		false
	end
	#find
	def find(obj)
		for i in 0 ... @count
			return @array[i] if @array[i] == obj
		end
		nil
	end
end
