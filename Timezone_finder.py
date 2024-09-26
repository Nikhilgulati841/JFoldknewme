# from timezonefinder import TimezoneFinder

# obj=TimezoneFinder()
# latitude = 41.8719
# longitude = 12.5674
# print(obj.timezone_at(lng=latitude, lat=longitude))

#from today till 180 days, divide it into 6 sections of 30 days each, print the dates, 
# and assign the tasks for each 30 days for:- (1.Python)(2.Python {DSA} and advance version of python)
# (3.EXCEL, DBMS and SQL, using databases with python)(4.Django and if needed{HTML, CSS, javascript} | 
# GIT and GIT version)(5. Operating system and APTITUDE)(2 more months) in total 240 days.
'''
for i in range(1,20):
    if i==6:
        print("\nDone with learning python basics\n")
    if i==12:
        print("\nDone with learning SQL\n")
    if i==18:
        print("\nDone with learnig Tkinter\n")
    else:
        print("\nToday is day {}".format(i))

'''

import datetime

# ask=input("\nEnter the week day you wish to calculate the date from today: ")
# a=time.strptime(ask,"%A").tm_wday
# b=datetime.now().strftime("%A")
# c=time.strptime(b,"%A").tm_wday

# diff=a-c
# print(f"\n{abs(diff)} days left :)\n")

# x=input("Enter : ")
# y=x.split(" ",4)
# z="$".join(y)
# print(y)
# print(z)

# To find the year is leap year by incrementing year using (year,month,day format use stackflow to find the answer)
# x=datetime.strptime("29-02-2025","%d-%m-%Y")
# y=x+timedelta(days=0)
# a=datetime.now().strftime("%d\%m%Y")
b=[]
for i in range(2010,2025):
    b.append(datetime(i,2,25))
    # if datetime(i,2,29) in 

print(b)
