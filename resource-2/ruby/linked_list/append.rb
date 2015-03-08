class linked_list
	def append(item)
		temp = Element.new(self, item, nil)
		if @head.nil?
			@head = temp
		else
			@tail.succ = temp
		end
		@tail = temp
	end
end
