def create_square(side_length, character, filled):
    if filled:

        for _ in range(side_length):
            row = character * side_length
            print(row)
    else:

        for row in range(side_length):
            if row == 0 or row == side_length - 1:
                square_row = character * side_length
            else:
                square_row = character + " " * (side_length - 2) + character
            print(square_row)


side_length = 5
character = "*"
filled = True

create_square(side_length, character, filled)