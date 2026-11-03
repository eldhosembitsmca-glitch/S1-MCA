#dictonary pgm
d={'a':1, 'c':2, 'd':5, 'b':3,'e':4}
asc=list(d.keys())
asc.sort()
print(asc)
asc.sort(reverse=True)
print(asc)

#removing even numbers
list1=[1,2,5,6,8,10,3]
n=len(list1)
i = 0
while i < len(list1):
    if list1[i] % 2 == 0:
        list1.pop(i)
    else:
        i = i + 1
print(list1)
