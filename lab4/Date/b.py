import datetime
t=datetime.date.today()
tom=t+datetime.timedelta(days=1)
ysrt=t-datetime.timedelta(days=1)
print(ysrt,t,tom)