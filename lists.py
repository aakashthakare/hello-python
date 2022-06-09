listNumber = [1, 2, 3, 4]
print(listNumber[0])
listNumber[1] = 33
print(listNumber)

print(listNumber[-1]) #last
print(listNumber[-2]) #second last

listNumber.insert(2, 99)

print(listNumber)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:5])
print(numbers[:5]) # First five
print(numbers[5:]) # After index 5

print(numbers[-2:]) # After second last index


print('Hello' [1:3]) # slice string


unsorted1 = [5, 4, 3, 2, 1]
unsorted2 = [6, 7, 3, 2, 1]
concatenated = unsorted1 + unsorted2;
print(concatenated)
concatenated.append(90)
print(len(concatenated))
sorted1 = sorted(unsorted1)
print("Unsorded", unsorted1, "Sorted", sorted1)

