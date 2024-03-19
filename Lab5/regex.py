import re
with open('row.txt', 'r', encoding='utf-8') as file:
        content = file.readlines()

#task1
def find_a_followed_by_bs(content):
    pattern = re.compile(r'а+б*')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где содержиться после а ноль или несколько б:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_a_followed_by_bs(content)


#task2
def find_a_followed_by_2_to_3_bs(content):
    pattern = re.compile(r'а{1}б{2,3}')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где содержиться после а два или три б:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_a_followed_by_2_to_3_bs(content)


#task3
def find_lowercase_sequences_with_underscore(content):
    pattern = re.compile(r'\b[a-z]+_[a-z]+\b')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("строки где :")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_lowercase_sequences_with_underscore(content)


#task4
def find_upper_case_letter_followed_by_lower(content):
    pattern = re.compile(r'\b[A-Z]{1}[a-z]+\b') # r'\b[А-Я]{1}+[а-я]+\b'
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("последовательность одной заглавной буквы, за которой следуют строчные буквы:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

find_upper_case_letter_followed_by_lower(content)


#task5
def match_a_followed_by_b(content):
    pattern = re.compile(r'а.*б$')
    lines = [line.strip() for line in content if pattern.search(line)]
    if lines:
        print("последовательность одной заглавной буквы, за которой следуют строчные буквы:")
        for line in lines:
            print(line)
    else:
        print("Таких строк нет.")

match_a_followed_by_b(content)


#task6
def replace_with_colon(content):
    result_string = content.replace(' ', ':').replace(',', ':').replace('.', ':')
    return result_string


text = 'Hello, world. This is a test.'
print(replace_with_colon(text))


#task7
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_case)

snake = "hello_world_example"
camel_case = snake_to_camel(snake)

print(f"Camel case: {camel_case}")


#task8
def split_at_uppercase(input_string):
    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result


#task9
def capital_letters(input_string):
    res = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return res


cnt = "SplitThisStringAtUppercaseLetters"

print(f"Resulting list: {split_at_uppercase(cnt)}\nResult string: {capital_letters(cnt)}")


#task10
def camel_to_snake(camel_case):
    res = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_case)
    return res.lower()

camel = "helloWorldExample"
snake_case = camel_to_snake(camel)

print(f"Camel case: {snake_case}")

