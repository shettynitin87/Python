

def multiply(n):
    return lambda a: a * n

if __name__ == '__main__':

    result = multiply(10)
    print(result(5))