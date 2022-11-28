import os
import re
import string

def get_words(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    return text.split()

def count_words(words):
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def sort_words(d):
    l = [(value, key) for key, value in d.items()]
    l.sort()
    return l

def get_all_words(file_name):
    with open(file_name, 'r') as f:
        text = f.read()
    text = text.lower()
    for ch in string.punctuation:
        text = text.replace(ch, ' ')
    return text.split()

def sort_all_words(words):
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    l = [(value, key) for key, value in d.items()]
    l.sort()
    return l
