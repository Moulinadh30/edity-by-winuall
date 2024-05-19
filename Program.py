def unique_values():
    input_array = []
    n = int(input("Enter the number of elements in the array: "))
    print("Enter the elements of the array:")
    for _ in range(n):
        element = int(input())
        input_array.append(element)
        
    unique_arr = []
    for value in input_array:
        if value not in unique_arr:
            unique_arr.append(value)
            
    print("Input array:", input_array)
    print("Output array with unique values:", unique_arr)

def isPalindrome():
    user_input = input("Enter a string to check if it is a palindrome: ")
    string = user_input.lower()
    left = 0
    right = len(string) - 1
    while left < right:
        if string[left] != string[right]:
            print("The string is not a palindrome.")
            return
        left += 1
        right -= 1
    print("The string is a palindrome.")

def factorial():
    n = int(input("Enter a number to calculate its factorial: "))
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Uncomment the function you want to use
# unique_values()
#isPalindrome()
print(factorial())
