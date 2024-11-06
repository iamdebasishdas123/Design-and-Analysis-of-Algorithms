def summ(num):
    if num == 1:
        return 1
    else:
        return num + summ(num - 1)
    
n = int(input("Enter the natural number: "))
print(f"Sum of first {n} natural numbers is {summ(n)}")