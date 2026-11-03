list1=[11,-21,0,4,45,66]
for num in list1:
	if num>0:
		print("list numbers :",num,",") 

n=int(input("limit :"))
for i in range(1,n):
	print(i*i)

word=input("enter a word")
for letter in word:
	if letter in ''a,e,i,o,u":
		print(letter)
	
words = ["aparna", "aravind"]

for word in words:
    print(word)
    for ch in word:
        print(ch, ord(ch))
