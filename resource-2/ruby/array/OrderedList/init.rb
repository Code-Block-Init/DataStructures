class ArrayOrderedList < ArrayOrderedList
	def init(size = 0)
		super()
		@array = Array.new(size)
	end
	attr_reader :array
	attr_reader :count
end
