import matplotlib.pyplot as plt
import numpy as np

class DrawModeClass():

    #draws a bar graph
    def drawModeGraph(dictionaryMode):
        x_Array = []
        y_Array = []
        for i in dictionaryMode:
            x_Array.append(i['Value']) 
            y_Array.append(i['Count'])

        x = np.array(x_Array)
        y = np.array(y_Array)
 
        plt.bar(x,y)
        plt.show()