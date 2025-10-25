def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(12))
print(is_prime(2))
print(is_prime(1))