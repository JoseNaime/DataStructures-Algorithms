"""
    Challenge 1 (Reverse String)

    Reverse a string using a stack
"""

import stack

string = "tset a si sihT"
reversedString = ""

s = stack.Stack()
for char in string:
    s.push(char)

while not s.isEmpty():
    reversedString += s.pop()

print(reversedString)
