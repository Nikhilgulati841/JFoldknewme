from datetime import datetime, timedelta, date

goal="26/10/2024 10:00pm"

x=datetime.now()
y=datetime.strptime(goal,"%d/%m/%Y %I:%M%p")
a=abs(y-x)
print(a)