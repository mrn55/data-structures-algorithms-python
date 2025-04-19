def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase

    lines = []

    for i in range(size - 1, -1, -1):
        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        row = '-'.join(left + right)
        lines.append(row.center(4 * size - 3, '-'))

    for i in range(1, size):
        left = alpha[size-1:i:-1]
        right = alpha[i:size]
        row = '-'.join(left + right)
        lines.append(row.center(4 * size - 3, '-'))

    print('\n'.join(lines))

print_rangoli()