class LinkedListStack < Stack 
	def init
		super
		@list = LinkedList.new
	end
	def purge
		@list.purge
		super
	end
end
