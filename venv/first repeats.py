def go(ann):
    if (len(ann) == 0):
        return False

    val = ann[len(ann) - 1];

    for x in range(0, len(ann) - 1):
        if ann[x] == val:
            return True
    return False


print(go([-99, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5]))
print(go([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9]))
print(go([10, 20, 30, 40, 50, -11818, 40, 30, 20, 10]))
print(go([32767]))
print(go([7, 7, 7, 7]))
print(go([9, 10, -88, 100, -555, 1000]))
print(go([10, 10, 10, 11, 456, 10, 10]))
print(go([-111, 1, 2, 3, 9, 11, 20, 30]))
print(go([9, 8, 7, 6, 5, 4, 3, 2, 0, -2, 9, 9]))
print(go([12, 15, 18, 21, 23, 1000]))
print(go([250, 19, 17, 15, 13, 11, 10, 9, 6, 3, 2, 1, 250]))
print(go([]))


