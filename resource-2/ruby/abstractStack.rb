class Stack < Container
	def init
		super
	end
	abstractmethod :push
	abstractmethod :pop
	abstractmethod :top
end
