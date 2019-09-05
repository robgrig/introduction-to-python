import datetime
import time
import calendar

date_of_birth=datetime.date(1996 , 12 ,16)
print(date_of_birth)

print('Year: ', date_of_birth.year)

print('Month: ', date_of_birth.month)

print('Day: ', date_of_birth.day)

print('Day of the week (version 1): ', date_of_birth.isoweekday())

tday = datetime.date.today()
print(tday)

bday=datetime.date(2019 , 12 , 16)
 
mnac=bday-tday
print(mnac)

cal = calendar.month(2017, 5)
print ("Here is the calendar:")
print (cal)

currentDT = datetime.datetime.now()
 

#print ("Current Day is: %d" % currentDT.day)
#print ("Current Hour is: %d" % currentDT.hour)
#print ("Current Minute is: %d" % currentDT.minute)

tdelta = datetime.timedelta(days = 1)
print( tday-tdelta, currentDT.hour , currentDT.minute)

print( tday+tdelta)

tdelta = datetime.timedelta(days = 4)
print( tday-tdelta)