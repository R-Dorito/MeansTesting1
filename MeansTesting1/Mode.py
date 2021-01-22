import matplotlib.pyplot as plt
import numpy as np

class ModeClass:
#Add class name
# break the bottom part up
# Introduce matplot
# Graphically draw this up

    # This here collects all the unique values of a given list
    def createModeDictionary(numbersList, uniqueDictionary):       
        #newList = list(dict.fromkeys(listNum))
        # List of numbers and their frequencies
        numberDictionary = []

        # This counts how many times a value appears in the list
        for i in uniqueDictionary:
            modeOccurances = numbersList.count(i)        
            numberDictionary.append({'Value': i, 'Count': modeOccurances})
        print(numberDictionary)
        return numberDictionary

    # Used to find all values with "Largest Frequencies"
    def returnListOfModes(dictionaryMode):
        modeList = []
        frequency = 0
        for i in dictionaryMode:
            currentCount = i['Count']
            #print("Current Count is:", currentCount)
            if currentCount > frequency:
                frequency = currentCount
        print("Max Value is:", frequency)

        for i in dictionaryMode:
            currentComparison = i['Count']
            if frequency == currentComparison:
                modeList.append(i)
        print("There is", len(modeList), "Mode(s)")
        return modeList

    #draws a bar graph
    def drawModeGraph(dictionaryMode):
        x_Array = []
        y_Array = []
        for i in dictionaryMode:
            x_Array.append(i['Value']) 
            y_Array.append(i['Count'])

        x = np.array(x_Array)
        y = np.array(y_Array)
 
        plt.bar(x,y)
        plt.show()
        


