import math
import enum

class SDType(enum.Enum):
    POPULATION = 0
    SAMPLE = 1

# Standard Deviation using sample and population:
class StandardDeviationClass():
    def standardDeviation(numItems, mean, listNum, type):
        totalSum = 0
        for i in listNum:
            totalSum += pow((i - mean), 2)

        sigma = math.sqrt(totalSum / (numItems - type.value))
        print("Standard Deviation type:", type.name, "is:", sigma)
        return sigma
    