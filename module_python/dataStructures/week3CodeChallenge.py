# CHALLENGE 1

def large_power(base, exponent):
    result  = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    
print(large_power(11, 22))

# CHALLENGE 2
def divisible_by_10(num):
    if num % 10 == 0:
        return True
    else:
        return False
print(divisible_by_10(11))