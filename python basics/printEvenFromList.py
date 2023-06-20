x=int(input("enter the number of elements "))
l1=list()
for i in range(x):
    l1.append(int(input("enter element")))
print("the list is "+str(l1))

for y in l1: 
    if(int(y)%2==0):
        print(str(y)+" ")

l1.reverse()

print(l1)
l1.reverse()

"or []"

print(l1[::-1])

