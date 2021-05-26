

#Fibonaci Function
def fibonaci_recurssion(count):
    if count <= 1:
        return count
    else:
        return (fibonaci_recurssion(count-1) + fibonaci_recurssion(count-2))


if __name__ == '__main__':
    count = 10
    for i in range(count):
        print(fibonaci_recurssion(i))