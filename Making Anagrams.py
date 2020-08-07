# abc
#ampok
#output:6

a=input()
b=input()
d=len(a)+len(b)
c=0
for i in a:
    if i in b:
        c+=2
print(d-c)

