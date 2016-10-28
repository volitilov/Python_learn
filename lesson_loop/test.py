from program import *
import random

letters = "abcdefghijklmnopqrstuvwxyz"
number = "1234567890"
complexity = 10

user = {}
admin = {}
key = []

print(createKey(random, letters, number, complexity, key))

print(recordKey(key, user, admin))
