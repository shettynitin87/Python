

def is_palindrome(name):
    reversed_string = name.lower()[::-1]
    if(reversed_string == name.lower()):
         return True
    else:
        return False

if __name__ == "__main__":
    requiredName = input("Enter the name: ")
    if(is_palindrome(requiredName)):
        print("Yes, the entered name is palindrome")
    else:
        print("No, the entered name is not a palindrome")