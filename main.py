def dobytok(межа1, межа2):
    bottom = min(межа1, межа2)
    top = max(межа1, межа2)
    product = 1
    for number in range(bottom, top + 1):
        product *= number
    return product
rezalt = dobytok(1, 3 )
print("Добуток у діапазоні:", rezalt)