# ------------------------------------------------------------------------------
# splitting a word into two

a=input("Enter a word combined with two words: ")
w=input("Where you wish to get it splitted from: ")

list=list(a)
list1=[]
list2=[]
# for i in a:
#     list.append(i)

print(list)
print("\n\n")

for j in list[:list.index(w)]:
    list1.append(j)

print(list1)
print("".join(list1))

for k in list[list.index(w)::]:
    list2.append(k)

print(list2)
print("".join(list2))
# ------------------------------------------------------------------------------