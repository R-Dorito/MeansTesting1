from Mode import ModeClass
from Mean import MeanClass
from Median import MedianClass
from DrawMode import DrawModeClass
from numpy import random


# This is a program that returns a Mean, Median, Mode, Standard Deviation a

# Use this to define the properties of the list
def defineList(listNum):
    # N is the number of items in the set
    global N 
    global UNIQUELIST

    listNum.sort()
    N = len(listNum)

    UNIQUELIST = list(dict.fromkeys(listNum))


# Test
listNumbers = []
i = 0
while i <= 20:
    listNumbers.append(random.randint(6))
    i += 1

defineList(listNumbers)

#print(findMean(listNumbers))
#truncatedMean(listNumbers)
dictionaryMode = ModeClass.createModeDictionary(listNumbers, UNIQUELIST)
frequency = ModeClass.getMaxFrequency(dictionaryMode)
modes = ModeClass.findAllModes(dictionaryMode, frequency)
#print(modes)

DrawModeClass.drawModeGraph(dictionaryMode)