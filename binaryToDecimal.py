

def binaryToDecimal(requiredNumber):
    sum = 0
    mul_factor = 1
    requiredNumber = requiredNumber[::-1]

    for digit in requiredNumber:
        if digit == '1':
            sum = sum + mul_factor

        mul_factor = mul_factor * 2

    return sum


if __name__ == '__main__':
    requiredNumber = "11001101011"

    decimalNumber = binaryToDecimal(requiredNumber)

    print("The Binary Number Is: "+str(decimalNumber))