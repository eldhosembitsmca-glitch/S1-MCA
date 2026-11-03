#colour pgm
file_name=input("enter a file name :")
ext=file_name.split(".")
print("file extension :",ext[-1])

colors=input("enter colors seperated by commas :").split(",")
print("first color :",colors[0])
print("last color :",colors[-1]) 

#another pgms
n = int(input("Enter an integer: "))
nn = n*n
nnn = n*n*n

result = n+nn+nnn
print("Result =", result) 

#another pgm
list1=["red","blue","green","yellow"]
list2=["blue","yellow"]

for color in list1:
	if color not in list2:
		print(color) 

#another pgm
str1=input("enter a string :")
str2=input("enter a string :")

a=list(str1)
b=list(str2)
c=a[0]
a[0]=b[0]
b[0]=c

str1 = ''.join(a)
str2 = ''.join(b)
print(str1+str2)




