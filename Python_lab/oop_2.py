class Bank:
	def __init__(self,ac_no,name,ac_type,balance):
		self.ac_no=ac_no
		self.name=name
		self.ac_type=ac_type
		self.balance=balance
		
	def deposit(self,amount):
		self.balance=self.balance+amount
		print("amount deposited")
	def withdraw(self,amount):
		if self.balance<amount:
			print("insufficent balance")
		else:
			self.balance=self.balance-amount
			print(amount," amount released ")
	def display(self):
		print("account number :",self.ac_no)
		print("Name :",self.name)
		print("account type :",self.ac_type)
		print("balance :",self.balance)
		
b=Bank(101,"john ", "saving",50000)
b.display()
b.deposit(10000)
b.withdraw(2000)
b.display()
