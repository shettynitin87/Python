

#Function for bubble Sorting
def bubble_sort(sentList):
    for i in range(len(sentList)-1):
        for j in range(0, len(sentList)-i-1):
            if sentList[j] > sentList[j+1]:
                sentList[j],sentList[j+1] = sentList[j+1],sentList[j]

    return sentList

if __name__ == "__main__":
    sentList = [20,30,12,55,76,88,10,91,44,5]
    sorted_list = bubble_sort(sentList)

    print("The Sorted List Is As Follows: "+ str(sorted_list))