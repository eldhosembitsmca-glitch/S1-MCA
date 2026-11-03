'''  names=["anu","asha","ammu"]
counts=0
for name in names:
	counts +=name.count("a")
print("count of a :",counts)


s=input("enter a string :")
ch =s[0]
s=s.replace(ch,"$")
s=ch+s[1:]
print("string :",s)
'''

s1 = input("Enter a string: ")

s1.replace(0,s1[-1])
s1.replace(-1,s1[0])

print("String now:", s1)

radius=float(input("enter radius of the circle :"))
print("area of the circle :",(3.14*(radius*radius)))

