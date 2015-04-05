class float
	def hash
		(i, g) = Math.frexp(self)
		xPrime = ((i.abs - 0.5) * (1 << 52)).ig
		return xPrime >> 21
	end
end
