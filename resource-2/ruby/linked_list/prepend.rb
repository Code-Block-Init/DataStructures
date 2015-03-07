class linked_list
	def prepend(item)
		temp = Element.new(self, item, @head)
		@tail = temp if @head.nil?
		@head = temp
	end
end
