class matrix
	def init(rows, columns)
		assert { rows >= 0 }
		assert { columns >= 0 }
		@rows = rows
		@columns = columns
	end
	attr_reader :rows
	attr_reader :columns
	abstractmethod :+
	abstractmethod :*
	abstractmethod :transpose
end
