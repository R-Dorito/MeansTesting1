from Mode import ModeClass
from Mean import MeanClass
from Median import MedianClass
from StandardDeviation import StandardDeviationClass
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
while i <= 10:
    listNumbers.append(random.randint(1, 7))
    i += 1

defineList(listNumbers)

#print(findMean(listNumbers))
#truncatedMean(listNumbers)
dictionaryMode = ModeClass.createModeDictionary(listNumbers, UNIQUELIST)
frequency = ModeClass.getMaxFrequency(dictionaryMode)
modes = ModeClass.findAllModes(dictionaryMode, frequency)
#print(modes)

#ModeClass.drawModeGraph(dictionaryMode)

mean = MeanClass.findMean(N, listNumbers)
StandardDeviationClass.sampleSD(N, mean, listNumbers)