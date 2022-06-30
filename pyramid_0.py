pyramid_width = 7
for i in range(pyramid_width):
    for j in range(pyramid_width - i):
        print(" ", end='')
    for k in range(2 * i + 1):
        print("0", end='')
    print('')
