from itertools import permutations

def print_permutations():
    text = input("Enter text: ")
    perms = permutations(text)
    for perm in perms:
        print(''.join(perm))


print_permutations()