class linkedListStack < Stack 
	#push
	def push(obj)
		@list.prepend(obj)
		@count += 1
	end
	#pop
	def pop
		raise ContainerEmpty if @count == 0
		result = @list.first
		@list.extract(result)
		@count -= 1
		return result
	end
	#top
	def top
		raise ContainerEmpty if @count == 0
		return @list.first
	end
end
