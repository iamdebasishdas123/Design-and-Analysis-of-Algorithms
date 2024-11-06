def reverse_num(num):
    if num//10 == 0:
        return num
    return str((num % 10)) + str(reverse_num(num//10))

n = int(input("Enter a number: "))
print("Reversed number is-- ",reverse_num(n))