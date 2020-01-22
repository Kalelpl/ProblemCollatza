def collatz(x):
    if (x % 2) == 0:
        return x //2
    elif (x % 2) == 1:
        return (3 * x + 1)

# print('Enter a number:')

try:
    x = int(raw_input('Please Provide a number'))
    while collatz(x):
        x = collatz(x)
        print(x)
        if x == 1:
            print('Success!')
            break
except ValueError:
    print('Please provide a number')

