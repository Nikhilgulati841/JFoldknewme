'''

a=45

else:
    print("Cannot say anything")  #wrong approach
if a>3:
    print("The number is gretare than 3")


a=[1,2,3,4,5,6,-1]
a.sort()
print(a)

for i in a[:len(a)]:
    print(i,end=" ")
# ----------

a=[]
num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))
num3=int(input("Enter number 3 :"))
num4=int(input("Enter number 4 :"))

a.append(num1)
a.append(num2)
a.append(num3)
a.append(num4)

print(a)

a.sort()
print(a)
print(f'The largest number among all is : {a[-1]}')
print(f'The largest number among all is : {max(a)}')
# --------



sub1=int(input("Enter the marks for subject1 : "))
sub2=int(input("Enter the marks for subject2 : "))
sub3=int(input("Enter the marks for subject3 : "))

sum=sub1+sub2+sub3
average=sum/3
print(round(average,2))

if sub1<33:
    print("Fail as you have less marks than 33 in sub1")
if sub2<33:
    print("Fail as you have less marks than 33 in sub2")
if sub3<33:
    print("Fail as you have less marks than 33 in sub3")

elif average<40:
    print("You have less overall marks than 40 | So you have FAILED")
else:
    print("Pass in the test average marking and individual subject marking also")


'''

    
text=input("Enter the text : \t")

list=text.split()


if "make a lot of money" in text:
    spam=True
elif "buy now" in text:
    spam=True
elif "subscribe this" in text or "Subscribe this" in text or "subscribe" in text or "Subscribe" in text:
    spam=True
elif "poti" in text:
    spam=True
else:
    spam=False

if spam:
    print("\nThis text is Spam\n")
else:
    print("\nThis text is not a Spam\n")


