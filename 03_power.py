def power_of_number(num,power):
    if power==0:
        return 1
    else:
        return num * power_of_number(num,power-1)
    
num = int(input("Enter the number:"))
pow = int(input("Enter the power:"))

print(num,"^",pow," = ",power_of_number(num,pow))