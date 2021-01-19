# Use this to define the properties of the list
def defineList(listNum):
    global LISTLENGTH 
    listNum.sort()
    LISTLENGTH = len(listNum)

def findMean(listNum):
    sum = 0
    for i in listNum:
        sum += i
    average = sum / LISTLENGTH
    return average

def truncatedMean(listNum):
    newList = list(dict.fromkeys(listNum))
    del newList[len(newList) - 1]
    del newList[0]
    return newList

def findMedian(listNum):
    # if odd do: x[(n+1)/2]
    # where x is a set and 
    # n is the number of elements
    # else do: ((x[n/2] + x[(n+1)/2])/2)

    if (LISTLENGTH % 2) != 0:
        print("its odd")

        # Although the formula states the n+1/2 should be done, 
        # it does not work well in this case
        location = (LISTLENGTH) / 2
        median = listNum[int(location)]
    else:
        #print("it's even")
        
        # Get the value of the first and second median number
        location1 = listNum[int((LISTLENGTH - 1) / 2)] 
        #print("L1:", location1, "at:",int((LISTLENGTH) / 2))
        
        location2 = listNum[int((LISTLENGTH) / 2)]
        #print("L2:", location2, "at:", int((LISTLENGTH - 1) / 2))

        median = (location1 + location2) / 2

    print("the median is:", median)
    return median

def findMode(listNum):
    # This here collects all the unique values of a given list
    newList = list(dict.fromkeys(listNum))

    numberDictionary = []

    # This counts how many times a value appears in the list
    for i in newList:
        modeOccurances = listNum.count(i)
        toAddToDictionary = {'Value': i, 'Count': modeOccurances}
        numberDictionary.append(toAddToDictionary)

    # Return the largest value

    print(numberDictionary)



listNumbers = [1, 1, 2, 6, 6, 9, 9, 9 ]
defineList(listNumbers)

#findMean(listNumbers)
#truncatedMean(listNumbers)
findMode(listNumbers)