# Simple function for test the word for palindrome without clear string (remove '#@!?>< ' etc.)
def simple_is_palindrome(s):
    return s == s[::-1]


print(simple_is_palindrome(''))                             # True
print(simple_is_palindrome('radar'))                        # True
print(simple_is_palindrome('b'))                            # True
print(simple_is_palindrome('and'))                          # False
print(simple_is_palindrome('ишак ищет у тещи каши'))        # True
print(simple_is_palindrome('а роза упала на лапу?азора'))   # False
print()

# Function with clear string (remove not alpha symbols)
def is_palindrome(s):
    new_str = "".join(c.lower() for c in s if c.isalpha())
    return new_str == new_str[::-1]


print(is_palindrome(''))                            # True
print(is_palindrome('radar'))                       # True
print(is_palindrome('b'))                           # True
print(is_palindrome('and'))                         # False
print(is_palindrome('ишак ищет у тещи каши'))       # True
print(is_palindrome('а роза упала на лапу&азора'))  # True
