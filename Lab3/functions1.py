#task1

def getounce(gram) :
    print( gram * 28.3495231)
    
#getounce(int(input()))


#task2

def getc(f) :
   a = 5/9
   b = f - 32
   print(a*b) 

#getc(int(input()))



#task3

def solve( numheads , numlegs) :
    chicken = (numlegs-2*numheads)/2
    rabbit = numheads - chicken
    print(chicken , rabbit)

#solve(35, 94)



#task4
def filter_prime(n):
    if n < 2:
        return 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return n

'''mylist = str(input())
numbers = mylist.split()
numbers = [num for num in numbers if filter_prime(int(num))]
print(numbers)'''

#task5
from itertools import permutations

def per():
    a = input("ENter here : ")
    perms= permutations(a)
    for perm in perms:
        print(''.join(perm))


'''per()'''

#task6
#task6
def reverse(a):
    words = a.split()
    i = len(words) - 1
    while i >= 0:
        print(words[i], end=' ')
        i -= 1
"""""
a = input('Enter text: ')
reverse(a)"""

#task7
def has_33(numbs):
    i = 0
    while i < len(numbs)-1:
        if numbs[i] == 3:
            if numbs[i+1] == 3:
                return True
        i += 1
    return False

'''numbers = input('Enter numbers: ')
numbs = numbers.split()
numbs = [int(num) for num in numbs]
print(has_33(numbs))'''


#task8

def spy_game(numbs):
    s = ''
    for i in numbs:
        s += i
    if '007' in s:
        return True
    return False

'''numbers = input('Enter numbers: ')
numbs = numbers.split()
print(spy_game(numbs))'''

#task9

def radius_volume(radius):
    sphera = 4/3*3.14*radius**3
    return sphera 
"""""
radius = int(input("Radius: "))
print(radius_volume(radius))"""""

#task10
def unique_elements(l):
    new_list = []
    i = 0
    while i < len(l):
        t_or_f = True
        j = 0
        while j < i:
            if l[i] == l[j]:
                t_or_f = False
            j += 1
        if t_or_f:
            new_list.append(l[i])
        i += 1
    return new_list

'''l = input('Enter elements: ')
elements = l.split()
new_list = unique_elements(elements)
print(new_list)'''

#task11
def palindrome(text):
    i = 0
    j = len(text)-1
    while i < len(text)/2:
        if text[i] != text[j]:
            return 'No palindrome'
        i+=1
        j-=1
    return 'palindrome'

'''text = input('Enter text: ')
print(palindrome(text))'''


#task12
def histogram(gist):
    i = 0
    while i < len(gist):
        j = 0
        while j < gist[i]:
            print('*', end='')
            j += 1
        print()
        i += 1

'''gist = input('Enter numbers: ')
gist = gist.split()
gist = [int(num) for num in gist]
histogram(gist)'''


#task13
import random

def find_num_random(rand_num, count):
    count += 1
    num = int(input('Take a guess.\n'))
    if num == rand_num:
        print(f'Good job, KBTU! You guessed my number in {count} guesses!')
        return
    print('\nYour guess is too low.')
    return find_num_random(rand_num, count)

'''name = input('Hello! What is your name?\n')
number = random.randint(1, 20)
count = 0
print(f'Well, {name}, I am thinking of a number between 1 and 20.\n')
find_num_random(number, count)'''

