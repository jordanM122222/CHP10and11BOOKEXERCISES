# Exercise 1

# Hashable tuple
t1 = (1, 2, 'a')
print(hash(t1))  # This will work

# Unhashable tuple
t2 = (1, [2, 3], 'a')
print(hash(t2))  # This will raise a TypeError

# Exercise 2

#!/usr/bin/env python3

if __name__ == '__main__':
    list0 = [1, 2, 3]
    list1 = [4, 5]

    t = (list0, list1)
    t[1].append(6)
    print(t)

    d = {t: "Hello"}  # Causes Type error because immutable tuple contains mutable lists.

# Exercise 3

#!/usr/bin/env python3

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range( len( letters ) )
letter_map = dict( zip( letters, numbers ) )

def shift_word(word, shift):
    ciphtertext = ''
    for l in word:
        l_index = (letter_map[l] + shift) % len(letters)
        ciphtertext += letters[l_index]
    return ciphtertext


if __name__ == '__main__':
    print(shift_word('cheer', 7))
    print(shift_word('melon', 16))

# Exercise 4

#!/usr/bin/env python3

def count_value(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter

def key_func(item):
    return item[1]

def most_frequent_letters(word):
    counter = count_value(word)
    # return dict( sorted( counter.items(), key=lambda item: item[1], reverse=True ) )
    return dict( sorted( counter.items(), key=key_func, reverse=True ) )

if __name__ == '__main__':
    print(most_frequent_letters('hello-world'))

# Exercise 5

#!/usr/bin/env python3
import json
from os.path import exists


def get_key(word):
    return ''.join(sorted(word.strip()))


def save_sorted_dict(word_dict, file_path):
    with open(file_path, 'w') as wd_file:
        json.dump(word_dict, wd_file, indent=True)


def load_sorted_dict(file_path):
    word_dict = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            key = get_key( word )
            key_list = word_dict.get( key, [] )
            key_list.append( word.strip() )
            word_dict[key] = key_list
    return word_dict

def load_word_dict(file_path, words_path='files/words.txt'):
    word_dict = {}
    if not exists(file_path):
        word_dict = load_sorted_dict(words_path)
        save_sorted_dict(word_dict, file_path)
    else:
        with open(file_path, 'r') as wd_file:
            word_dict = json.load(wd_file)
    return word_dict


def find_anagrams(word_list, word_dict):
    for word in word_list:
        key = get_key(word)
        if len(word_dict[key]) > 1:
            print(f'{word_dict[key]}')

if __name__ == '__main__':
    word_dict_path = 'files/word_dict.json'
    find_anagrams(['deltas', 'retainers', 'generating', 'termless'], load_word_dict(word_dict_path))

# Exercise 6

#!/usr/bin/env python3

def word_distance(word1, word2):
    return sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)

def word_distance_indexes(word1, word2):
    return [i for i, pair in enumerate(zip(word1, word2)) if pair[0] != pair[1]]


if __name__ == '__main__':
    print(word_distance('hello', 'hxllo'))
    print(word_distance('ample', 'apply'))
    print(word_distance('kitten', 'mutton'))
    print(word_distance_indexes('hello', 'halpo'))

# Exercise 7

#!/usr/bin/env python3

from Exercise06 import word_distance
from Exercise05 import load_word_dict

if __name__ == '__main__':
    word_dict_path = 'files/word_dict.json'
    word_dict = load_word_dict(word_dict_path)
    for k, v in word_dict.items():
        if len(v) > 1:  # These are all the words that have anagrams
            for i in range( len( v ) ): # Start with the first word
                for j in range( i + 1, len( v ) ): # Compare it to each word but not to itself
                    if word_distance( v[i], v[j] ) == 2:
                        print( f'Metathesis: {v[i]} and {v[j]}' )