def factorial(n):
    result = 1
    for i in range (1,n+1):
        result *=i
        
    return result

# call the function with a sample number

sample_number = 5
print("Factorial of ", sample_number, " is :", factorial(sample_number))