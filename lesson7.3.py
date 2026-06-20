def second_index(text, some_str):

    f = text.find(some_str)
    if f == -1:
        return None
    s = text.find(some_str, f + 1)
    if s != -1:
        return s
    else:
        return None

assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"

print("ОК")
