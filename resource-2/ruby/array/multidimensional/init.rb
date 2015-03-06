class multidimensionalarray
	def init(*dimensions)
		@dimensions = Array.new(dimensions.length)
		@factors = Array.new(dimensions.length)
		product = 1
		i = dimensions.length - 1
		while i >= 0
			@dimensions[i] = dimensions[i]
			@factors[i] = product
			product *= @dimensions[i]
			i -= 1
		end
		@data = Array.new(product)
	end
end
