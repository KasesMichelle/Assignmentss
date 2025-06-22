import re

def is_palindrome(s):
    # Normalize input: lowercase and remove non-alphanumeric characters
    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())

    stack = []
    for ch in cleaned:
        stack.append(ch)

    for ch in cleaned:
        if ch != stack.pop():
            return False
    return True

# Example usage:
s = input("Enter a word or phrase: ")
if is_palindrome(s):
    print(f'"{s}" is a palindrome.')
else:
    print(f'"{s}" is not a palindrome.')
