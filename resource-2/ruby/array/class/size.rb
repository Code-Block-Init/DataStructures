class array
	def length = (value)
		temp = array.new(value, nil)
		for i in 0 ... [length, value].min
			temp.set_item(i, get_item(i))
		end
		clear
		set_item(value - 1, nil) if value > 0
		for i in 0 ... temp.length
			set_item(i, temp.get_item(i))
		end
	end
end
