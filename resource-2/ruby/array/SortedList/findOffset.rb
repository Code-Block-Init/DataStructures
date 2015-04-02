class ArraySortedList < ArratOrderedList
	def findOffset(obj)
		left = 0
		right = @count - 1
		while left <= right
			middles = (left + right) / 2
			if obj > @array[middle]
				left = middle + 1
			elsif obj < @array[middle]
				right = middle - 1
			else
				return middle
			end
		end
		return -1
	end
end
