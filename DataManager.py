import Time  # for processing time-based values

# Provides functions that the GUI will use. 
# Almost all processing is done in this module. GUI will only display info or check errors
# Coded by Jun Wei
class DataManager():

    def __init__(self, data):
        f = open("log.txt", "a")
        try:
            self.stallInfo = data["stall_info"]
        except:
            print("Error getting stall info", file=f)

        try:
            self.foodInfo = data["food_info"]
        except:
            print("Error getting food info", file=f)
    
        try:
            self.opHour = data["operating_hour"]
        except:
            print("Error getting opHour info", file=f)

        try:
            self.opHourString = data["operating_hour_string"]
        except:
            print("Error getting opHourString info", file=f)

        f.close()
        
    # return a dictionary of {<id>: <name of stall>}
    # default - return all stalls if no day-time specified, or else return based on day-time and operating hours
    # Takes Date and Time object
    def getStallList(self, date=-1, timeObj=-1):
        toRet = {}

        # Default return
        if date == -1 and timeObj == -1: 
            for i in self.stallInfo:
                toRet[i] = self.stallInfo[i][0]
        # Based on date, time
        else:
            day = Time.getDayNum(date)
            time = Time.convertTimeToInt(timeObj)
            indexToCheck = day * 2
            for i in self.stallInfo:
                if self.opHour[i][indexToCheck] <= time and time <= self.opHour[i][indexToCheck+1]: # Checks operating hours
                    toRet[i] = self.stallInfo[i][0]

        return toRet


    def getStallOperatingHoursString(self, name: str):
        return self.opHourString[name]


    # Returns the queue time based on the factor and length of queue
    def getQueueTime(self, id, number):
        return self.stallInfo[id][1] * number

    # Collects food available at date, time set, and returns the collection (list)
    # Takes Time, Date object
    def getMenu(self, id, date, time):
        menu = self.foodInfo[id] # all the food from the stall, list of tuples
        menuToDisplay = []

        # Gets all food from the stall if no time and date specified
        if date == None and time == None: 
            for food in menu:
                menuToDisplay.append({"name": food[0], "price": food[1], "id": food[5]})
            return menuToDisplay
        
        # Gets food based on time and date specified
        # Checks if startTime and endTime of food is between specified time
        for food in menu:
            if Time.getDayNum(date) in food[4] and Time.convertIntToTime(food[2]) <= time and time <= Time.convertIntToTime(food[3]):
                menuToDisplay.append({"name": food[0], "price": food[1], "id": food[5]}) 
        
        return menuToDisplay

    def getMealTimeDict(self, id):
        return self.stallInfo[id][2]