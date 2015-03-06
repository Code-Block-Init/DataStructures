class multidimensionalarray
	def getOffset(index)
		raise IndexError if index.length != @dimensions.length
		offset = 0
		for i in 0 ... @dimensions.length
			if index[i] < 0 or index[i] >= @dimensions[i]
				raise IndexError
			end
			offset += @factors[i] * index[i]
		end
		return offset
	end
	def [](*index)
		@data[self.getOffset(index)]
	end
	def []=(*indexAndVal)
		value = indexAndVal.pop
		@data[self.getOffset(indexAndVal)] = value
	end
end
