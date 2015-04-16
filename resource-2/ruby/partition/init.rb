class PartitionWorld < Partition 
	def init(n)
		super
		@array = Array.new(@universeSize)
		for item in 0 ... @universeSize
			@array[item] = PartitionTree.new(self, item)
		end
		@count = @universeSize
	end
end
