def even_numbers(a, b):
    for number in range(a + 1, b):
        if number % 2 == 0:
            print(number)

even_numbers(10, 15)