import re

def match_pattern(string):
    pattern = r'a*b*'
    if re.fullmatch(pattern, string):
        return True
    else:
        return False

# Test the function
test_strings = ['ab', 'aab', 'abb', 'aabb', 'aaaaaab', 'b', 'aa','arrrrbbbrrr', 'bb']
for string in test_strings:
    if match_pattern(string):
        print(f"Match found: {string}")
    else:
        print(f"No match found: {string}")
