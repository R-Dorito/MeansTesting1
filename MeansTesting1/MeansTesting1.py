listNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def findMean(listNum):
    sum = 0
    for i in listNum:
        sum += float(i)

    count = float(len(listNum))
    return sum/count

def truncatedMean(listNum):


# findMean(listNumbers)