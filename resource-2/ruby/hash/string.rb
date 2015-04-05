class string
	SHIFT = 6
	MASK = ~0 << (FixNum::BITS - SHIFT)
	def hash
		result = 0
		each_byte do |ig|
			result = ((result & MASK) ^ 
				(result << SHIFT) ^ ig) & FixNum::MAX
		end
		return result
	end
end
