from Mode import ModeClass
from Mean import MeanClass
from Median import MedianClass
from StandardDeviation import SDType
from StandardDeviation import StandardDeviationClass

from numpy import random
import tkinter as tk


# This is a program that returns a Mean, Median, Mode, Standard Deviation a

## Use this to define the properties of the list
#def defineList(listNum):
#    # N is the number of items in the set
#    global N 
#    global UNIQUELIST

## Test
#listNumbers = []
#i = 0
#while i <= 10:
#    listNumbers.append(random.randint(1, 7))
#    i += 1

#N = len(listNumbers)
#UNIQUELIST = list(dict.fromkeys(listNumbers))
#UNIQUELIST.sort()

##defineList(listNumbers)

##print(findMean(listNumbers))
##truncatedMean(listNumbers)
#dictionaryMode = ModeClass.createModeDictionary(listNumbers, UNIQUELIST)
#modes = ModeClass.returnListOfModes(dictionaryMode)
##print(modes)

##ModeClass.drawModeGraph(dictionaryMode)

#mean = MeanClass.findMean(N, listNumbers)
#print(listNumbers)
#StandardDeviationClass.standardDeviation(N, mean, listNumbers, SDType.SAMPLE)
#StandardDeviationClass.standardDeviation(N, mean, listNumbers, SDType.POPULATION)

window = tk.Tk()
window.title('Plotting in Tkinter')

# run the gui 
window.mainloop()