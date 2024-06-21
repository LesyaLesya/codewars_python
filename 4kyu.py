import itertools
import re
from collections import Counter

"""
So Many Permutations!
In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!

Examples:

With input 'a':
Your function should return: ['a']

With input 'ab':
Your function should return ['ab', 'ba']

With input 'abc':
Your function should return ['abc','acb','bac','bca','cab','cba']

With input 'aabb':
Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

Note: The order of the permutations doesn't matter.
"""
print('*** So Many Permutations! ***')


def permutations(s):
    return list(set(list(map(''.join, itertools.permutations(s)))))


print(permutations('abc'))


"""
Most frequently used words in a text

Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array 
of the top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
    Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
    Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, 
    or an empty array if a text contains no words.

Examples:

top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]
"""

print('*** Most frequently used words in a text ***')


def top_3_words(text):
    string = re.findall(r"'*[a-z][a-z']*", text.lower())
    return [i[0] for i in Counter(string).most_common(3)]


print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""))
print(top_3_words("  , e   .. "))
print(top_3_words("  //wont won't won't "))
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))


"""
Strip Comments

Complete the solution so that it strips all text that follows any of a set of comment 
markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""

print('*** Strip Comments ***')


def strip_comments(strng, markers):
    l = strng.split('\n')
    for i in markers:
        l = [j.split(i)[0].rstrip() for j in l]
    return '\n'.join(l)


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))
print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))


"""
Next smaller number with the same digits

Write a function that takes a positive integer and returns the next smaller positive integer 
containing the same digits.

For example:

next_smaller(21) == 12
next_smaller(531) == 513
next_smaller(2071) == 2017

Return -1 (for Haskell: return Nothing, for Rust: return None), when there is no smaller number that contains 
the same digits. Also return -1 when the next smaller number with the same digits would require 
the leading digit to be zero.

next_smaller(9) == -1
next_smaller(135) == -1
next_smaller(1027) == -1  # 0721 is out since we don't write numbers with leading zeros

    some tests will include very large numbers.
    test data only employs positive integers.
"""

print('*** Next smaller number with the same digits ***')


def next_smaller(n):
    perms = tuple(set(itertools.permutations(str(n))))
    l = (int(''.join(i)) for i in perms if i[0] != '0')
    res = sorted(l, reverse=True)
    m = res[res.index(n):]
    return -1 if len(m) == 1 else m[1]


print(next_smaller(907))
print(next_smaller(135))
print(next_smaller(414))
print(next_smaller(1234567908))
