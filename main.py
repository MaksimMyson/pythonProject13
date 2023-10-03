def number(a):
    if a <= 1:
        return False
    if a <=3:
        return True
    for i in range (2, int(a**0.5)+1):
        if a % i == 0:
            return False

    return True
rezalt = number(10)
print(rezalt)
