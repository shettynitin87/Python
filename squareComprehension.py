'''
Method to Calulate the Square
'''


def square(requiredList):
    squaredList = {x: x ** 2 for x in requiredList}
    return squaredList


if __name__ == "__main__":
    requiredList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    squaredList = square(requiredList)

    # Printing the required list
    for values in squaredList.values():
        print(values)
