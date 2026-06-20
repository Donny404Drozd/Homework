
def is_palindrome(text):

    c = ""
    for h in text:
        if h.isalnum():
            c += h.lower()
    return c == c[::-1]

assert (is_palindrome("A man, a plan, a canal: Panama") == True), "Test1"
assert is_palindrome("0P") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"

print("ОК")
