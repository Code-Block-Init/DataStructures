class ArrayMultiSet < MultiSet 
	#insert
	def insert(item)
		@array[item] += 1
	end
	#withdraw
	def withdraw(item)
		raise ArgumentError if @array[item] == 0
		@array[item] -= 1
	end
	def member?(item)
		@array[item] > 0
	end
end
