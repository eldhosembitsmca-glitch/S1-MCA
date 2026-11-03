#dictionaries merging pgm
a={'a':1,'b':2}
b={'c':3,'d':4}
a.update(b)
print("merged dict :",a) 

#2 numbers gcd calculating pgm
x=int(input("enter a number"))
y=int(input("enter a number"))
rem=0
while y!=0:
	rem=x%y
	x=y
	y=rem
	
print("GCD =",x) 

#even numbers list
list1=[1,2,3,4,5,6,7]
list2=[]
for i in list1:
	if i%2==0:
		list2.append(i)
		
print("new list :",list2) 

#factorial finding pgm
n=int(input("enter a number"))
fact=n
n=n-1
while n>0:
	fact=fact*n
	n=n-1	
print("factorial is :",fact) 

#fibnocci series pgm
N = int(input("Enter a range: "))
m = 0
n = 1

for i in range(N):
    print(m, end=" ")
    o = m + n
    m = n
    n = o
	
