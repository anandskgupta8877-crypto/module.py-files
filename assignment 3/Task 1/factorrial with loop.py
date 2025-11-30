def factorial(n):
    result =1
    for i in range(1,n+1):
        result *=i
        
    return result

num = int(input("Enter the number:"))
print("factorial of ",num ,"is:",factorial(num))