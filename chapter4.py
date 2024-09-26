
# name="Nikhil"

# print(name.startswith("Nik"))

# x=["nikhil","nn","jj","h"]

# print(x)

# while x!="exit":
#     y=input("Enter value for which you need to find the location in the list : \n\n")
#     print("-----------------------------------")
   
    
#     if y in x:
#         print("The index of the choosen value is : ",x.index(y),"\n-----------------------------------\n")
#     elif y=="exit":
#         print("\n---- End of the Game ----\n")
#         break
#     else:
#         print("------------------------------------\nThis value is not in the list...!If you wish to exit the game, then type exit\n")

# _________________________________________________________________________________

# x=0

# while x!=True:
#     x=input("Do you wish to play the game? \n")

#     if x=="yes" or x=="y" or x=="Y":
#         print("Ok..! Cool...\n")
#     elif x=="no" or x=="n" or x=="N":
#         print("Thank you for choosing to play this game...! Now the game is exited.")
#         break
#     else:
#         print("I did not understand the option, Please choose yes or no | y or n")

# _________________________________________________________________________________

# x=input("Enter a statement with spaces which you need it to be printed with - in between and also to print each word individually : ")
# list=x.split()
# print(list)

# for i in list:
#     print(i)

# for i in list:
#     print(i,end="-")

# print("\n")
# x="nikhil"
# print(x)
# x.capitalize()
# print(x)
# print(x.capitalize())

# x=["nikhil","nn","jj","h"]
# y=[]
# z=[]
# for i in x:
#     y.append(i.capitalize())
#     z.append(i.upper())

# print(x)
# print(y)
# print(z)

# _________________________________________________________________________________

# Enter all the numbers with 1 space that you wish to sum up

# x=input("Enter all the numbers with 1 space that you wish to sum up  : ")
# list=x.split()
# print(list)

# total=[]

# for i in range(len(list)):
#     total.append(int(list[i]))

# print(total)
# print("\nSum of all the numbers | ",end="")
# for i in total:
#     print(i,end=" ")
# print(" = ",sum(total),"\n")


# _________________________________________________________________________________



x=["nikhil",2,1,"nannu"]
x.pop(0)
print(x)
y=set(x)
print(y)  

a={1,4,2}
a.update([2,3,1,"nannu"])   #you cannot add list to a set. However, you can add the list items in a set using update() method.
print(a)

# _________________________________________________________________________________


# x=input("Enter the numbers with 1 space which you wish to get the sum of: \n")
# list1=x.split(" ")
# list2=[]
# print(list1)

# for i in list1:
#     list2.append(int(i))

# print(list2)
# total=0
# for j in range(len(list2)):
#     total=total+list2[j]
    
# print("Sum using \"for loop\" {}".format(total))
# print("Sum using 'sum' function of list",sum(list2))




