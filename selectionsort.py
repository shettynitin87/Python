
#Function for selection sort
def selection_sort(requiredList):
    for i in range(len(requiredList)):
        min_index = i

        for j in range(i+1, len(requiredList)):
            if requiredList[min_index] > requiredList[j]:
                min_index = j

        #Swap the found min element with the first element
        requiredList[i],requiredList[min_index] = requiredList[min_index], requiredList[i]
    return requiredList

if __name__ == "__main__":
    requiredList = [20,30,12,55,76,88,10,91,44,5]
    sortedList = selection_sort(requiredList)

    print("The Sorted List= "+ str(sortedList))