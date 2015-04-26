class AVLTree < BinarySearchTree
	def LR_rotation
		raise StateError if empty?
		@left.RR_rotation
		LL_rotation
	end
end
