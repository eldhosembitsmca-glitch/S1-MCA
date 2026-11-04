#args
def a(*args):
	for i in args:
		print(i)
a(1,2,3)

#kargs
def b(**kargs):
	for i,j in kargs.items():
		print(f"{i} : {j} ")

b(name="arun")

#student grade pgm
mark=int(input("enter a student mark (0-100) :"))
if mark>=90:	
	print('A garde')
elif mark>=80:
	print('B grade')
elif mark>=70:
	print('C grade')
elif mark>=60:
	print('D grade')
else:
	print('Fail')

#Lambda function usage	
fun =lambda x:"eligible" if x>=18 else "not eligible"	
age=int(input("enter your age :"))
print(fun(age))

if age>=18:
	print("eligible to vote")
else:
	print("not eligible to vote")
	
#function
def sum_of_n(n):
	sum=0
	for i in range(1,n+1):
		sum +=i
	print(f"sum : {sum}")
	
sum_of_n(10)

