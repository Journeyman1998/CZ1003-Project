# An utility Date/Time class
# Coded by Jun Wei
# Some methods may not be used in program

import datetime
import calendar

DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
DAYS_SHORT = ("Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun")

#takes time integer and return the Time object
def convertIntToTime(timeInInt):
    hour = timeInInt // 100
    minute = timeInInt % 100
    return datetime.time(hour, minute)

# takes Time object and return the integer representation
def convertTimeToInt(time):
    hour = time.hour
    minute = time.minute
    return hour * 100 + minute

# takes day integer and return the name of day
def getDayString(dayNum):
    return DAYS[dayNum]

# takes time integer and return the string representation
def getTimeString(time):
    hour = time // 100
    minute = time % 100
    suffix = ""
    suffix = " AM" if hour < 12 else  " PM" 
    if hour > 12:
        hour = hour - 12
    return "{}.{}{}".format(hour, str(minute).zfill(2), suffix)

# to get the day of a certain date
# takes Date object
def getDayNum(date):
    y = date.year
    m = date.month
    d = date.day
    return calendar.weekday(y, m, d) + 1 # bcos 0 is Mon

#to show full date and time 
def getDateTimeString(date, time):
    dateString = date.isoformat()
    timeString = time.isoformat(timespec='auto')
    return "{}, {}".format(dateString, timeString)


# Takes year, month, day (int) and returns Date object, default return is current date
def getDate(year=-1, month=-1, day=-1):
    if year == -1:
        now = datetime.datetime.now()
        return datetime.date(now.year, now.month, now.day)
    else:
        return datetime.date(year, month, day)


# Takes hour, min, sec (int) and returns time object, default return is current time
def getTime(hour=-1, minute=-1, second=-1):
    if hour == -1:
        now = datetime.datetime.now()
        return datetime.time(now.hour, now.minute, now.second)
    else:
        return datetime.time(hour, minute, second)

