
# from datetime import datetime, date, timedelta

# x=date.today()

# print("\nToday is | ",datetime.now(),"\n")
# print("I will cover python basics and advanced video of \'CodeWithHarry\' + \
# would have already started and completed more than half of the course from tutedude course of python till this date | ",end=" ")
# y=x+timedelta(days=45)
# print(y,end=" ")
# print(y.strftime("The Month after 45 days will be: %B\n"))


# from datetime import datetime, date, timedelta

# x=datetime.now()
# print("\n",x,"\n")
# y=x+timedelta(days=45)
# print("\n",y,"\t",y.strftime("%m and weekday: %A"),"\n")
# z=y+timedelta(days=60)
# print("\n",z,"\t",z.strftime("%M and weekday: %a"),"\n")

# da=int(input("How many days you wish to get added to today:\t"))
# x=datetime.today()
# print(x)
# print(x.strftime("%I:%M %p"))
# y=x+timedelta(days=da)
# print(y.strftime("That will be %A and %jth day of the year, %d %B, %Y %I:%M %p"))

# from datetime import datetime, date, timedelta
# date1 = datetime(2024, 9, 1, 8,24,40,58)+ timedelta(days=45)  --
# print(date1)

# StartDate = "9-3-2024 8:00 pm"
# seconddate= "9-10-2024 9:00 pm"

# Date1 = datetime.strptime(StartDate, "%m-%d-%Y %I:%M %p")
# Date2 = datetime.strptime(seconddate, "%m-%d-%Y %I:%M %p")
# print(Date1.strftime("\n%A %jth day of the year, %Y | %I:%M %p\n"))

# currentdate=datetime.today()
# print(currentdate)
# print(Date2)
# diff=Date2-Date1
# print(abs(diff))  #gives correct value whenever used
# print(diff) #only used when calculating the date for future with today


# from datetime import datetime, date, timedelta

# startdate="9-2-2024  8:00 pm"
# finaldate=input("Enter the final date, you wish to calculate the days till that(use format[MONTH(XX)\\DAYS(XX)\\YEAR(XXXX) Time(XX:XX am/pm)]): \t")
# enddate=int(input("Enter the days you have planned to be be added today: \t"))

# Date1=datetime.strptime(startdate,"%m-%d-%Y %I:%M %p")
# currentdate=datetime.today()
# daysadd=currentdate+timedelta(days)
# Date2=Date1+timedelta(days=enddate)
# Date3=datetime.strptime(finaldate,"%m\\%d\\%Y %I:%M %p")

# print(Date1)
# print(Date2)
# diff=Date3-Date1
# print(abs(diff))

import calendar
from datetime import datetime, date, timedelta
import time, pytz

z=0

