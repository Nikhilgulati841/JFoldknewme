
# Write a program to create a dictionary of hindi words and print the english word out of it using the user input 
# a={"sehai":"Ink","bandar":"Monkey","buddhu":"Stupid"}
# o=list(a.keys())
# print("This is the list of dictionary item from which you can choose : ",o,"\n")

# take=input("Please enter for which word you wish to get the english meaning : ")


# if take in o:
#     print("The english meaning of {} is : {}\n".format(take,a[take]))

# else:
#     print('This value of {} is not an option from the above options...!'.format(take))


# # or by this method also.

# a={"sehai":"Ink","bandar":"Monkey","buddhu":"Stupid"}
# take=input("Enter the hindi word :\n")
# # print("The english meaning of your word is : ",a[take])
# print("The english meaning of your word is : ",a.get(take)) #This will return None if not present in the dictonary and not an error

# _______________________________________________________________________________

# # To take 5 inputs and display all the unique values,
# # also  print two same value in a set with int and string as data type as for a2 
# a1=int(input("Enter no 1 :"))
# a2=input("Enter no 2 :")
# a3=int(input("Enter no 3 :"))
# a4=int(input("Enter no 4 :"))
# a5=int(input("Enter no 5 :"))

# a={a1,a2,a3,a4,a5}
# print("Unique value is : ",a)
# v={1,3,3,4,5}
# print(v)

# _______________________________________________________________________________
# to find the palindrome
# a="1234321"
# a[:]==a[::-1]  #returns True


# _______________________________________________________________________________


# Allow 5 friends to enter their fav language and assume that names are unique
# favlang={}
# a1=input("Enter your favourite language nikhil: ")
# a2=input("Enter your favourite language shubham: ")
# a3=input("Enter your favourite language akhil: ")
# a4=input("Enter your favourite language aryan: ")
# a5=input("Enter your favourite language nannu: ")
# print("\n")

# favlang["nikhil"]=a1
# favlang["shubham"]=a2
# favlang["akhil"]=a3
# favlang["aryan"]=a4
# favlang["nannu"]=a5

# print(favlang)

# listkeys=list(favlang.keys())
# listvalues=list(favlang.values())

# x=input("\n\nEnter the name of the language, to which you wish to know the name of the person using it:\t")
# print("\nThe person using {} is : {}".format(x,listkeys[listvalues.index(x)]))

# print("----------------------------------")
# print(f"\nAll name using {x}\n")
# for key,value in favlang.items():    #alternate option
#     if value.startswith(x):
#         print("Name: ",key)
# print("----------------------------------")



# --------------------------------------------------------------------------------------------------------

x=["Nikhil","nannu","Bhim","bheem","hello"]
letter=input("Enter the letter: ")

for i in x:
    if i[0].lower()==letter.lower():
        print(i)
    



# --------------------------------------------------------------------------------------------------------




# x=0
# c=input("Enter the friend name for which you wish to get their selected favourite language : \n")

# while x!=exit:
#     if c in keylist:
#         print("The selected language by your friend {} is : {} ".format(c,favlang.get(c)))
#         c=input("Enter the friend name for which you wish to get their selected favourite language : \n")

#     elif c=="exit" or c=="Exit":
#         print("You have choose to exit out of the program")
#         break
#     else:
#         print("This friend name is not present in your data | Please choose wisely\n")
#         c=input("Enter the friend name for which you wish to get their selected favourite language : \n")
# ---------------------------------------------------------------------------------

# pos=valuelist.index(c)
# # print(pos)
# print(keylist[pos])
# print(list(favlang.keys())[list(favlang.values()).index(c)])

# print(len(favlang))
# print(list(favlang.keys()))

# print(list(favlang.keys())[list(favlang.values()).index(c)])


# print(list(favlang.keys())[4])
# -----------------------------------------------------------


# hello={"name1":"Nikhil","name2":"Aman","dict2":{"name1":"Nikhil1","name2":"Aman2"}}
# hi={}
# c=(1,)
# d=1
# e=1,2,3



