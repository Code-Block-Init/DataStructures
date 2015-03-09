class abstractObject < ::Object
	def init
		super
	end
	include ::Comparable
	def <=> (obj)
		if is_a?(obj.type)
			return compareTo(obj)
		elsif obj.is_a?(type)
			return -obj.compareTo(self)
		else
			return type.name <=> obj.type.name
		end
	end
	abstractMethod :compareTo
	protected :compareTo
end
