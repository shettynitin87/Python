#Structure for a Node

class Node:
    #Constructor for a node
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    #Constructor to create an empty linked list
    def __init__(self):
        self.head = None

    #Function to insert a node at the begining of a Circular Linked List
    def push(self,data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        #If linked list is not none then set the next of last node
        if self.head != None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1
        self.head = ptr1

    #Function to print the nodes in the circular limked list
    def print_linked_list(self):
        temp = self.head
        requiredList = []
        if self.head != None:
            while(True):
                print(str(temp.data))
                temp = temp.next
                requiredList.append(temp.data)
                if (temp == self.head):
                    break
        return requiredList

#Function for bubble Sorting
def bubble_sort(sentList):
    for i in range(len(sentList)-1):
        for j in range(0, len(sentList)-i-1):
            if sentList[j] > sentList[j+1]:
                sentList[j],sentList[j+1] = sentList[j+1],sentList[j]

    return sentList

if __name__ == "__main__":
    #Initialize list of empty array
    cllist = CircularLinkedList()

    #Create a list
    cllist.push(23)
    cllist.push(4)
    cllist.push(7)
    cllist.push(12)
    cllist.push(99)

    print("Contents Of Circular List:")
    requiredList = cllist.print_linked_list()

    sorted_list = bubble_sort(requiredList)

    print("The Sorted List Is As Follows: "+ str(sorted_list))


