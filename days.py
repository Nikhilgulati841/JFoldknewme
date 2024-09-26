from datetime import datetime, date, timedelta

def day():
    add=int(input("Enter the days you have planned to be added today: "))
    currentdate=datetime.today()
    daysadd=currentdate+timedelta(days=add)
    p=daysadd.strftime("\n==>Today is {} \n\
    After {} days from now, the day will be %A and the date[%B %d, %Y]\n".format(currentdate.strftime("%A and the date[%B %d, %Y]"),add))
    print(p.upper())
    print("------------------------------------------------------------")
    return "Code ran successfully with 0 error"

    
