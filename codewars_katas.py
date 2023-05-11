import collections
import itertools
import re
import string


"""
Descending Order

Your task is to make a function that can take any non-negative integer as an argument and return it with its 
digits in descending order. Essentially, rearrange the digits to create the highest possible number.
Examples:

Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

"""
print('*** Descending Order ***')


def descending_order(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(descending_order(42145))
print(descending_order(145263))
print(descending_order(123456789))


"""
Isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false


"""
print('*** Isograms ***')


def is_isogram(string):
    if any([i.isdigit() for i in string]) or [item for item, count in collections.Counter(string.lower()).items() if count > 1]:
        return False
    return True


print(is_isogram("Dermatoglyphics"))
print(is_isogram("moose"))
print(is_isogram("aba"))


"""
Categorize New Member

The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
They would like your help with an application form that will tell prospective 
members which category they will be placed.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7. 
In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.
Input

Input will consist of a list of pairs. Each pair contains information for a single potential member. 
Information consists of an integer for the person's age and an integer for the person's handicap.
Output

Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether 
the respective member is to be placed in the senior or open category.
Example

input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]


"""
print('*** Categorize New Member ***')


def open_or_senior(data):
    output = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            output.append('Senior')
        else:
            output.append('Open')
    return output


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))


"""
Two to One

Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string, the longest possible, containing distinct letters - 
each taken only once - coming from s1 or s2.
Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"


"""
print('*** Two to One ***')


def longest(a1, a2):
    a3 = a1 + a2
    return ''.join(sorted(list(set(a3))))


print(longest('xyaabbbccccdefww', 'xxxxyyyyabklmopq'))


"""
Jaden Casing Strings

Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, 
he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, 
check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual 
quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.

Example:

Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

"""
print('*** Jaden Casing Strings ***')


def to_jaden_case(string):
    return ' '.join([i.capitalize() for i in string.split()])


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


"""
Detect Pangram

A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence 
"The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. 
Return True if it is, False if not. Ignore numbers and punctuation.

"""
print('*** Detect Pangram ***')


def is_pangram(s):
    al = list(string.ascii_lowercase)
    return all([i in s.lower() for i in al])

print(is_pangram("The quick brown fox jumps over the lazy dog"))


"""
Is this a triangle?

Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""
print('*** Is this a triangle? ***')


def is_triangle(a, b, c):
    if (a+b > c) and (a+c > b) and (b+c > a):
        if a > 0 and b > 0 and c > 0:
            return True
    return False


print(is_triangle(2, 2, 1))


"""
Find the missing letter

Write a method that takes an array of consecutive (increasing) letters as input 
and that returns the missing letter in the array.

You will always get an valid array. And it will be always exactly one letter be missing. 
The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e'
['O','Q','R','S'] -> 'P'

(Use the English alphabet with 26 letters!)

Have fun coding it and please don't forget to vote and rank this kata! :-)

"""
print('*** Find the missing letter ***')


def find_missing_letter(chars):
    al = string.ascii_lowercase if chars[0] >= 'a' else string.ascii_uppercase
    for i in al[al.index(chars[0]):]:
        if i not in chars:
            return i[0]


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))


"""
Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"

"""
print('*** Convert string to camel case ***')


def to_camel_case(text):
    a = re.split('-|_', text)
    new_string = a[0]
    for i in range(1, len(a)):
        new_string += a[i][0].upper() + a[i][1:]
    return new_string


print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))


"""
Counting Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters 
and numeric digits that occur more than once in the input string. The input string can be assumed 
to contain only alphabets (both uppercase and lowercase) and numeric digits.
Example

"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""
print('*** Counting Duplicates ***')


def duplicate_count(text):
    a = []
    text = text.lower()
    for i in text:
        if text.count(i) > 1:
            a.append(i)
    return len(set(a))


print(duplicate_count("aA11"))
print(duplicate_count("ABBA"))
print(duplicate_count("Indivisibilities"))
print(duplicate_count("indivisibility"))
print(duplicate_count("abcde"))


"""
Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.
"""
print('*** Find the unique number ***')


def find_uniq(arr):
    l = [i for i in set(arr) if arr.count(i) == 1]
    return l[0]


print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))
print(find_uniq([ 0, 0, 0.55, 0, 0 ]))


"""
The Hashtag Generator

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

"""
print('*** The Hashtag Generator ***')


def generate_hashtag(s):
    if s == '':
        return False
    else:
        a = s.strip().split(' ')
        new_string = '#'
        for i in range(len(a)):
            if a[i] == '':
                continue
            new_string += a[i][0].upper() + a[i][1:].lower()
        if len(new_string) > 140:
            return False
    return new_string


