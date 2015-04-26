class AVLTree < BinarySearchTree
	def balance
		adjustHeight
		if balanceFactor > 1
			if @left.balanceFactor > 0
				LL_rotation
			else
				LR_rotation
			end
		elsif balanceFactor < -1
			if @right.balanceFactor < 0
				RR_rotation
			else
				RL_rotation
			end
		end
	end
end
