def product(a,b):
    if a == 1:
        return b
    elif b == 1:
        return a
    else:
        return a + product(a,b-1)
    
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

print(num1,"X",num2," = ",product(num1,num2))