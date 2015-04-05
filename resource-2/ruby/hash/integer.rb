class FixNum
	BITS = 31
	MAX = 1073741823
	MIN = -1073741824
end
class integer
	def hash
		return self & FixNum::MAX
	end
end
