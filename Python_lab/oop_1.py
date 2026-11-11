class Rectangle:
	def __init__(self,l,b):
		self.l=l
		self.b=b
	def area(self):
		return self.l*self.b
	def perimeter(self):
		return 2*(self.l + self.b)
		
		
r1=Rectangle(5,10)
r2=Rectangle(20,10)
print(r1.area())
print(r1.perimeter())
print(r2.area())
print(r2.perimeter())

if r1.area() >r2.area():
	print("rectangle r1 area is greater ")
else:
	print("rectangle r2 area is greater ")