print(generate_hashtag(" Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello     World   "))
print(generate_hashtag(""))


"""
Simple Pig Latin

Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !

"""
print('*** Simple Pig Latin ***')


def pig_it(text):
    lst = []
    for i in text.split():
        if i.isalpha():
            a = i[1:] + i[0] + 'ay'
            lst.append(a)
        else:
            lst.append(i)
    return ' '.join(lst)


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))


"""
Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
print('*** Convert boolean values to strings "Yes" or "No". ***')


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    return "No"


print(bool_to_word(True))


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
Extract the domain name from a URL
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. 
For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"


"""
print('*** Extract the domain name from a URL ***')


def domain_name(url):
    n = re.search(r'(^https?://)?(w{3}\.)?(\w+-?\w+)', url)
    return n.group(3)


print(domain_name('http://github.com/carbonfive/raygun'))
print(domain_name('http://www.zombie-bites.com'))
print(domain_name('https://www.cnet.com'))

"""
Sum of Digits / Digital Root

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue 
reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
Examples

    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


"""
print('*** Sum of Digits / Digital Root ***')


def digital_root(n):
    while n > 9:
        n = sum(map(int, list(str(n))))
    return n


print(digital_root(16))
print(digital_root(493193))


"""
Are You Playing Banjo?

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo" 
name + " does not play banjo"

Names given are always valid strings.

"""
print('*** Are You Playing Banjo? ***')


def are_you_playing_banjo(name):
    if name.startswith("R") or name.startswith("r"):
        return name + " plays banjo"
    return name + " does not play banjo"


print(are_you_playing_banjo('Ray'))
print(are_you_playing_banjo('Ann'))


"""
Adding Arrays

Create a function that takes an array of letters, and combines them into words in a sentence.

The array will be formatted as so:

[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
]

The function should combine all the 0th indexed letters to create the word 'just', 
all the 1st indexed letters to create the word 'live', etc.

Shorter words will have an empty string in the place once the word has already been mapped out 
(see the last element in the last element in the array).

Examples:

[
  ['J','L','L','M'],
  ['u','i','i','a'],
  ['s','v','f','n'],
  ['t','e','e','']
] // => "Just Live Life Man"
"""
print('*** Adding Arrays ***')


def arr_adder(arr):
    num_of_words = len(arr[0])
    sent = []
    for i in range(num_of_words):
        sent.append(''.join([k[i] for k in arr if k[i] != '']))
    return ' '.join(sent)


print(arr_adder([
  [ 'T', 'M', 'i', 't', 'p', 'o', 't', 'c' ],
  [ 'h', 'i', 's', 'h', 'o', 'f', 'h', 'e' ],
  [ 'e', 't', '', 'e', 'w', '', 'e', 'l' ],
  [ '', 'o', '', '', 'e', '', '', 'l' ],
  [ '', 'c', '', '', 'r', '', '', '' ],
  [ '', 'h', '', '', 'h', '', '', '' ],
  [ '', 'o', '', '', 'o', '', '', '' ],
  [ '', 'n', '', '', 'u', '', '', '' ],
  [ '', 'd', '', '', 's', '', '', '' ],
  [ '', 'r', '', '', 'e', '', '', '' ],
  [ '', 'i', '', '', '', '', '', '' ],
  [ '', 'a', '', '', '', '', '', '' ]
]
))

"""
99 Problems

Write a function last that accepts a list and returns the last element in the list.

If the list is empty:

In languages that have a built-in option or result type (like OCaml or Haskell), return an empty option

In languages that do not have an empty option, just return None

"""
print('*** 99 Problems ***')


def last(lst):
    return lst[-1] if len(lst) > 0 else None


print(last([]))
print(last([1, 2]))


"""
Remove consecutive duplicate words

Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. For example:

"alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"

--> "alpha beta gamma delta alpha beta gamma delta"
"""
print('*** Remove consecutive duplicate words ***')


def remove_consecutive_duplicates(s : str) -> str:
    lst = s.split()
    new_lst = []
    prev = ''
    for i in lst:
        if i == prev:
            continue
        new_lst.append(i)
        prev = i
    return ' '.join(new_lst)


print(remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))

"""
Chain me

Write a generic function chainer

Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).

The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.

def add10(x): return x + 10
def mul30(x): return x * 30

chain(50, [add10, mul30])
# returns 1800
"""
print('*** Chain me ***')


def add10(x): return x + 10
def mul30(x): return x * 30


def chain(init_val, functions):
    res = init_val
    for i in functions:
        res = i(res)
    return res


print(chain(50, [add10, mul30]))
