import itertools
import collections

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


"""
Find Duplicates 

Given an array, find the duplicates in that array, and return a new array of those duplicates. 
The elements of the returned array should appear in the order when they first appeared as duplicates.

Note: numbers and their corresponding string representations should not be treated as duplicates (i.e., "1" != 1).
Examples

[1, 2, 4, 4, 3, 3, 1, 5, 3, "5"]  ==>  [4, 3, 1]
[0, 1, 2, 3, 4, 5]                ==>  []


"""
print('*** Find Duplicates ***')


def duplicates(arr):
    new_arr = []
    for i in range(len(arr)):
        if i != arr.index(arr[i]) and arr[i] not in new_arr:
            new_arr.append(arr[i])
    return new_arr


print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, "5"]))
print(duplicates([0, 1, 2, 3, 4, 5]))
print(duplicates(['1', 2, 4, '4', 3, '3', 1, 5, 3, 3, 3, 3]))
print(duplicates([]))


"""
Length and two values.

Given an integer n and two other values, build an array of size n filled with these two values alternating.
Examples

5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []

"""
print('*** Length and two values. ***')


def alternate(n, first_value, second_value):
    lst = [first_value, second_value]
    new_lst = []
    count = 0
    for i in itertools.cycle(lst):
        if count > n - 1:
            break
        new_lst.append(i)
        count += 1
    return new_lst


print(alternate(5, True, False))
print(alternate(10, "blue", "red"))
print(alternate(0, "one", "two" ))


"""
Compare 2 digit numbers

You are given 2 two-digit numbers. You should check if they are similar by comparing 
their numbers, and return the result in %.

Example:

    compare(13,14)=50%;
    compare(23,22)=50%;
    compare(15,51)=100%;
    compare(12,34)=0%.


"""
print('*** Compare 2 digit numbers ***')


def compare(a, b):
    a = sorted(str(a))
    b = sorted(str(b))
    if a == b:
        return '100%'
    elif a[0] in b or a[1] in b:
        return '50%'
    else:
        return '0%'


print(compare(13, 14))
print(compare(23, 22))
print(compare(15, 51))
print(compare(12, 34))
print(compare(66, 16))


"""
Simple remove duplicates

Remove the duplicates from a list of integers, keeping the last ( rightmost ) occurrence of each element.
Example:

For input: [3, 4, 4, 3, 6, 3]

    remove the 3 at index 0
    remove the 4 at index 1
    remove the 3 at index 3

Expected output: [4, 6, 3]

"""
print('*** Simple remove duplicates ***')


def solve(arr):
    for i in arr[:]:
        if arr.count(i) > 1:
            arr.pop(arr.index(i))
    return arr


print(solve([3, 4, 4, 3, 6, 3]))
print(solve([1, 2, 1, 2, 1, 2, 3]))


"""
String ends with?

Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false

"""
print('*** String ends with? ***')


def solution(text, ending):
    return text.endswith(ending)


print(solution('abc', 'bc'))
print(solution('abc', 'd'))


"""
Anagram Detection

An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
Examples

    "foefet" is an anagram of "toffee"

    "Buckethead" is an anagram of "DeathCubeK"
"""
print('*** Anagram Detection ***')


def is_anagram(test, original):
    str1 = sorted(test.lower())
    str2 = sorted(original.lower())
    return str1 == str2


print(is_anagram("foefet", "toffee"))
print(is_anagram("Buckethead", "DeathCubeK"))
print(is_anagram("Twoo", "WooT"))
print(is_anagram("dumble", "bumble"))
print(is_anagram("ound", "round"))
print(is_anagram('GRbqbKlDlBxZUqUuJ', 'xQlYDJVRZCUbquGUq'))


"""
Friend or Foe?

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a 
friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
"""

print('*** Friend or Foe? ***')


def friend(x):
    return [i for i in x if len(i) == 4]


print(friend(["Ryan", "Kieran", "Mark"]))
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]))


"""
Find array

You are given two arrays arr1 and arr2, where arr2 always contains integers.

Write a function such that:

For arr1 = ['a', 'a', 'a', 'a', 'a'], arr2 = [2, 4] the function returns ['a', 'a']

For arr1 = [0, 1, 5, 2, 1, 8, 9, 1, 5], arr2 = [1, 4, 7] the function returns [1, 1, 1]

For arr1 = [0, 3, 4], arr2 = [2, 6] the function returns [4]

For arr1=["a","b","c","d"] , arr2=[2,2,2], the function returns ["c","c","c"]

For arr1=["a","b","c","d"], arr2=[3,0,2] the function returns ["d","a","c"]
"""
print('*** Find array ***')


def find_array(arr1, arr2):
    new_arr = []
    for i in arr2:
        try:
            new_arr.append(arr1[i])
        except IndexError:
            continue
    return new_arr


print(find_array(['a', 'a', 'a', 'a', 'a'], [2, 4]))
print(find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]))
print(find_array([1], []))
print(find_array([0, 3, 4], [2, 6]))


"""
Exes and Ohs

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean 
and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""
print('*** Exes and Ohs ***')


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


print(xo("ooxx"))
print(xo("xooxx"))
print(xo("ooxXm"))
print(xo("zpzpzpp"))
print(xo("zzoo"))
print(xo("oxOx"))
print(xo(""))

