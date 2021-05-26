

def find_the_middle_element(requiredList):
    for count in range(0,len(requiredList)):
        if count == len(requiredList)-1:
            if count % 2 == 0:
                return int(count/2)
            else:
                return int(count/2)+1


if __name__ == "__main__":
    requiredList = [1,2,3]
    requiredElement = find_the_middle_element(requiredList)
    print("The Required Element is= "+ str(requiredList[requiredElement]))

    #removing the element from the array
    del requiredList[requiredElement]

    print("The list after removing= "+str(requiredList))