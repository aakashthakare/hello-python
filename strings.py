print("Hey!")
print('Hello!')
print('This is "great"')
print("This is 'great'")
print("Hello " + 'World')
greeting = "Hey"

name = "James"
print(greeting + ' ' + name)

# nameFromInput = input("Please enter your name : ")
# print(greeting + ' ' + nameFromInput)

multiLineString = "A\nB\nC\n"
print(multiLineString)

multiTabString = "A\tB\tC\t"
print(multiTabString)

print("This sting has \"escaped\" 'quotes'.")

print("""No Escape required with "tripple" 'quotes'!""")

multiLineStringWithoutSlashN = """
This
String
Is
Multi Line
With
Tripple
Quotes!
"""
print(multiLineStringWithoutSlashN)

print("Unescaped : \test\new | Escaped : \\test\\new")