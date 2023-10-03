def if_number_is_happy(number):
    if number < 10000 or number > 999999:
        return False
    thry_first = number // 1000
    thry_second = number % 1000
    if thry_first == thry_second:
        return True
    return False
rezalt = if_number_is_happy(123123)
print(rezalt)

