class denseMatrix < matrix 
	def init(rows, columns)
		super
		@array = MuliDimensionalArray.new(rows, columns)
	end
	def [](i, j)
		@array[i, j]
	end
	def []=(i, j, value)
		@array[i, j] = value
	end
end
