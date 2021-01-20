class MedianClass:
     def findMedian(listNum):
        # if odd do: x[(n+1)/2]
        # where x is a set and 
        # n is the number of elements
        # else do: ((x[n/2] + x[(n+1)/2])/2)

        if (N % 2) != 0:
            #print("its odd")
            # Although the formula states the n+1/2 should be done, 
            # it does not work well in this case
            location = (N) / 2
            median = listNum[int(location)]
        else:
            #print("it's even")
            # Get the value of the first and second median number
            location1 = listNum[int((N - 1) / 2)] 
            #print("L1:", location1, "at:",int((LISTLENGTH) / 2))
        
            location2 = listNum[int((N) / 2)]
            #print("L2:", location2, "at:", int((LISTLENGTH - 1) / 2))

            median = (location1 + location2) / 2

        print("the median is:", median)
        return median
