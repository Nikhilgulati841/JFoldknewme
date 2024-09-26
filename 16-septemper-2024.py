#  split a word without spaces into two
# word=input("Type the sentence without any space: ")
# cut=input("Enter the word from which you wish to cut the word into two: ")

# list=list(word)
# l1=[]
# l2=[]
# for i in list[:list.index(cut)]:
#     l1.append(i)

# for i in list[list.index(cut):]:
#     l2.append(i)

# print("".join(l1))
# print("".join(l2))
# ________________________________________________________________________

#  weekday between a given year for today  | Also write the number for tm_wday,weekday(),isoweekday(),for x.strftime(%A), for x.strftime(%w)

# from datetime import datetime, date, timedelta
# import time

# weekdays = {1: "Monday",
#             2: "Tuesday",
#             3: "Wednesday",
#             4: "Thursday",
#             5: "Friday",
#             6: "Saturday",
#             7: "Sunday"}

# start_year=int(input("Enter the starting year\n"))
# end_year=int(input("Enter the ending year\n"))
# x=datetime.now().date()
# print(x.isoweekday())
# print(time.strptime("Monday","%A").tm_wday)
# year=x.year
# month=x.month
# day=x.day


# for i in range(start_year, end_year+1):
#     print("The {}\\{} in the year[{}] has fallen on: {}".format(day,month,i,weekdays[datetime(i,month,day).isoweekday()]))



# ________________________________________________________________________

#  weekday name for today and for specified date 

from datetime import datetime, date, timedelta
import time

weekdays = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}

start_year=int(input("Enter the starting year\n"))
end_year=int(input("Enter the ending year\n"))
day=input("Enter the month and the day| In this Format[ Month(XX)\\Day(XX) ]: ")
x=datetime.strptime(day,"%m\\%d")
month=x.month
day=x.day


for i in range(start_year, end_year+1):
    print("The {}\\{} in the year[{}] has fallen on: {}".format(day,month,i,weekdays[datetime(i,month,day).isoweekday()]))





# ________________________________________________________________________

#datetime(2024,9,16,59,59,59).date()  --> will only print the date and .time()  -->will only print the time

# import calendar
# from datetime import datetime
# print(calendar.month_name[9])
# x=calendar.monthrange(2024,7)
# # calendar.prcal(2024)
# print(x)
# print(x[0])
# y=datetime.strptime(str(x[0]+1),"%d")
# z=y.strftime("this is %A")
# print(z)

# if x[-1]==29:
#     print("leap year")
# else:
#     print("Normal year")

