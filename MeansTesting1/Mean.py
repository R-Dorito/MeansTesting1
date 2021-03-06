class MeanClass:
    def findMean(numItems, listNum):
        sum = 0
        for i in listNum:
            sum += i
        mean = sum / numItems
        return mean

    def truncatedMean(listNum, uniqueList):
        truncatedList = uniqueList

        # There needs to be at least 3 values to run the truncated mean
        # If there isn't, then return the list/
        if len(truncatedList) >= 3:
            del truncatedList[len(truncatedList) - 1]
            del truncatedList[0]

        return findMean(truncatedList)

   


