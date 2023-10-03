def draw_line  (lenght, direction, symbol):
    if direction == "Горизонтальна":
        line = symbol * lenght
    elif direction == "Вертикальна":
            line = "\n".join([symbol] * lenght)
    else:
        return "Невірний напрямок"
    print(line)

draw_line(5, "Горизонтальна", "*")
draw_line(5, "Вертикальна", "$")



