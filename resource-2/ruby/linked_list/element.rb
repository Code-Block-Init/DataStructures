class linked_list
	class element
		def init(list, datum, succ)
			@list = list
			@datum = datum
			@succ = succ
		end
		attr_accessor :datum
		attr_accessor :succ
	end
end
