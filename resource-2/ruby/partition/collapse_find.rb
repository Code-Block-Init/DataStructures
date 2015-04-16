class PartitionWorld2 < PartitionWorld
	def find(item)
		root = @array[item]
		while not root.parent.nil?
			root = root.parent
		end
		ptr = @array[item]
		while not ptr.parent.nil?
			ptr, ptr.parent = ptr.parent, root
		end
		return root
	end
end
