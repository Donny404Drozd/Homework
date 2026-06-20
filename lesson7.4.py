
def common_elements():

    l3 = [i for i in range(100) if i % 3 == 0]
    l5 = [i for i in range(100) if i % 5 == 0]
    s3 = set(l3)
    s5 = set(l5)
    r = s3.intersection(s5)
    return r

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("ОК")