def draw_right_angled_triangle(rows):
    for row in range(rows):
        print("*" * (row+1))


def square_wtih_hollow_center(num):
    for row in range(num):
        for column in range(num):
            if row == 0 or row == 5 - 1:
                print("*", end="")
            elif column == 0 or column == 5-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


def expression(index):
    return " " * ((5 - index) // 2) + "*" * index + " " * ((5 - index) // 2)


def diamond(num):
    if num % 2 != 0:
        for i in range(1, num + 1, 2):
            print(expression(i))

        for i in range(num - 2, 0, -2):
            print(expression(i))
    else:
        print("Please enter an odd number")
