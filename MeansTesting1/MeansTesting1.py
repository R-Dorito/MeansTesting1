from Mode import ModeClass
from Mean import MeanClass
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
listNumbers = [1, 3, 2, 3, 4, 4, 2, 2, 2, 3, 3]
defineList(listNumbers)

#print(findMean(listNumbers))
#truncatedMean(listNumbers)
dictionaryMode = ModeClass.createModeDictionary(listNumbers, UNIQUELIST)
frequency = ModeClass.getMaxFreq(dictionaryMode)
modes = ModeClass.findAllModes(dictionaryMode, frequency)
print(modes)