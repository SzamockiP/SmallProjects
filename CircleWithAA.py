density = 10

x_matrix = 50 * density
y_matrix = 50 * density

ascii_values = {
    0.0: ' ',
    0.1: '.',
    0.2: ',',
    0.3: ':',
    0.4: '!',
    0.5: '=',
    0.6: '#',
    0.7: '%',
    0.8: '&',
    0.9: '$',
    1.0: '@',
}

matrix = [['@' for i in range(x_matrix)] for j in range(y_matrix)]


def elipse_add(x, y, a, b, elipse_middle):
    if ((x - elipse_middle[0]) / b ** 2) ** 2 + ((y - elipse_middle[1]) / a ** 2) ** 2 <= 1:
        return 1
    else:
        return 0


def elipse_sub(x, y, a, b, elipse_middle):
    if ((x - elipse_middle[0]) / b ** 2) ** 2 + ((y - elipse_middle[1]) / a ** 2) ** 2 <= 1:
        return 0
    else:
        return 1


def rectangle_sub(x, y, p_1, p_2):
    if p_1[0] < x < p_2[0]:
        if p_1[1] < y < p_2[1]:
            return 0
        else:
            return 1
    else:
        return 1


for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
        if matrix[x][y] != 0:
            matrix[x][y] = rectangle_sub(x, y, (150, 150), (350, 350))
        if matrix[x][y] != 0:
            matrix[x][y] = elipse_sub(x, y, 7, 10, (250, 150))
        if matrix[x][y] != 0:
            matrix[x][y] = elipse_sub(x, y, 10, 6, (315, 340))
        if matrix[x][y] != 0:
            matrix[x][y] = elipse_sub(x, y, 10, 6, (185, 340))
        if matrix[x][y] != 0:
            matrix[x][y] = elipse_sub(x, y, 8, 6, (350, 260))
        if matrix[x][y] != 1:
            matrix[x][y] = elipse_add(x, y, 5, 8, (250, 170))

round_sum = 0

display_matrix = [['' for i in range(int(x_matrix / density))] for j in range(int(y_matrix / density))]  # deklaracja tablicy ASCII
for x in range(int(x_matrix / density)):
    for y in range(int(y_matrix / density)):
        for x_p in range(x * density, x * density + density):
            for y_p in range(y * density, y * density + density):
                round_sum += matrix[x_p][y_p]
        round_sum = round(round_sum / density / density, 1)
        display_matrix[y][x] = round_sum

for x in range(0, len(display_matrix)):
    for y in range(0, len(display_matrix[x])):
        display_matrix[x][y] = ascii_values[display_matrix[x][y]]

for x in display_matrix:
    for y in x:
        print(y, end=' ')
    print()

input()
