def get_factorial(number: int):
    result = 1
    for num in range(1,number+1):
        result *= num
    return result

an_integer = int(input("Enter an integer : "))
print(get_factorial(an_integer))

