#Dates are worked upon by importing modules like datetime ,time and calendar.

#time module
import time
print(time.time()) #no of ticks since 12AM,1st Jan 1970

print(time.localtime(time.time())) #return a time tuple

print(time.asctime(time.localtime(time.time()))) #time can be formatted by asctime() method

#sleep() method for delay
for i in range(0,5):
    print(i)
    #time.sleep(1) #delays for 1 second every time loop works


#datetime module
import datetime
print(datetime.datetime.now()) #formatted date

print(datetime.datetime(2020,4,4)) #returns datetime object for specified date
print(datetime.datetime(2020,4,4,1,26,40)) #specified date with time 

#comparison of dates
from datetime import datetime as dt
if(dt(dt.now().year,dt.now().month,dt.now().day) >dt(1990,5,12)):
  print("After 1990")
#here these three arguments (year,month,day) are essential in dt 


#calendar module
import calendar
cal=calendar.month(2020,12) #prints the calendar for specified year and month 
print(cal)

s=calendar.prcal(2020) #print calendar for whole year specified