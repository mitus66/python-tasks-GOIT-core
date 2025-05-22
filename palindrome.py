def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower()

    s = new_s
    return s == s[::-1]

# Використання функції
print(is_palindrome("Козак з казок"))  # Виведе: True
