class linked_list
	def clone
		result = linked_list.new
		ptr = @head
		while not ptr.nil?
			result.append(ptr.datum)
			ptr = ptr.succ
		end
		result
	end
end
