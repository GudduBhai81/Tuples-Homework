def multiply_tuple_elements(numbers):
    product = 1
    for number in numbers:
        product *= number
    return product

# Example usage
numbers_tuple = (2, 3, 4)
result = multiply_tuple_elements(numbers_tuple)
print("The product of the numbers in the tuple is:", result)