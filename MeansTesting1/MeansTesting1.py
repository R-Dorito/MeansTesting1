listNumbers = [0,1,1,1,2,2,4,4,7]

def findMean(listNum):
    sum = 0
    for i in listNum:
        sum += float(i)

    count = float(len(listNum))
    return sum/count

def truncatedMean(listNum):
    newList = list(dict.fromkeys(listNum))
    newList.sort()

    lastNumberOfList = len(newList) - 1

    del newList[lastNumberOfList]
    del newList[0]

    return newList

def findMedian(listNum):
    lenList = len(listNum)
    # if odd do: x[(n+1)/2]
    # else do: ((x[n/s] + x[(n+1)/2])/2)



    
#findMean(listNumbers)
truncatedMean(listNumbers)