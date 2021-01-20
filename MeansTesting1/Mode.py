class Mode:
#Add class name
# break the bottom part up
# Introduce matplot
# Graphically draw this up

    #This is a test Function
    def findMode(listNum):
        dictionaryMode = createModeDictionary(listNum)
        frequency = returnMaxFrequency(dictionaryMode)
        findAllModes(dictionaryMode, frequency)
        
    # This here collects all the unique values of a given list
    def createModeDictionary(listNum):       
        #newList = list(dict.fromkeys(listNum))
        # List of numbers and their frequencies
        numberDictionary = []

        # This counts how many times a value appears in the list
        for createCountList in UNIQUELIST:
            modeOccurances = listNum.count(createCountList)        
            numberDictionary.append({'Value': createCountList, 'Count': modeOccurances})
        return numberDictionary

    # Used to return the largest frequency
    def returnMaxFrequency(dictionaryMode):
        maxCount = 0
        for itterable in dictionaryMode:
            currentCount = itterable['Count']
            #print("Current Count is:", currentCount)
            if currentCount > maxCount:
                maxCount = currentCount
        print("Max Value is:", maxCount)
        return maxCount

    # Used to find all values with "Largest Frequencies"
    def findAllModes(dictionaryMode, frequency):
        modeList = []
        for currentValuesInDict in dictionaryMode:
            currentComparison = allValuesInDict['Count']
            if frequency == currentComparison:
                modeList.append(currentValuesInDict)
        print("There is", len(modeList), "Mode(s)")
        return modeList



