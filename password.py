
import random
import string

password=input("Enter the password: ")
list=[]
for i in password:
    list.append(i)

# or 
print("___________________")
print("".join(random.sample(password,len(password))))


# random.shuffle(list)
# print(list)

# characterlist=""
# characterlist +=string.ascii_lowercase
# print(characterlist)
# store=[]
# for i in range(10):
#     a=random.choice(characterlist)
#     store.append(a)

# print("".join(store).upper())

#____________________________________________________________ 

# a="hellomyname"
# print("".join(random.sample(a,len(a))))

# a={"hello":1,"henry":2,"lulu":3,"lokhand":4,"kilo":5}
# start=str(input("Tell the letter: "))
# for key,value in a.items():
#     if key.startswith(start):
#         print(key)
   
