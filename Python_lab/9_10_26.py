#longest a word in string
str=input("enter a string").split()
longest=str[0]
for word in str:
	if(len(word)>len(longest)):
		longest=word
		
print(longest)

#up and down side pyramid
lim=int(input("enter a limit :"))
for row in range(1,lim+1):
	for col in range(1,row+1):
		print("*",end=" ")
	print()
for row in range(lim-1,0,-1):
	for col in range(1,row+1):
		print("*",end=" ")
	print()	

#right angle pyramid
lim=int(input("enter a limit :"))
for row in range(1,lim+1):
	for space in range(row,lim+1):
		print(" ",end=" ")
	for col in range(1,row+1):
		print("*",end=" ")
	print()
	
#factors of a number
n=int(input("enter a limit :"))
for i in range(1,n+1):
	if n%i==0:
		print(i)
		
#full pyramid
lim=int(input("enter a limit :"))
for row in range(1,lim+1):
	for space in range(row,lim+1):
		print(" ",end=" ")
	for col in range(1,row+1):
		print("*",end=" ")
		print(" ",end=" ")
	print()
	
# \  pattern
lim=int(input("enter a limit :"))
space=1
for i in range(1,lim+1):
	for j in range(1,space):
		print(" ",end=" ")
	print("*",end=" ")
	print()
	space +=1
	
# / pattern 
lim =int(input("enter a limit :"))
for i in range(lim,1,-1):
	for j in range(1,i+1):
		print(" ",end=" ")
	print("*")
	print()




