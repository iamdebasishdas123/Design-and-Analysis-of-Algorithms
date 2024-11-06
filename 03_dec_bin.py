def decimal_to_binary(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return decimal_to_binary(num // 2) + str(num % 2)

num = int(input("Enter a number: "))
print("Binary of", num, "is:", decimal_to_binary(num))