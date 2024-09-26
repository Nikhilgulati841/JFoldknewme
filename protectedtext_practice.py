import random as r 
b=int(input('how many words you wish to type in => '))
#print(''.join(r.sample(a,len(a))))

d=[]
for i in range(b):
    n=input("enter a word : ")
    z=(''.join(r.sample(n,len(n))))
    d.append(z)
print(d)  

x="".join(r.sample(d,len(d)))
print(x)

list=[]
for j in d:
    list.append(j)

y="".join(list)
print("".join(r.sample(y,len(y))))
    