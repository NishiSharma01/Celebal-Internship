def print_rangoli(size):
    # your code goes here
    import string
    alpha = string.ascii_lowercase
    width = 4 * size - 3
    lines = []

    
    for i in range(size - 1, -size, -1):
        s = alpha[size - 1:abs(i):-1] + alpha[abs(i):size]
        lines.append('-'.join(s).center(width, '-'))

    print('\n'.join(lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)