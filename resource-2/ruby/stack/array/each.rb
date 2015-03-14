class ArrayStack < stack
	def each
		for i in 0 ... @count
			yield @array[i]
		end
	end
end
