

#Function for Fibonaci series

def fibonaci(count):
    processed_set = []
    first = 0
    second = 1
    temp = 0

    for i in range(count):
        processed_set.append(first)
        temp = first + second
        first = second
        second = temp
    return processed_set

if __name__ == '__main__':
    count = 10
    required_set = fibonaci(count)

    print("The Required Set is: "+str(required_set))