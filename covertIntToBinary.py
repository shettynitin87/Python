
binary = []
def convert_int_to_binary(number):
    if number == 1:
        binary.append(1)
    elif number == 0:
        binary.append(0)
    else:
        x,y = divmod(number, 2)
        binary.append(y)
        convert_int_to_binary(x)


if __name__ == "__main__":
    number = input("Enter the number: ")
    convert_int_to_binary(int(number))
    print("The required binary is {} for {}".format(binary[::-1], number))