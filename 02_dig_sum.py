def summation_digits(num):
    if(num//10 == 0):
        return num
    else:
        return (num % 10) + summation_digits(num//10)
    
print("\n\nSum of digits is: ",summation_digits(641))