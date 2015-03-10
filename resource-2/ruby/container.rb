class container < abstractObject
	include ::Enumerable
	def init
		super
		@count = 0
	end
	attr_reader :count
	def purge
		@count = 0
	end
	def empty?
		count == 0
	end
	def full?
		false
	end
end
