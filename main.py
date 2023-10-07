def palidrome(a):
    if a == a[::-1]:
        return True
    else:
        return False
numbers = 123321
rezalt = palidrome(str(numbers))
print(rezalt)
