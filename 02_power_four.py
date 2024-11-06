def is_power_four(num):
    if num == 1:
        return True
    elif num < 1 or num % 4 != 0:
        return False
    else:
        return is_power_four(num/4)
    
print(is_power_four(65))