while z!=True:
    c=input("\nType 1 | Current date and weekday\n\
Type 2 | Want to add some days to the current date\n\
Type 3 | Want to get the difference(in day with exact hours) between today and the date mentioned\n\
Type 4 | Want to get the difference(in day with exact hours) between two dates or hours\n\
Type 5 | To know [Exact Day No. of that specific year, Full calendar of that year, Weekday, Weekday name of the 1st of that month, Calendar of that year]\n\
Type 6 | Get all the format of date for today\n\
Type 7 | How many days left till the upcoming week day you choose\n\
Type 8 | Change the timezone\n\
Type 9 | Get the weekdays name for differnt year, for the same date as today or different\n\
Type 10| Want to add some hours to the current time\n\
------------------------------------------------------------\n\
Type EXIT | to exit the application\n\
------------------------------------------------------------\n\n\
Please type, which option you wish to choose: ")
    

    
    if c=="2":
        add=int(input("Enter the days you have planned to be added today: "))
        currentdate=datetime.today()
        daysadd=currentdate+timedelta(days=add)
        p=daysadd.strftime("\n==>Today is {} \n\
After {} days from now, the day will be %A and the date[%B %d, %Y]\n".format(currentdate.strftime("%A and the date[%B %d, %Y]"),add))
        print(p.upper())
        print("------------------------------------------------------------")

    elif c=="1":
        currentdate=datetime.today()
        q=currentdate.strftime("\n==> Today is %A and the date[%B %d, %Y] Time[%I:%M%p]\n")
        print(q.upper())
        print("\nIf you would like to know the date time and week of some other place--> Type 8 to change the Timezone")
        print("------------------------------------------------------------")

    elif c=="3":
        currentdate=datetime.today()
        enddate=input("\nEnter the date from which you wish to get the difference(in days and hours) from today\n\
Please type in this format | [MONTH(XX)\\DAYS(XX)\\YEAR(XXXX) Time(XX:XXam/pm)]: ")
        date1=datetime.strptime(enddate,"%m\\%d\\%Y %I:%M%p")
        diff=date1-currentdate
        r="\n==> The difference between your mentioned date|\n\
[{}] and Today[{}] is: {}(hours)\n".format(date1.strftime("%B %d, %Y Time| %I:%M %p"),currentdate.strftime("%B %d, %Y Time| %I:%M %p"),abs(diff))
        print(r.upper())
        print("------------------------------------------------------------")

    elif c=="4":
        print("\n||if you wish to get the difference between the hours, put the same date||\n")
        startdate=input("\nEnter date 1\n\
Please type in this format | [MONTH(XX)\\DAYS(XX)\\YEAR(XXXX): ")
        enddate=input("\nEnter date 2\n\
Please type in this format | [MONTH(XX)\\DAYS(XX)\\YEAR(XXXX): ")
        date4=datetime.strptime(startdate,"%m\\%d\\%Y")
        date5=datetime.strptime(enddate,"%m\\%d\\%Y")
        diff2=date4-date5

        print(("\n==> The difference between dates|\n\
{} and {} is: {}".format(date4.strftime("%B %d, %Y"),date5.strftime("%B %d, %Y"),abs(diff2))).upper())
        print("------------------------------------------------------------\n")
        ask=input("If you wish to get the difference with hours, types Yes, else No: ")
        if ask=="Yes" or ask=="YES" or ask=="yes" or ask=="y" or ask=="Y":
            startdate1=input("\nEnter date 1\n\
Please type in this format | [MONTH(XX)\\DAYS(XX)\\YEAR(XXXX) Time(XX:XXam/pm)]: ")
            enddate1=input("\nEnter date 2\n\
Please type in this format | [MONTH(XX)\\DAYS(XX)\\YEAR(XXXX) Time(XX:XXam/pm)]: ")
            date6=datetime.strptime(startdate1,"%m\\%d\\%Y %I:%M%p")
            date7=datetime.strptime(enddate1,"%m\\%d\\%Y %I:%M%p")
            diff3=date6-date7
        
            print(("\n==> The difference between dates|\n\
{} and {} is: {}".format(date4.strftime("%B %d, %Y %I:%M%p"),date5.strftime("%B %d, %Y %I:%M%p(hours)"),abs(diff3))).upper())
            print("------------------------------------------------------------\n")

        else:
            continue

    elif c=="5":
        typedate=input("\nEnter the date in this format | [MONTH(XX)\\DAYS(XX)\\YEAR(XXXX)]: ")
        date2=datetime.strptime(typedate,"%m\\%d\\%Y")
        print(("\n\n==> For date you mentioned [{}], it is DaY No:{} of year[{}]\n".format(date2.strftime("%A %B %d, %Y"),date2.strftime("%j"),date2.strftime("%Y"))).upper())
        l=[]
        l=typedate.split("\\")
        x1=calendar.monthrange(int(l[-1]),int(l[0]))
        y1=datetime.strptime(str(x1[0]+1),"%d")
        print(x1[0])
        print(y1.strftime("\n==> Also, the 1st of that month was %A and this month have"),f"{x1[1]} days\n")
        print("You can also have a look at the calendar for that year below:\n")
        print(calendar.calendar(int(l[-1])))
        print("Calender printed successfully")
        print("------------------------------------------------------------")

    elif c=="6":
        todaydate=datetime.now()
        print("\nAll the format for today's date|\n\n{}\n{}\n{}".format(todaydate.strftime("%d\\%m\\%Y"),todaydate.strftime("%d %B, %Y"),todaydate.strftime("%d-%m-%Y and and today is %jth day of the year")))
        print("------------------------------------------------------------")

    elif c=="7":
        ask=input("\nEnter which day of the week you wish to calculate the days from today\n\
Format[sunday,monday etc..]: ").capitalize()
    
        x=time.strptime(ask,"%A").tm_wday   #to get the number value of the weekday in string format (time.strptime("string",%A)).tm_wday
        t=datetime.now().strftime("%A")
        m=time.strptime(t,"%A").tm_wday
        z=datetime.now()
        # print(x)    
        # print(t.isoweekday())  #t.isoweekday() (wrong) is used for getting integer value of that week but not with string
        # print(z.isoweekday())    #z.isoweekday() (correct) with date.now() value 1==>Monday, 2==>Tuesday like that 
        # print(z.weekday())       #z.weekday() will also give the integer value but, it will show 0==>Monday, 1==>Tuesday like that 
        # print(t)                 #tm_wday from the given value of string, will also give same as 0==>Monday, 1==>Tuesday
        w_diff=x-m                 #for x.strftime(%w) --> 0==>Monday, 1==>Tuesday
        n_diff=w_diff+7            #calendar.monthrange(2024,9)  --> (first day of week->Sunday, last day no of that month-->30) This will also give ==> 0==>Monday, 1==>Tuesday
        # print("---->> ",w_diff)
        if w_diff==1:
            print("\n==> Today is: {}\n\
==> {} day from Today, {} will come..!\n".format(t,abs(w_diff),ask))
            print("------------------------------------------------------------")
        elif w_diff==0:
            print("\n==> Today is the same day: {} :) \n\
==> So, the next {} will be on 7th Day from Today :)\n".format(ask,ask))
            print("------------------------------------------------------------")
        elif w_diff<0:
            if abs(w_diff)==1:
                print("\n==> {} day back from Today was {} :) \n\
==> Also, {} days from Today will be your next {} :)\n".format(abs(w_diff),ask,n_diff,ask))
                print("------------------------------------------------------------")
            else:
                print("\n==> {} days back from Today was {} :) \n\
==> Also, {} days from Today will be your next {} :)\n".format(abs(w_diff),ask,n_diff,ask))
                print("------------------------------------------------------------")

        else:
            print("\n==> Today is: {}\n\
==> {} days from Today, {} will come..!\n".format(t,abs(w_diff),ask))
            print("------------------------------------------------------------")

    elif c=="8":
        print("\nTimezones for==> Italy | London | Spain | New York | India | Portugal |\
 Egypt | Turkey | Amsterdam | Nairobi | Norway | Canada | Dubai | Pakistan\n")
        zone=input("Enter for which you want the time zone: ").capitalize()
        city={"Italy":"CET", "London":"Europe/London", "Spain":"CET", "Portugal":"WET", "Egypt":"Egypt", "Turkey":"Turkey", "Nairobi":"Africa/Nairobi", 
              "Norway":"CET", "Canada_Pacific":"Canada/Pacific", "Canada_Eastern":"Canada/Eastern","Canada_Mountain":"Canada/Mountain",
              "Canada_Central":"Canada/Central", "Dubai":"Asia/Dubai", "Pakistan":"Etc/GMT-5", "India":"Asia/Kolkata", "New york":"America/New_York","Newyork":"America/New_York","Amsterdam":"Europe/Amsterdam"}
        if zone=="Canada":
            choose=input("Enter which timezone of canada: Pacific || Mountain || Eastern || Central\n").capitalize()
            if choose=="Pacific":
                zone="Canada_Pacific"
            elif choose=="Mountain":
                zone="Canada_Mountain"
            elif choose=="Eastern":
                zone="Canada_Eastern"
            elif choose=="Central":
                zone="Canada_Central"
            else:
                print("\nPlease choose among==> Pacific || Mountain || Eastern || Central\n")
        #url=https://www.timeanddate.com/time/zone/canada

        x=pytz.timezone(city.get(zone))
         
        print(f"\n==> In {zone}:\n\n",datetime.now(x).strftime("Weekday| %A\nDate[%B %d, %Y]\nTime[%I:%M:%S %p]\n"))
        print("------------------------------------------------------------")
        # alltimezone=pytz.all_timezones
        # print(alltimezone)

    elif c=="9":
        weekdays = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}

        today=datetime.now()
        current_year=today.year
        # print(current_year)
        day=today.strftime("%d")
        month=today.strftime("%B")
        year=today.strftime("%Y")

        user=input("\nYou wish to get the weekday as of \"Today's\" date for different years OR for \"Different\" date: \n\
Type 1| For Today's date:\n\
Type 2| For Different date: \n")
        
        if user=="1":
            start_year=int(input("\nEnter the starting year: "))
            end_year=int(input("Enter the ending year: "))
            print("\n")

            for i in range(start_year,end_year+1):
                print("==> The {} {} in the Year[{}] has fallen on : {}".format(month,day,i,weekdays[datetime(i,today.month,today.day).isoweekday()]))

        elif user=="2":    
            day=input("\nEnter the month and the day| In this Format[ Month(XX)\\Day(XX) ]: ")
            start_year1=int(input("\nEnter the starting year: "))
            end_year1=int(input("Enter the ending year: "))
            x=datetime.strptime(day,"%m\\%d")
            month1=x.strftime("%B")
            day1=x.day
            print("\n")
            for i in range(start_year1, end_year1+1):
                print("==> The {} {} in the year[{}] has fallen on: {}".format(month1,day1,i,weekdays[datetime(i,x.month,day1).isoweekday()]))

        else:
            print("\nPlease type 1 or 2 || Choosen option is not valid ||\n")
        print("------------------------------------------------------------")

    elif c=="10":
        add=input("\nEnter hours, that you wish to add in the current timings: \n\
In this format [XX:XX] | ")
        a=datetime.today()
        a1=a.strftime("%B %d %Y %I:%M")
        s=add.split(":")
        print(a.strftime("\n==> Today is: Date | [%A %B %d, %Y] Time | %I:%M%p\n"))
        add1=a+timedelta(hours=int(s[0]), minutes=int(s[1]))
        print("\n==> After adding {} hours, the new Date[{}] and Time | {}".format(add,add1.strftime("%A & %B %d, %Y"),add1.strftime("%I:%M %p")))
        print("------------------------------------------------------------")


    elif c=="Exit" or c=="EXIT" or c=="exit" or c=="e" or c=="E":
        print("\n--------------------------Application Exited--------------------------\n\
-------------------------------Thank You------------------------------\n")
        break
    else:
        print("\n\nIf you wish to Exit the application, please choose 'EXIT'\n")
        print("------------------------------------------------------------")

