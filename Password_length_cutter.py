n=(input("Enter the password that you needed to update the lenghth: "))
l=int(input("Enter the length till which you wish to cut through the lenghth: "))

if len(n)>l:
    print("The entered password is outside the maximum length of {}, it should be : {}".format(l,n[:l]))

else:
    print("The entered password is under the maximum length{}".format(n))
