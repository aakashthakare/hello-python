# Immutable!
tuple = (1, 2, 3)
tupleSingleElement = (1,)

weeks = ('S', 'M', 'T', 'W', 'T', 'F', 'S')
print(weeks)

# del weeks
# print(weeks)

weekList = list(weeks)

print(weekList)

for w in weeks:
    print(w)


def min_max(numbers):
    m = min(numbers)
    n = max(numbers)
    return (m, n)


print(min_max([1, 2, 99, -1]))
