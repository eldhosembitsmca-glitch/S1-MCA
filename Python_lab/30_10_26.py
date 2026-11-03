		
print(f"largest ={max} , smallest ={min}")
#char count
s = input("Enter a string: ")

for i in s:
    if s.index(i) == s.index(i):
        print(i, ":", s.count(i))
        
#four digit perfect square
start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

a = []

for i in range(start, end + 1):
    if 1000 <= i <= 9999:
        root = int(i ** 0.5)

        if root * root == i:
            even = True

            for j in str(i):
                if int(j) % 2 != 0:
                    even = False

            if even:
                a.append(i)

print("Result:", a)
            
#amstrong number 
n = int(input("Enter a number: "))
temp = n
total = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == n:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
    
#palindrome
s=input("enter a string :")
if s==s[::-1]:
	print("palindrome")
else:
	print("not plaindrome")

#remove duplicates froma list 
num=input("enter a numbers :").split()
new_list=[]
for i in num:
	if i not in new_list:
		new_list.append(i)
		
print("new list :",new_list)

#largest and smallest number in a list
num=input("enter a numbers :").split()
min=int(num[0])
max=int(num[0])
for i in num:
	if int(i)<min:
		min=int(i)
	if int(i)>max:
		max=int(i)
		

