class abstractQueue < Container
	def init
		super
	end
	abstractmethod :enqueue
	abstractmethod :dequeue
	abstractmethod :head
end
