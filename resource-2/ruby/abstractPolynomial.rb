class Polynomial < Container
	def init
		super
	end
	abstractmethod :addterm
	abstractmethod :differentiate!
	abstractmethod :+
end
