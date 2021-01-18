listNumbers = [0,1,1,1,2,2,4,4,7]

# Use this to define the properties of the list
def defineList(listNum):
    listNum.sort()
    
    global listLength 
    listLength = len(newList)


def findMean(listNum):
    sum = 0
    for i in listNum:
        sum += i
    average = sum / listLength

    return average

def truncatedMean(listNum):
    newList = list(dict.fromkeys(listNum))

    del newList[listLength - 1]
    del newList[0]

    return newList

def findMedian(listNum):
    lenList = len(listNum)
    # if odd do: x[(n+1)/2]
    # else do: ((x[n/s] + x[(n+1)/2])/2)





    
#findMean(listNumbers)
truncatedMean(listNumbers)