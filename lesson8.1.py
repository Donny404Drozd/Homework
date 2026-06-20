
def add_one(some_list):

    n = ""
    for d in some_list:
        n += str(d)
    w = int(n) + 1
    r = []
    for c in str(w):
        r.append(int(c))
    return r

assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], "Test1"
assert add_one([9, 9, 9]) == [1, 0, 0, 0], "Test2"
assert add_one([0]) == [1], "Test3"
assert add_one([9]) == [1, 0], "Test4"

print("ОК")
