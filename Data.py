import ast
import json
from collections import OrderedDict

LOOKUP = {"Mon": 0, "Monday": 0, "Tue": 1, "Tues": 1, "Tuesday": 1, "Wed": 2, "Wednesday": 2, "Thu": 3, "Thur": 3, "Thurs": 3, "Thursday": 3,
          "Fri": 4, "Friday": 4, "Sat": 5, "Saturday": 5, "Sun": 6, "Sunday": 6, "PH": 7, "Public Holidays": 7, "Public Holiday": 7}

# Parses 1st line of stall data into tuple storing the info
# Helper function for getData()
# Coded by Xuege
def parseStallInfo(data):

    stallInfo = data[0].rstrip().split(";")
    # load different mealtimes for the stall
    timeSectDict = json.loads(stallInfo[2])
    timeSect = OrderedDict(timeSectDict)
    # name, queue-factor, mealtimes (ordered dictionary)
    try:
        return (stallInfo[0], int(stallInfo[1]), timeSect)
    except:
        return (stallInfo[0], 1, timeSect)


# Obtain operating hours of stall based on different file inputs (more flexible)
# Parse the data passed in from the text file (second line)
# Helper function for getData()
# Coded by Xuege and Jun Wei
def parseOperatingHours(data):

    operationDictionaryString = []  # for use in displaying operating hours
    opHour = 16 * [-1]  # for use in stall and menu display code. -1 => closed

    # Pops the used lines from data files
    data.pop(0)
    data.pop(0)


    while data[0].rstrip('\n') != "*": # Checks for the * that signals end of operating hours info
        string = data[0].rstrip('\n').split(':') # Splits Days and Time
        data.pop(0) # Pop whenever line is not needed anymore
        operationDictionaryString.append(
            (string[0].strip(), string[1].strip())) # Used for displaying in opHour window

        # Code below to retrieve operation hours of each day (cannot use String for comparison and processing)
        # Lookup dictionary above to convert Day String into Day Numbers
        # Maybe can use "in" to retrieve days since each day has a unique portion of char (i.e Mon, Tue, Sat, etc)

        days = string[0].split(',')  # Splits by ranges of days (Mon - Wed) or individual days
        time = string[1].split('to') # Splits time string into 2 parts

        # If closed, both time will be -1
        if time[0].strip() != "Closed":
            try:
                startTime = int(time[0])
            except:
                startTime = 0
            
            try:
                endTime = int(time[1])
            except:
                endTime = 2359
        else:
            startTime = -1
            endTime = -1


        for i in range(len(days)):
            day = days[i].strip()
            if(day == "Weekends"): # Check if shorthand "Weekends" is used
                opHour[10] = startTime
                opHour[11] = endTime
                opHour[12] = startTime
                opHour[13] = endTime
            elif(day == "Weekdays"): # Check if shorthand "Weekdays" is used
                for i in range(0, 6):
                    opHour[2*i] = startTime
                    opHour[2*i+1] = endTime
            elif(len(day.split("-")) == 1): # Check if it is an individual day
                numDay = LOOKUP[day]
                opHour[2*numDay] = startTime
                opHour[2*numDay+1] = endTime
            else:  # it is a range of days
                dayRange = day.split("-")
                numStart = LOOKUP[dayRange[0].strip()]
                numEnd = LOOKUP[dayRange[1].strip()]
                for i in range(numStart, numEnd+1):
                    opHour[2*i] = startTime
                    opHour[2*i+1] = endTime
    data.pop(0) # Pop the final "*"
    return operationDictionaryString, opHour


# Parse the food data passed in
# Returns a list of tuple
# Helper function for getData()
# Coded by Xuege
def parseFoodInfo(data):
    foodList = []
    for i in range(len(data)):
        foodData = data[i].rstrip().split(";") # Splits the line of each food
        dayList = ast.literal_eval(foodData[4]) # Converts into a list using ast.literal.eval()

        # tuple: name, price, startTime, endTime, dayList, id(photo)
        try:
            food = (foodData[0], float(foodData[1]), int(foodData[2]), int(foodData[3]), dayList, foodData[5])
        except:
            food = (foodData[0], 0.0, 0, 0, dayList, foodData[5])
            
        foodList.append(food)

    return foodList


# Parses data from database files
# Returns a dictionary (Stalls)
# id: (name<string>,queuefactor<int>,{"timesec_1":time<int>})
#
# Return a dictionary (Food)
# id: [(name<string>, price<float>, startTime<int>, endTime<int>, [dayList<int>], food_id), (food2), ...]

# Returns a dictionary of list (Operating Hours)
# operatingList["<id>"][2n / 2n+1] for start and end respectively

# Returns a dictionary of list (Operating Hours string for GUI display)
# operatingList["<name>"] for each stall
# Coded by Xuege and Jun Wei

def getData(filename):

    try:
        meta = open(filename, "r").read().splitlines()
    except:
        raise FileNotFoundError

    root = meta[0].split("=")[1].rstrip() # Find where to locate stall data files
   
    stallInfo = {}
    stallFood = {}
    operatingHour = {}
    operatingHourString = {}
    
    try:
        length = int(meta[1].split("=")[1].rstrip()) # Number of stall data files to be expected
    except:
        return {"stall_info": stallInfo, "food_info": stallFood, "operating_hour": operatingHour, "operating_hour_string": operatingHourString}


    logfile = open("log.txt", "a")
    print("*Program running*", file=logfile)

    for i in range(1, length+1):  # files start from 1.txt onwards

        filename = root + str(i) + ".txt"
        try:
            data = open(filename, "r").read().splitlines()
        except:
            print("{} not found".format(filename), file=logfile)
            continue

        data = open(filename, "r").read().splitlines()
        stall_info = parseStallInfo(data)  # passes in first line of data (info)
        nameOfStall = stall_info[0]
        operatingString, operatingList = parseOperatingHours(data)
        foodList = parseFoodInfo(data)

        # initialising the dictionary for each stall
        stallInfo[i] = stall_info
        stallFood[i] = foodList
        operatingHour[i] = operatingList
        operatingHourString[nameOfStall] = operatingString
    
    logfile.close()
    return {"stall_info": stallInfo, "food_info": stallFood, "operating_hour": operatingHour, "operating_hour_string": operatingHourString}
