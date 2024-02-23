import datetime

x = datetime.datetime.now()
y=x.time()

print(y.strftime("%H:%M:%S"))