module algorithms
	def Algorithms.breadth_first_traversal(tree) # :yield: key
		queue = QueueAsLinkedList.new
		queue.enqueue(tree) if not tree.empty?
		while not queue.empty?
			t = queue.dequeue
			yield t.key
			for i in 0 ... t.degree
				subTree = t.getSubTree(i)
				queue.enqueue(subTree) if not subTree.empty?
			end
		end
	end
end
