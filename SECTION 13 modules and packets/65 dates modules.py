#date modules

#this module is in python by default    
import datetime

#show today date
print(datetime.date.today())

#to get complete date
completeDate = datetime.datetime.now()
print(completeDate)
print(completeDate.year) #show year
print(completeDate.month) #show month
print(completeDate.day) #show day

# to custom date
customDate = completeDate.strftime('%d/%m/%Y, %H:%M:%S')
print(customDate)

#getting time in other format
print(datetime.datetime.now().time())

