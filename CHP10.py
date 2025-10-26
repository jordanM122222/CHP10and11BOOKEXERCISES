# Exercise 1

# Creating a list of strings
list_of_strings = ["apple", "bannah", "cherry", "date"]

# Creating a set from the list
my_set = set(list_of_strings)

# Checking if a string is in the set
if "bannah" in my_set:
    print("bannah is in the set")
    else:
    print("bannah is not in the set")

# Exercise 2

#!/usr/bin/evn python3

def value_counts_efficient(word):
    counter = {}
    for l in word:
        counter[l] = counter.get(l, 0) + 1
    return counter


if __name__ == '__main__':
    print(value_counts_efficient("hello"))

# Exercise 3

#!/usr/bin/env python3

from Exercise02 import value_counts_efficient

def has_duplicates_efficient(word):
    return len(set(word)) < len(word)

def has_duplicates_comprehension(word):
    return any(v > 1 for v in dict.values(value_counts_efficient( word )))

def has_duplicates(word):
    counter = value_counts_efficient(word)
    for k,v in counter.items():
        if v > 1:
            return True
    return False

if __name__ == '__main__':
    print(has_duplicates('un-unpredictably'))
    print(has_duplicates('unpredictably'))
    print('-'* 80)
    print(has_duplicates_comprehension('un-unpredictably'))
    print(has_duplicates_comprehension('unpredictably'))
    print('-'* 80)
    print(has_duplicates_efficient('un-unpredictably'))
    print(has_duplicates_efficient('unpredictably'))

# Exercise 4

#!/usr/bin/env python3

from Exercise02 import value_counts_efficient

def find_repeats_v1(counter):
    repeats = []
    for k,v in counter.items():
        if v > 1:
            repeats.append(k)
    return repeats

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.

    counter: dictionary that maps from keys to counts

    returns: list of keys
    """
    return [k for k,v in counter.items() if v > 1]

if __name__ == '__main__':
    print(
        find_repeats_v1(
            value_counts_efficient('hello')))
    print('-'*80)
    print(
        find_repeats(
            value_counts_efficient('hello')))

# Exercise 5

#!/usr/bin/env python3

from Exercise02 import value_counts_efficient

def add_counters_v1(counter1, counter2):
    result = dict(counter1)
    for k, v in counter2.items():
        result[k] = result.get(k, 0) + v
    return result

def add_counters(counter1, counter2):
    return {k: counter1.get(k, 0) + counter2.get(k, 0)
            for k in set(counter1.keys()).union(set(counter2.keys()))}

if __name__ == '__main__':
    print(add_counters_v1(
        value_counts_efficient('brontosaurus'),
        value_counts_efficient('apatosaurus')
    ))
    print('-'*80)
    print(add_counters(
        value_counts_efficient('brontosaurus'),
        value_counts_efficient('apatosaurus')
    ))

# Exercise 6

#!/usr/bin/env python3

def load_word_list(file_path):
    word_list = {}
    with open(file_path, 'r') as word_file:
        for word in word_file:
            word_list[word.strip().lower()] = True
    return word_list

def is_interlocking(word, word_list={}):
    word = word.lower()
    intword1 = word[0::2]
    intword2 = word[1::2]
    return intword1 in word_list and intword2 in word_list

if __name__ == '__main__':
    # print(is_interlocking('schooled', load_word_list('files/words.txt')))
    # print(is_interlocking('school', load_word_list('files/words.txt')))

    word_list = load_word_list('files/words.txt')
    for word in word_list:
        if len(word) >= 8 and is_interlocking(word, word_list):
            print(f'{word}: {word[0::2]}, {word[1::2]}')
