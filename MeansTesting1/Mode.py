class Mode(object):
#Add class name
# break the bottom part up
# Introduce matplot
# Graphically draw this up

    def findMode(listNum):
        # This here collects all the unique values of a given list
        #newList = list(dict.fromkeys(listNum))

        # List of numbers and their frequencies
        numberDictionary = []

        # This counts how many times a value appears in the list
        for createCountList in UNIQUELIST:
            modeOccurances = listNum.count(createCountList)        
            numberDictionary.append({'Value': createCountList, 'Count': modeOccurances})

        # Used to return the largest frequency
        maxCount = 0
        modeList = []
        for itterable in numberDictionary:
            currentCount = itterable['Count']
            #print("Current Count is:", currentCount)
            if currentCount > maxCount:
                maxCount = currentCount
        print("Max Value is:", maxCount)

        # Used to find all values with "Largest Frequencies"
        for theMode in numberDictionary:
            currentComparison = theMode['Count']
            if maxCount == currentComparison:
                modeList.append(theMode)
    
        print("There is", len(modeList), "Mode(s)")



