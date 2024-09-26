

from playsound import playsound
a=input("If you want to play a song then please press 'Y' otherwise 'N' :")

if a=='Y' or a=='y':
    playsound('E:\\Python\\chapters\\song.mp3')
    playsound('E:\\Python\\chapters\\song.mp3')

elif a=='N' or a=='n':
    print("Thank you for your response")

else:
    print("Please choose between the provided options ")

input()

                                    
# from datetime import datetime, date, timedelta, timezone

# x=datetime.now()   #when using (date) after importing date time, 
#                 #date.now() will not be used| either datetime.now() or date.today()
# print(x+timedelta(days=7))