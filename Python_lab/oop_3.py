class Time:
	def __init__(self,h,m,s):
		self.__h=h
		self.__m=m
		self.__s=s
	def __add__(self,t):
		h=self.__h+t.__h
		m=self.__m+t.__m
		s=self.__s+t.__s
		if s>=60:
			m=m+s//60
			s=s%60
		if m>60:
			h=h+m//60
			m=m%60
		return Time(h,m,s)
	def display(self):
		print("Time ",self.__h,":", self.__m, ":" ,self.__s)
		
t1=Time(2,45,50)
t2=Time(1,30,20)
t3=t1+t2
t3.display()
