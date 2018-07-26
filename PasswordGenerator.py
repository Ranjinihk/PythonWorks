#!/bin/python3

import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?.,-'

numb = input("number of passwords : ")
numb = int(numb)
length = input("password length : ")
length = int(length)

for p in range(numb):
    password=''
    for c in range(length):
        password+=random.choice(chars)
    print(password)
