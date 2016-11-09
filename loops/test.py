from program import *

letters = "abcdefghijklmnopqrstuvwxyz"
complexity = 10

user = {}
admin = {}
testStr = []

key = createKey(letters, complexity, testStr)

print(recordKey(testStr, user, admin, key))
