def odd_numbers_between(a, b):
    for number in range(a + 1, b):
        if number % 2 != 0:
            print(number)

odd_numbers_between(1, 10)

