class array
	alias_method :get_item, :[]
	alias_method :set_item, :[]=
	protected :get_item, :set_item
	def getOffset(index)
		@baseIndex = 0 if @baseIndex.nil?
		raise IndexError if not \
			(@baseIndex ... @baseIndex + length) === index
		return index - @baseIndex
	end
	def [](index)
		get_item(getOffset(index))
	end
	def []=(index, value)
		set_item(getOffset(index), value)
	end
end
