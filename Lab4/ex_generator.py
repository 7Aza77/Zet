#task1
def generate_squares(n):
    for i in range(1, n):
        yield i**2


#task2
def generate_even_numbers(n):
    for i in range(0, n, 2):
        yield i


#task3
def generate_divisible_by_3_and_4(n):
    for i in range(1, n+1):
        if i % 3 == 0 or i % 4 == 0:
            yield i


def generate_squares_a_b(a, b): # включая b(?)
    for i in range(a, b):
        yield i**2


def generate_nymbers(n):
    for i in range(n+1):
        yield (i-n)*(-1)


N = int(input('Enter num: '))


squares_generator = generate_squares(N+1)
print('generates the squares of numbers:', end=' ')
for square in squares_generator:
    print(square, end=' ')


even_numbers = generate_even_numbers(N+1)
print('\neven numbers:', end=' ')
for even in even_numbers:
    print(even, end=', ')


devisible = generate_divisible_by_3_and_4(N)
print('\ndivisible by 3 and 4:', end=' ')
for devis in devisible:
    print(devis, end=' ')



square_a_b = generate_squares_a_b(4, 7)
print('\nsquares  all numbers from (a) to (b):', end=' ')
for a_b in square_a_b:
    print(a_b, end=' ')


numbers = generate_nymbers(N)
print('\nnumbers:', end=' ')
for num in numbers:
    print(num, end=' ')