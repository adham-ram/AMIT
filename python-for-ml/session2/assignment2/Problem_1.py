x=input("Enter a string: ")
x=x.split()
y=len(x)
s=""
for i in x:
    s+=x[y-1]+" "
    y-=1
print(s)