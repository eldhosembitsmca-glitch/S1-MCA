list1=[10,20,20]
sum=0;
for i in list1:
	sum +=i;
	
print("sum is :",sum)

#pyramid
n=int(input("enter the number of steps :"))
for i in range(1,n+1):
	for j in range(1,i+1):
		print(i*j, end=" ")
		
	print()
	
#string	
word=input("enter a string :")
if word.endswith("ing"):
	word=word+"ly"
else:
	word=word+"ing"
	
print(word)

#swap
a,b=10,20
print("values before swap a,b",a,b)
b,a=a,b
print("values after swap a,b", a,b)

#no didvide 5,10
a=int(input("enter a number :"))
if(a%5==0 ) and (a%10==0):
	print("this number is divided by 5 and 10")
else:
	print("this number is not  divided by 5 and 10")

#multiple of 3	
b=int(input("enter a number :"))
if b%3==0:
	print("this number is a multiple of 3")
else:
	print("this number is not multiple of 3")


		


