file = open('numbers.py')
content = file.read()
# print(content)

print(file.seek(11))
print(file.tell())

print(file.read(3))
file.close()
print("Is file closed?", file.closed)

with open('loops.py', 'rt') as loopFile:
    print(loopFile.mode)
    for line in loopFile:
        print(line)