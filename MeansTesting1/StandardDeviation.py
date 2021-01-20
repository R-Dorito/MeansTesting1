import math

# Standard Deviation using sample and population:
class StandardDeviationClass():
    def sampleSD(numItems, mean, listNum):
        totalSum = 0
        for i in listNum:
            totalSum += pow((i - mean), 2)
        sigma = math.sqrt(totalSum / (numItems - 1))
        print("Standard Deviation:", sigma)
        return sigma
        