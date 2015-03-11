class container < abstractObject
	def accept(visitor)
		assert { visitor.is_a?(visitor) }
		each do |obj|
			break if visitor.done?
			visitor.visit(obj)
		end
	end
end
