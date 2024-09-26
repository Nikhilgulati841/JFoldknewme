"""
# Question 1

a=int(input("Enter a number : "))
b=int(input("Enter a number to divide with : "))

print("The number of times it will be divided : ", a/b)
print("The absolute number of times it will be divided : ", a//b)
print("The remainder : ", a%b)


# Question 2

a=int(input("Enter first number : "))
b=int(input("Enter second number : "))

print(f'first number is {a} and second number is {b}')

if a>b:
    print("First number {} is greater than {} ".format(a,b))
else:
    print("Second number {1} is greater than first number {0} ".format(a,b))


# Question 3

name=input("Enter your name : \t")
date=input("Enter the date : \t")
print("\n")

letter='''\nHello name,\n
Thank you for joining WNS
on : date\n'''

letter=letter.replace("name",name)
letter=letter.replace("date",date)
print(letter)


# Question 4

letter="Hello my  name  is nikhil, please correct    this statement as  soon as possible.  Thank you"


print(letter.find("  "))
print(letter.replace("  "," "))
print(letter)
print(letter.count("  "))

x=letter.split("  ")
print(x)

for i in x:
    print(i,end=" ")

"""

print("""\nhi my name is nikhil
 and i am here to judge""")
print('''hi my name is nikhil\
 and i am here to judge''')



