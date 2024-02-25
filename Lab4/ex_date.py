from datetime import datetime , timedelta 
#task1

x = datetime.now() - timedelta(days=5)
y = x.strftime("%A")
print(x,y)


#task2
x = datetime.now() + timedelta(days=1)
x2 = datetime.now() - timedelta(days=1)
x3 = datetime.now()
y = x.strftime("%A")
y2 = x2.strftime("%A")
y3 = x3.strftime("%A")
print(x,y)
print(x2,y2)
print(x3,y3)

