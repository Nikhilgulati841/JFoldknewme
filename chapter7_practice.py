'''

a=int(input("Enter the number for which you wish to get the multiplication : \n"))
b=int(input("Enter till which number you wish to get the multiuplication for the number chosen above : \n"))

for i in range(1,b+1):
    print("The multiplication of {} * {} = {}".format(a,i,i*a))

'''
#greet all the person whose name started with s

list=["harry","nikhil","sunny","nannu","shubham"]
greet=input("enter the letter you want to greet : \n")

for i in list:
    if i.startswith(greet):
        print("Welcome | {} sir |".format(i))
    
   
'''
# greet all the persons whose name has a letter n in it 

list=["harry","nikhil","sunny","nannu","shubham"]
for i in list:
    if 'n' in i:
        print("Welcome | {} sir |".format(i))
    else:
        print("Thank you for coming, now it's time to go {}".format(i))

# using while loop get the multiplication

i=1

a=int(input("Enter the number for which you wish to get the multiplication : \n"))
b=int(input("Enter till which number you wish to get the multiuplication for the number chosen above : \n"))

while i<=b:
    print("The multiplication of {} * {} = {}".format(a,i,i*a))
    i+=1

# given number is prime or not

num=int(input("Enter a number to find if it is prime or not : \n"))

for i in range(2,num):
    if num%i==0:
        print(f'The number {num} is not prime')
        break
else:
    print(f'The number {num} is prime')

# Find the sum of first n natural numbers
n=int(input("Enter the number till which you wish to get the sum of for the natural numbers : \n"))

i=0
a=[]
while i<=n:
    a.append(i)
    i+=1

print(sum(a))

# find the factorial of the given number
import sys
sys.set_int_max_str_digits(10000000)
n=int(input("Enter the number for which you wish to get the factorial for : \n"))
fact=1
for i in range(1,n+1):
    fact=fact*i

print(fact)

# print start patterns

n=int(input("Enter the number of lines to print the star pattern \n"))

for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()

    
# Function to print full pyramid pattern

num=int(input("Enter the number of lines : \n"))

for i in range(num):
    # for printing spaces
    for j in range(num-i):
        print(" ",end="")
        # for printing stars
    for j in range(1,2*i):
        print("*",end="")
    print()
        
for i in range(num,0,-1):
    # for printing spaces
    for j in range(num-i):
        print(" ",end="")
        # for printing stars oppo direction
    for j in range(2*i-1):
        print("*",end="")
    print()


#reverse multiplication printing

a=int(input("Enter the number for which you wish to get the multiplication : \n"))
b=int(input("Enter till which number you wish to get the multiuplication for the number chosen above : \n"))

for i in range(b,0,-1):
    print("The multiplication of {} * {} = {}".format(a,i,i*a))
    
'''
    