input()
#x=timedelta(seconds=360)
#print(x)  --> 0:06:00


# from datetime import datetime, date, timedelta
# import time

# ask1="Friday"
# # e=datetime.strptime(ask1,"%A")
# # print(e.strftime("%A"))


# c=input("Enter the weekday name: ")
# date8=datetime.now().strftime("%A")

# # print(date8.strftime("%w"))
# date1=time.strptime(c,"%A").tm_wday    #to get the number value of the weekday in string format (time.strptime("string",%A)).tm_wday
# date2=time.strptime(date8,"%A").tm_wday

# # for other example, refer(https://www.geeksforgeeks.org/isoweekday-method-of-datetime-class-in-python/)

# print("{}th day from now will be {}".format(abs(date1-date2),c))
# # x=date8.weekday()
# # print(x)
# # y=datetime.strptime(x,"%w")
# # y=datetime.(ask1,"%A")
# # print(y.strftime("%w"))
# # weekday=7-week
# # print("\nNumber of days left till {} is {}\n".format(ask1,weekday))




# names of different timezones
# ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Ciudad_Juarez', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Nelson', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CET', 'CST6CDT', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Kyiv', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NZ', 'NZ-CHAT', 'Navajo', 'PRC', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kanton', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Samoa', 'UTC', 'Universal', 'W-SU', 'WET', 'Zulu']
