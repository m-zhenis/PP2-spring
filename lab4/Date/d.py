import datetime

x = datetime.datetime.now()
y=datetime.datetime(2030,5,3,2,1,8)
dif=x-y


print(dif.total_seconds())