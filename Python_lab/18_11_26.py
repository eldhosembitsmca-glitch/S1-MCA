class Publisher:
	def __init__(self,name):
		self.name=name
class Book(Publisher):
	def __init__ (self, name,title,author):
		super().__init__(name)
		self.title=title
		self.author=author
class Python(Book):
	def __init__ (self,name,title,author,price,page_no):
		super().__init__(name,title,author)
		self.price=price
		self.page_no=page_no
	def display(self):
		print("Publisher name :",self.name)
		print("title :",self.title)
		print("author name :",self.author)
		print("price :",self.price)
		print("page no :",self.page_no)
		
s1=Python("DC Books","python for beginners","alex",200,300)
s1.display()
