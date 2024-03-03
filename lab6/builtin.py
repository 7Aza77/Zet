import  math

#task1 
'''
list = []
m = int(input())
for i in range(m) :
    n = int(input())
    list.append(n)
print(math.prod(list))
'''

#task2
'''''
def string(string):
    upper_c = sum(1 for char in string if char.isupper())
    lower_c = sum(1 for char in string if char.islower())
    return upper_c,lower_c
    
word = str(input())
upper_c = string(word)
lower_c = string(word)
print(upper_c)
print(lower_c)
'''

#task3
def is_palindrome(s):
    
    s = s.replace(" ", "").lower()
   
    return s == s[::-1]


string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome.")

#task4
import time
import math

def square_root_after_delay(number, milliseconds):
    time.sleep(milliseconds / 1000)  # Convert milliseconds to seconds
    result = math.sqrt(number)
    print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

#task5
def truth(t):
    return all(t)


mytuple = (True, True, True)
notmytuple = (False, False, False)

print(truth(mytuple)) 
print(truth(notmytuple))  




