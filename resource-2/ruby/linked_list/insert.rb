class linked_list
	class Element
		def insertAfter(item)
			@succ = Element.new(@list, item, @succ)
			if @list.tail.equal?(self)
				@list.tail = @succ
			end
		end
		def insertBefore(item)
			temp = Element.new(@list, item, self)
			if @list.head.equal?(self)
				@list.head = temp
			else
				prevPtr = @list.head
				while not prevPtr.nil? \
						and not prevPtr.succ.equal?(self)
					prevPtr = prevPtr.succ
				end
				prevPtr.succ = temp
			end
		end
	end
end
