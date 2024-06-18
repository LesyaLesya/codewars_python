import itertools
import collections
import string
import re

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


"""
Find the capitals

Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of all capital letters in the string.
Example

Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
"""

print('*** Find the capitals ***')


def capitals(word):
    return [i for i in range(len(word)) if word[i].isupper()]


print(capitals('CodEWaRs'))
print(capitals('xscrCVojMBHFLrVuotJu'))
print(capitals('DOgTMfrhxudKXraetOVzyaVR'))


"""
Find the divisors! 

Create a function named divisors/Divisors that takes an integer n > 1 and returns an 
array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. 
If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) 
(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
"""

print('*** Find the divisors! ***')


def divisors(integer):
    res = [i for i in range(2, integer) if integer % i == 0]
    return f'{integer} is prime' if len(res) == 0 else res


print(divisors(12))
print(divisors(25))
print(divisors(13))
print(divisors(29))


"""
Two numbers are positive

Task:

Your job is to write a function, which takes three integers a, b, and c as arguments, and returns True 
if exactly two of of the three integers are positive numbers (greater than zero), and False - otherwise.
Examples:

two_are_positive(2, 4, -3) == True
two_are_positive(-4, 6, 8) == True
two_are_positive(4, -6, 9) == True
two_are_positive(-4, 6, 0) == False
two_are_positive(4, 6, 10) == False
two_are_positive(-14, -3, -4) == False
"""

print('*** Two numbers are positive ***')


def two_are_positive(a, b, c):
    return True if (a > 0 and b > 0 and c <= 0) or (b > 0 and c > 0 and a <= 0) or (a > 0 and c > 0 and b <=0 ) else False


print(two_are_positive(2, 4, -3))
print(two_are_positive(-4, 6, 8))
print(two_are_positive(-4, 6, 0))
print(two_are_positive(-14, -3, -4))
print(two_are_positive(4, 6, 10))



"""
Help Suzuki rake his garden!

Help Suzuki rake his garden!

The monastery has a magnificent Zen garden made of white gravel and rocks and it is raked diligently everyday 
by the monks. Suzuki having a keen eye is always on the lookout for anything creeping into the garden that must 
be removed during the daily raking such as insects or moss.

You will be given a string representing the garden such as:

garden = 'gravel gravel gravel gravel gravel gravel gravel gravel gravel rock slug ant gravel gravel snail 
rock gravel gravel gravel gravel gravel gravel gravel slug gravel ant gravel gravel gravel gravel rock slug 
gravel gravel gravel gravel gravel snail gravel gravel rock gravel snail slug gravel gravel spider gravel gravel 
gravel gravel gravel gravel gravel gravel moss gravel gravel gravel snail gravel gravel gravel ant gravel 
gravel moss gravel gravel gravel gravel snail gravel gravel gravel gravel slug gravel rock gravel gravel 
rock gravel gravel gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel spider 
gravel rock gravel gravel'

Rake out any items that are not a rock or gravel and replace them with gravel such that:

garden = 'slug spider rock gravel gravel gravel gravel gravel gravel gravel'

Returns a string with all items except a rock or gravel replaced with gravel:

garden = 'gravel gravel rock gravel gravel gravel gravel gravel gravel gravel'
"""

print('*** Help Suzuki rake his garden! ***')


def rake_garden(garden):
    l = garden.split(' ')
    new_l = [i if i == 'rock' or i == 'gravel' else 'gravel' for i in l]
    return ' '.join(new_l)


print(rake_garden('slug spider rock gravel gravel gravel gravel gravel gravel gravel'))
print(rake_garden('gravel gravel gravel gravel gravel gravel gravel gravel gravel rock '
                  'slug ant gravel gravel snail rock gravel gravel gravel gravel gravel '
                  'gravel gravel slug gravel ant gravel gravel gravel gravel rock slug '
                  'gravel gravel gravel gravel gravel snail gravel gravel rock gravel '
                  'snail slug gravel gravel spider gravel gravel gravel gravel gravel '
                  'gravel gravel gravel moss gravel gravel gravel snail gravel gravel '
                  'gravel ant gravel gravel moss gravel gravel gravel gravel snail gravel '
                  'gravel gravel gravel slug gravel rock gravel gravel rock gravel gravel '
                  'gravel gravel snail gravel gravel rock gravel gravel gravel gravel gravel '
                  'spider gravel rock gravel gravel'))


"""
Keep the Order

Your job here is to write a function (keepOrder in JS/CoffeeScript, keep_order in 
Ruby/Crystal/Python, keeporder in Julia), which takes a sorted array ary and a value val, 
and returns the lowest index where you could insert val to maintain the sorted-ness of the array. 
The input array will always be sorted in ascending order. It may contain duplicates.

Do not modify the input.
Some examples:

keep_order([1, 2, 3, 4, 7], 5) #=> 4
                      ^(index 4)
keep_order([1, 2, 3, 4, 7], 0) #=> 0
          ^(index 0)
keep_order([1, 1, 2, 2, 2], 2) #=> 2
                ^(index 2)

"""

print('*** Keep the Order ***')


def keep_order(ary, val):
    for i in ary:
        if val <= i:
            return ary.index(i)
    return len(ary)


print(keep_order([1, 2, 3, 4, 7], 5)) # 4
print(keep_order([1, 2, 3, 4, 7], 0)) # 0
print(keep_order([1, 1, 2, 2, 2], 2)) # 2
print(keep_order([1, 2, 3, 4], 5)) # 4
print(keep_order([1, 2, 3, 4], -1)) # 0


"""
Remove anchor from URL

Complete the function/method so that it returns the url with anything after the anchor (#) removed.
Examples

"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
"""

print('*** Remove anchor from URL ***')


def remove_url_anchor(url):
    return url.split('#')[0]


print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))
print(remove_url_anchor("www.codewars.com/katas/"))


"""
The unknown but known variables: Addition

This should be fairly simple. It is more of a puzzle than a programming problem.

There will be a string input in this format: 'a+b' 2 lower case letters (a-z) seperated by a '+'

Return the sum of the two variables.

There is one correct answer for a pair of variables.

I know the answers, it is your task to find out.

Once you crack the code for one or two of the pairs, you will have the answer for the rest.

It is like when you were in school doing math and you saw "11 = c+h" and you needed to find out what c and h were.

However you don't have an 11. You have an unknown there as well. Example:

X = a+b.

You don't know what X is, and you don't know what b is or a, but it is a puzzle and you will find out.

As part of this puzzle, there is three hints or clues on solving this. 
I won't tell you what the other two are, but one of them is: Don't overthink it. It is a simple solution 

Given the input as a string - Return the sum of the two variables as int.
"""

print('*** The unknown but known variables: Addition ***')


def the_var(the_variables):
    alphabet = string.ascii_lowercase
    l1, l2 = the_variables.split('+')
    return (alphabet.find(l1)+1) + (alphabet.find(l2)+1)


print(the_var('d+g'))


"""
These are not my grades! (Revamped !)

At the end of the last semester, Prof. Joey Greenhorn implemented an online 
report card for his students in order to save paper. 
Everything seemed to be working fine back then, but since the start of the new semester he 
has received several emails from students complaining about erroneous grades showing up in 
their online report cards. Can you help him correct his implementation of the "Student" class?

The "Student" class should behave like this :

someStudent = Student()
someOtherStudent = Student()
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
someStudent.grades == [98] # Evaluates to True
someOtherStudent.grades == [77] # Evaluates to True

But right now, this is happening :

someStudent = Student()
someOtherStudent = Student()
someStudent.add_grade(98)
someOtherStudent.add_grade(77)
someStudent.grades == [98, 77] # Evaluates to True
someOtherStudent.grades == [98, 77] # Evaluates to True
"""

print('*** These are not my grades! (Revamped !) ***')


class Student:

    def __init__(self, first_name, last_name, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)


"""
Thinkful - Object Drills: Quarks

Background

You're modelling the interaction between a large number of quarks and have decided to create a 
Quark class so you can generate your own quark objects.

Quarks are fundamental particles and the only fundamental particle to experience all four fundamental forces.
Your task

Your Quark class should allow you to create quarks of any valid color ("red", "blue", and "green") and 
any valid flavor ('up', 'down', 'strange', 'charm', 'top', and 'bottom').

Every quark has the same baryon_number (BaryonNumber in C#): 1/3.

Every quark should have an .interact() (.Interact() in C#) method that allows any quark to interact 
with another quark via the strong force. When two quarks interact they exchange colors.
Example

>>> q1 = Quark("red", "up")
>>> q1.color
"red"
>>> q1.flavor
"up"
>>> q2 = Quark("blue", "strange")
>>> q2.color
"blue"
>>> q2.baryon_number
0.3333333333333333
>>> q1.interact(q2)
>>> q1.color
"blue"
>>> q2.color
"red"
"""

print('*** Thinkful - Object Drills: Quarks ***')


class Quark:
    def __init__(self, color, flavor):
        if self.verify_color(color):
            self.color = color
        if self.verify_flavor(flavor):
            self.flavor = flavor
        self.baryon_number = 1/3

    @classmethod
    def verify_color(cls, color):
        if color not in ['red', 'blue', 'green']:
            raise TypeError('wrong color')
        else:
            return color

    @classmethod
    def verify_flavor(cls, flavor):
        if flavor not in ['up', 'down', 'strange', 'charm', 'top', 'bottom']:
            raise TypeError('wrong flavor')
        else:
            return flavor

    def interact(self, other):
        self.color, other.color = other.color, self.color


q1 = Quark("red", "up")
print(q1.color)
# "red"
print(q1.flavor)
# "up"
q2 = Quark("blue", "strange")
print(q2.color)
#"blue"
print(q2.baryon_number)
# 0.3333333333333333
q1.interact(q2)
print(q1.color)
#"blue"
print(q2.color)
# "red"


"""
Array element parity

In this Kata, you will be given an array of integers whose elements have both a negative and a 
positive value, except for one integer that is either only negative or only positive. 
Your task will be to find that integer.

Examples:

[1, -1, 2, -2, 3] => 3

3 has no matching negative appearance

[-3, 1, 2, 3, -1, -4, -2] => -4

-4 has no matching positive appearance

[1, -1, 2, -2, 3, 3] => 3

(the only-positive or only-negative integer may appear more than once)
"""

print('*** Array element parity ***')


def solve(arr):
    for i in arr:
        if -i not in arr:
            return i


print(solve([1, -1, 2, -2, 3, 3]))


"""
Dropcaps

DropCaps means that the first letter of the starting word of the paragraph should 
be in caps and the remaining lowercase, just like you see in the newspaper.

But for a change, let"s do that for each and every word of the given String. 
Your task is to capitalize every word that has length greater than 2, leaving smaller words as they are.

*should work also on Leading and Trailing Spaces and caps.

"apple"            => "Apple"
"apple of banana"  => "Apple of Banana"
"one   space"      => "One   Space"
"   space WALK   " => "   Space Walk   " 

Note: you will be provided atleast one word and should take string as input and return string as output.
"""

print('*** Dropcaps ***')


def drop_cap(words):
    re_whitespace = re.compile(r'(\s+)')
    l = re_whitespace.split(words)
    for i in range(len(l)):
        if len(l[i]) > 2:
            l[i] = l[i].capitalize()
    return ''.join(l)


print(drop_cap('apple of banana'))
print(drop_cap('   space WALK   '))


"""
What time is it?

Given a time in AM/PM format as a string, convert it to 24-hour military time time as a string.

Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. 
Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock

Try not to use built-in Date/Time libraries.
Examples

"07:05:45PM"  -->  "19:05:45"
"12:00:01AM"  -->  "00:00:01"
"11:46:47PM"  -->  "23:46:47"
"""

print('*** What time is it? ***')


def get_military_time(time):
    pm = {'12': '12', '01': '13', '02': '14', '03': '15', '04': '16', '05': '17', '06': '18', '07': '19',
          '08': '20', '09': '21', '10': '22', '11': '23'}
    am = {'12': '00', '01': '01', '02': '02', '03': '03', '04': '04', '05': '05', '06': '06', '07': '07',
          '08': '08', '09': '09', '10': '10', '11': '11'}
    am_pm = time[-2:]
    hours = time[:2]
    if am_pm == 'AM':
        correct_hour = am.get(hours)
    else:
        correct_hour = pm.get(hours)
    return correct_hour + time[2:-2]


print(get_military_time('12:00:01AM'))
print(get_military_time('11:46:47PM'))


"""
Is n divisible by (...)?

Create a function that checks if the first argument n is divisible by all other 
arguments (return true if no other arguments)

Example:

(6,1,3)--> true because 6 is divisible by 1 and 3
(12,2)--> true because 12 is divisible by 2
(100,5,4,10,25,20)--> true
(12,7)--> false because 12 is not divisible by 7
"""

print('*** Is n divisible by (...)? ***')


def is_divisible(*args):
    first = args[0]
    return all([first % args[i] == 0 for i in range(1, len(args))])


print(is_divisible(3,3,4))
print(is_divisible(12,3,4))
print(is_divisible(8,3,4,2,5))


"""
Filter the number

Filter the number

Oh, no! The number has been mixed up with the text. Your goal is to retrieve 
the number from the text, can you return the number back to its original state?
Task

Your task is to return a number from a string.
Details

You will be given a string of numbers and letters mixed up, you have to return all 
the numbers in that string in the order they occur.
"""

print('*** Filter the number ***')


def filter_string(string):
    return int(''.join([i for i in string if i.isdigit()]))


print(filter_string('a1b2c3'))
print(filter_string('aa1bb2cc3dd'))


"""
Tail Swap

You'll be given a list of two strings, and each will contain exactly one colon (":") 
in the middle (but not at beginning or end). The length of the strings, before and after the colon, are random.

Your job is to return a list of two strings (in the same order as the original list), 
but with the characters after each colon swapped.
Examples

["abc:123", "cde:456"]  -->  ["abc:456", "cde:123"]
["a:12345", "777:xyz"]  -->  ["a:xyz", "777:12345"]
"""

print('*** Tail Swap ***')


def tail_swap(strings):
    l = [i.split(':') for i in strings]
    l[0][1], l[1][1] = l[1][1], l[0][1]
    return [':'.join(q) for q in l]


print(tail_swap(['abc:123', 'cde:456']))


"""
Disemvowel Trolls

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels 
from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""

print('*** Disemvowel Trolls ***')


def disemvowel(string_):
    UPPERS = 'AEIOU'
    LOWERS = 'aeiou'
    res = ''
    for i in string_:
        if i in UPPERS or i in LOWERS:
            continue
        else:
            res += i
    return res


print(disemvowel("No offense but,\nYour writing is among the worst I've ever read"))


"""
Vowel Count

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

print('*** Vowel Count ***')


def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count


print(get_count('aeiou'))


"""
The animals went in two by two

A great flood has hit the land, and just as in Biblical times we need to get the animals to the ark in pairs. 
We are only interested in getting one pair of each animal, and not interested in any animals where there 
are less than 2....they need to mate to repopulate the planet after all!

You will be given a list of animals, which you need to check to see which animals there are at least two of, 
and then return a dictionary containing the name of the animal along with the fact that there 
are 2 of them to bring onto the ark.

>>> two_by_two(['goat', 'goat', 'rabbit', 'rabbit', 'rabbit', 'duck', 'horse', 'horse', 'swan'])
{'goat': 2, 'horse': 2, 'rabbit': 2}

# If the list of animals is empty, return False as there are no animals to bring onto the ark and we are all doomed!!!
>>> two_by_two([])
False

# If there are no pairs of animals, return an empty dictionary
>>> two_by_two(['goat'])
{}
"""

print('*** The animals went in two by two ***')


def two_by_two(animals):
    if len(animals) == 0: return False
    return {i: 2 for i in animals if animals.count(i) >= 2}


print(two_by_two([]))
print(two_by_two(['goat']))
print(two_by_two(["dog", "cat", "dog", "cat", "beaver", "cat"]))
print(two_by_two(["goat", "goat", "rabbit", "rabbit", "rabbit", "duck", "horse", "horse", "swan"]))


"""
Double value every next call

This kata is about static method that should return different values.
On the first call it must be 1, on the second and others - it must be a double from previous value. 
"""

print('*** Double value every next call ***')


class Class:
    RES = 1

    @staticmethod
    def get_number():
        r = Class.RES
        Class.RES *= 2
        return r


print(Class().get_number()) #1
print(Class().get_number()) #2
print(Class().get_number()) #4
print(Class().get_number()) #8


"""
User class for Banking System

A company is opening a bank, but the coder who is designing the user class made some errors. 
They need you to help them.

You must include the following:
Note: These are NOT steps to code the class

    A withdraw method
        Subtracts money from balance
        One parameter, money to withdraw
        Raise a ValueError if there isn't enough money to withdraw
        Return a string with name and balance(see examples)

    A check method
        Adds money to balance
        Two parameters, other user and money
        Other user will always be valid
        Raise a ValueError if other user doesn't have enough money
        Raise a ValueError if checking_account isn't true for other user
        Return a string with name and balance plus other name and other balance(see examples)

    An add_cash method
        Adds money to balance
        One parameter, money to add
        Return a string with name and balance(see examples)

Additional Notes:

    Checking_account should be stored as a boolean

    No input numbers will be negative

    Output must end with a period

    Float numbers will not be used so, balance should be integer

    No currency will be used

Examples:

Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, False)

Jeff.withdraw(2) # Returns 'Jeff has 68.'

Joe.check(Jeff, 50) # Returns 'Joe has 120 and Jeff has 18.'

Jeff.check(Joe, 80) # Raises a ValueError

Joe.checking_account = True # Enables checking for Joe

Jeff.check(Joe, 80) # Returns 'Jeff has 98 and Joe has 40'

Joe.check(Jeff, 100) # Raises a ValueError

Jeff.add_cash(20.00) # Returns 'Jeff has 118.'
"""

print('*** User class for Banking System ***')


class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, value):
        self.balance = self.balance - value
        if self.balance < 0:
            raise ValueError("isn't enough money to withdraw")
        return f'{self.name} has {self.balance}.'

    def add_cash(self, value):
        self.balance = self.balance + value
        return f'{self.name} has {self.balance}.'

    def check(self, other, value):
        if not other.checking_account:
            raise ValueError("is not valid")
        if other.balance < value:
            raise ValueError("isn't enough money to withdraw")
        other.balance = other.balance - value
        self.balance = self.balance + value
        return f'{self.name} has {self.balance} and {other.name} has {other.balance}.'


Jeff = User('Jeff', 70, True)
Joe = User('Joe', 70, True)
print(Jeff.withdraw(2))
print(Joe.check(Jeff, 50))
print(Jeff.check(Joe, 80))
print(Jeff.add_cash(20))


"""
String Reordering

The input will be an array of dictionaries.

Return the values as a string-seperated sentence in the order of their keys' integer equivalent (increasing order).

The keys are not reoccurring and their range is -999 < key < 999. The dictionaries' 
keys & values will always be strings and will always not be empty.
Example

Input:
List = [
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]

Output:
'Vatsan took his dog for a spin'
"""

print('*** String Reordering ***')


def sentence(lst):
    d = {int(key): value for i in lst for key, value in i.items()}
    return ' '.join(i[1] for i in sorted(d.items()))


print(sentence([{'1': 'dog'}, {'2': 'took'}, {'4': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}]))
print(sentence([
        {'4': 'dog' }, {'2': 'took'}, {'3': 'his'},
        {'-2': 'Vatsan'}, {'5': 'for'}, {'6': 'a'}, {'12': 'spin'}
       ]))

"""
Reverse the bits in an integer

Write a function that reverses the bits in an integer.

For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

You can assume that the number is not negative.
"""

print('*** Reverse the bits in an integer ***')


def reverse_bits(n):
    return int(''.join(reversed(list(str(bin(n)).split('b')[1]))), 2)


print(reverse_bits(417))


"""
Sum a list but ignore any duplicates

Please write a function that sums a list, but ignores any duplicate items in the list.

For instance, for the list [3, 4, 3, 6] , the function should return 10.
"""

print('*** Sum a list but ignore any duplicates ***')


def sum_no_duplicates(l):
    return sum([i for i in l if l.count(i) == 1])


print(sum_no_duplicates([3, 4, 3, 6]))


"""
Swapping Cards

Two players draw a pair of numbered cards so that both players can form a 2 digit number. 
A winner can be decided if one player's number is larger than the other.

However, there is a rule where a player can swap any one of their cards with any one of the other 
player's cards in a gamble to get a higher number! Note that it is illegal to swap the order of 
your own cards. That means if you draw a 1 then a 9, you cannot swap them to get 91.

Paul's strategy is to always swap his lowest number with the opponent's ten's digit. 
Return whether this results in Paul winning the round.

    n1 is Paul's number
    n2 is his opponent's number

Worked Example

(41, 79) ➞ true
# Paul's lowest number is 1
# The opponent's ten's digit is 7
# After the swap: 47 > 19
# Paul wins the round

Notes

    If both of Paul's digits are the same, swap the ten's digit with the opponent's (paul likes to live riskily).
    The cards don't include the number 0.
    11 <= All numbers <= 99 (excluding numbers containing 0)
"""

print('*** Swapping Cards ***')


def swap_cards(n1, n2):
    pauls_nums = list(str(n1))
    opponent_nums = list(str(n2))
    if pauls_nums[0] == pauls_nums[1]:
        pauls_nums[0], opponent_nums[0] = opponent_nums[0], pauls_nums[0]
    else:
        pauls_min = pauls_nums.index(min(pauls_nums))
        pauls_nums[pauls_min], opponent_nums[0] = opponent_nums[0], pauls_nums[pauls_min]
    return ''.join(pauls_nums) > ''.join(opponent_nums)


print(swap_cards(41, 98))
print(swap_cards(67, 53))
print(swap_cards(77, 54))


"""
From A to Z

Given a string indicating a range of letters, return a string which includes all the letters in that range, 
including the last letter. Note that if the range is given in capital letters, return the string in capitals also!
Examples

gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"

gimme_the_letters("h-o") ➞ "hijklmno"

gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"

gimme_the_letters("J-J") ➞ J"
"""

print('*** From A to Z ***')


def gimme_the_letters(sp):
    letters = string.ascii_lowercase if sp[0] >= 'a' else string.ascii_uppercase
    sp_start = sp[0]
    sp_end = sp[-1]
    return ''.join(i for i in letters[letters.index(sp_start):letters.index(sp_end)+1])


print(gimme_the_letters("a-z"))
print(gimme_the_letters("h-o"))
print(gimme_the_letters("Q-Z"))


"""
Refactored Greeting

The following code could use a bit of object-oriented artistry. 
While it's a simple method and works just fine as it is, in a larger system it's 
best to organize methods into classes/objects. (Or, at least, something similar depending on your language)

Refactor the following code so that it belongs to a Person class/object. 
Each Person instance will have a greet method. The Person instance should be instantiated 
with a name so that it no longer has to be passed into each greet method call.

Here is how the final refactored code would be used:

joe = Person('Joe')
joe.greet('Kate') # should return 'Hello Kate, my name is Joe'
joe.name          # should == 'Joe'
"""


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def greet(self, gname):
        return f"Hello {gname}, my name is {self.name}"


p = Person('Jack')
print(p.name)
print(p.greet('Kate'))


"""
Number of Decimal Digits

Determine the total number of digits in the integer (n>=0) given as input to the function. 
For example, 9 is a single digit, 66 has 2 digits and 128685 has 6 digits. Be careful to avoid overflows/underflows.
"""

print('*** Number of Decimal Digits ***')


def digits(n):
    return len(str(n))


print(digits(9876543210))


"""
Odd or Even?

Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).
Examples:

Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
"""

print('*** Odd or Even? ***')


def odd_or_even(arr):
    s = sum(arr)
    return 'even' if s == 0 or s % 2 == 0 else 'odd'


print(odd_or_even([0]))
print(odd_or_even([0, 1, 4]))


"""
Building Strings From a Hash

Complete the solution so that it takes the object (JavaScript/CoffeeScript) or 
hash (ruby) passed in and generates a human readable string from its key/value pairs.

The format should be "KEY = VALUE". Each key/value pair should be separated by a comma except for the last pair.

Example:

solution({"a": 1, "b": '2'}) # should return "a = 1,b = 2"
"""

print('*** Building Strings From a Hash ***')


def solution(pairs):
    return ','.join(sorted([f'{key} = {value}' for key, value in pairs.items()]))


print(solution({'a': 1, 'b': 2})) # should return "a = 1,b = 2"


"""
Minimum Steps (Array Series #6)

minimumSteps({1, 10, 12, 9, 2, 3}, 6)  ==>  return (2)

Explanation:

    We add two smallest elements (1 + 2), their sum is 3 .

    Then we add the next smallest number to it (3 + 3) , so the sum becomes 6 .

    Now the result is greater or equal to 6 , Hence the output is (2) i.e (2) operations are required to do this .
"""

print('*** Minimum Steps (Array Series #6) ***')


def minimum_steps(numbers, value):
    numbers.sort()
    count = 0
    s = numbers[0]
    if value < s: return 0
    for i in range(1, len(numbers)+1):
        s += numbers[i]
        count += 1
        if s >= value:
            return count


print(minimum_steps([4,6,3], 7))
print(minimum_steps([19,98,69,28,75,45,17,98,67], 464))
print(minimum_steps([4,6,3], 2))


"""
Initialize my name

Some people just have a first name; some people have first and last names and some 
people have first, middle and last names.

You task is to initialize the middle names (if there is any).
Examples

'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'
"""

print('*** Initialize my name ***')


def initialize_names(name):
    l = name.split()
    l[1:-1] = map(lambda x: f'{x[0]}.', l[1:-1])
    return ' '.join(l)


print(initialize_names('Jack Ryan'))
print(initialize_names('Alice Betty Catherine Davis'))


"""
Decompose single strand DNA into 3 reading frames


Input

In a single strand of DNA you find 3 Reading frames, take for example the following input sequence:

AGGTGACACCGCAAGCCTTATATTAGC

Output

For the output we are going to take the combinations and show them in the following manner:

Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC
Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC
Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C
"""

print('*** Decompose single strand DNA into 3 reading frames ***')


def decompose_single_strand(single_strand):
    frame_1 = ' '.join([single_strand[i:i+3] for i in range(0, len(single_strand), 3)])
    frame_2 = single_strand[0] + ' ' + ' '.join([single_strand[i:i+3] for i in range(1, len(single_strand), 3)])
    frame_3 = single_strand[:2] + ' ' + ' '.join([single_strand[i:i + 3] for i in range(2, len(single_strand), 3)])
    return f'Frame 1: {frame_1}\nFrame 2: {frame_2}\nFrame 3: {frame_3}'


print(decompose_single_strand('AGGTGACACCGCAAGCCTTATATTAGC'))


"""
String matchup

Example

array1 = ['abc', 'abc', 'xyz', 'cde', 'uvw']
array2 = ['abc', 'cde', 'uap']

How many times do the elements in array2 appear in array1?

    'abc' appears twice in the first array (2)
    'cde' appears only once (1)
    'uap' does not appear in the first array (0)

Therefore, solve(array1, array2) = [2, 1, 0]
"""

print('*** String matchup ***')


def solve(a, b):
    return [a.count(i) for i in b]


print(solve(['abc', 'abc', 'xyz', 'abcd', 'cde'], ['abc', 'cde', 'uap']))


"""
Number Pairs

In this Kata the aim is to compare each pair of integers from 2 arrays, and return a new array of large numbers.

Note: Both arrays have the same dimensions.

Example:

arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]
"""

print('*** Number Pairs ***')


def get_larger_numbers(a, b):
    return [a[i] if a[i] > b[i] else b[i] for i in range(len(a))]


print(get_larger_numbers([13, 64, 15, 17, 88], [23, 14, 53, 17, 80]))


"""
Check three and two

Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), 
check if the array contains three and two of the same values.
Examples

["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"

"""

print('*** Check three and two ***')


def check_three_and_two(array):
    s = set(array)
    return {array.count(i) for i in s} == {2, 3}


print(check_three_and_two(["a", "a", "a", "b", "b"]))
print(check_three_and_two(["a", "c", "a", "c", "b"]))
print(check_three_and_two(["a", "a", "a", "a", "a"]))


"""
Inspiring Strings

When given a string of space separated words, return the word with the longest length. 
If there are multiple words with the longest length, return the last instance of the word with the longest length.

Example:

'red white blue' //returns string value of white

'red blue gold' //returns gold
"""

print('*** Inspiring Strings ***')


def longest_word(string_of_words):
    return (sorted(string_of_words.split(), key=len))[-1]


print(longest_word('a b c d each'))
print(longest_word('each step'))


"""
Powers of 3

Given a positive integer N, return the largest integer k such that 3^k < N.

For example,

largest_power(3) == 0
largest_power(4) == 1
"""

print('*** Powers of 3 ***')


def largest_power(N):
    i = 0
    while 3 ** i < N:
        i += 1
    return i - 1


print(largest_power(2))
print(largest_power(4))


"""
Number of Divisions

Example

For example the number 6 can be divided by 2 two times:

1. 6 / 2 = 3
2. 3 / 2 = 1 remainder = 1
"""

print('*** Number of Divisions ***')


def divisions(n, divisor):
    count = 0
    while divisor <= n:
        n = int(n / divisor)
        count += 1
    return count


print(divisions(6, 2))
print(divisions(2, 3))
print(divisions(5, 5))
print(divisions(2450, 5))


"""
Dominant array elements

An element in an array is dominant if it is greater than all elements to its right. 
You will be given an array and your task will be to return a list of all dominant elements. For example:

solve([1,21,4,7,5]) = [21,7,5] because 21, 7 and 5 are greater than elments to their right. 
solve([5,4,3,2,1]) = [5,4,3,2,1]

Notice that the last element is always included. All numbers will be greater than 0.
"""

print('*** Dominant array elements ***')


def solve(arr):
    res = []
    for i in range(len(arr)):
        if all([arr[i] > j for j in arr[i+1:]]):
            res.append(arr[i])
    return res


print(solve([16,17,14,3,14,5,2]))


"""
Find the lucky numbers

Write a function filterLucky/filter_lucky() that accepts a list of integers and filters the 
list to only include the elements that contain the digit 7.

For example,

ghci> filterLucky [1,2,3,4,5,6,7,68,69,70,15,17]
[7,70,17]
"""

print('*** Find the lucky numbers ***')


def filter_lucky(lst):
    return [i for i in lst if '7' in str(i)]


print(filter_lucky([1,2,3,4,5,6,7,68,69,70,15,17]))


"""
Ordering the words!

"hello world" => " dehllloorw"
"bobby"       => "bbboy"
""            => "Invalid String!"
"!Hi You!"    => " !!HYiou"
"""

print('*** Ordering the words! ***')


def order_word(s):
    if not s: return "Invalid String!"
    return ''.join(sorted(s))


print(order_word("hello world"))
print(order_word(''))


"""
Simple letter removal

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first.

For example: 
solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b' 
solve('abracadabra', 8) = 'rdr'
solve('abracadabra',50) = ''
"""

print('*** Simple letter removal ***')


def solve(st,k):
    letters = string.ascii_lowercase
    for i in letters:
        count = st.count(i)
        if count <= k:
            st = st.replace(i, '')
            k -= count
        else:
            st = st.replace(i, '', k)
            break
    return st


print(solve('abracadabra', 1))


"""
Fizz Buzz

Return an array containing the numbers from 1 to N, where N is the parametered value.

Replace certain values however if any of the following conditions are met:

    If the value is a multiple of 3: use the value "Fizz" instead
    If the value is a multiple of 5: use the value "Buzz" instead
    If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead

N will never be less than 1.

Method calling example:

fizzbuzz(3) -->  [1, 2, "Fizz"]
"""

print('*** Fizz Buzz ***')


def fizzbuzz(n):
    res = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            res.append('FizzBuzz')
        elif i % 5 == 0:
            res.append('Buzz')
        elif i % 3 == 0:
            res.append('Fizz')
        else:
            res.append(i)
    return res


print(fizzbuzz(15))


"""
Concatenated Sum

original number =2997 , n=3
2997 = 222+999+999+777 and here each digit is concatenated three times.

original number=-2997 , n=3

-2997 = -222-999-999-777 and here each digit is concatenated three times
"""

print('*** Concatenated Sum ***')


def check_concatenated_sum(n, t):
    x = sum([int(i * t if t > 1 else i) for i in list(str(abs(n)))])
    return True if x == abs(n) else False


print(check_concatenated_sum(2997, 3))
print(check_concatenated_sum(-198, 2))
print(check_concatenated_sum(198, 0))


"""
Alphabetize a list by the nth character 

Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n). 
The function should alphabetize the list based on the nth letter of each word.

The letters should be compared case-insensitive. If both letters are the same, order them normally 
(lexicographically), again, case-insensitive.

Example:

sort_it('bid, zag', 2) #=> 'zag, bid'
"""

print('*** Alphabetize a list by the nth character ***')


def sort_it(words, n):
    l = words.split(', ')
    return ', '.join(sorted(l, key=lambda x: x[n-1]))


print(sort_it('bill, bell, ball, bull', 2))


"""
Alternate capitalization

Given a string, capitalize the letters that occupy even indexes and odd indexes separately, 
and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.
"""

print('*** Alternate capitalization ***')


def capitalize(s):
    l = list(s)
    res = []
    even = ''.join([value.upper() if idx % 2 == 0 else value.lower() for idx, value in enumerate(l)])
    odd = ''.join([value.upper() if idx % 2 != 0 else value.lower() for idx, value in enumerate(l)])
    res.append(even)
    res.append(odd)
    return res


print(capitalize('abcdef'))


"""
Alphabet symmetry

Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. 
In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy 
the positions they would occupy in the alphabet, which are positions 4 and 5.

Given an array of words, return an array of the number of letters that occupy their positions 
in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) = [4, 3, 1]
"""

print('*** Alphabet symmetry ***')


def solve(strings : list[str]) -> list[int]:
    letters = {'a': 0, 'b': 1, 'c': 2, 'd':3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
               'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22,
               'x': 23, 'y': 24, 'z': 25}
    count = 0
    res = []
    for i in strings:
        for idx, letter in enumerate(i.lower()):
            if idx == letters[letter]:
                count += 1
        res.append(count)
        count = 0
    return res


print(solve(["abode","ABc","xyzD"]))


"""
Sorting Dictionaries

Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?

Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

The list must be sorted by the value and be sorted largest to smallest.
Examples

sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
"""

print('*** Sorting Dictionaries ***')


def sort_dict(d):
    return list(sorted(d.items(), key=lambda x: x[1], reverse=True))


print(sort_dict({1:2, 2:4, 3:6}))


"""
ReOrdering

>>> re_ordering('ming Yao')
'Yao ming'

>>> re_ordering('Mano donowana')
'Mano donowana'

>>> re_ordering('wario LoBan hello')
'LoBan wario hello'

>>> re_ordering('bull color pig Patrick')
'Patrick bull color pig'
"""

print('*** ReOrdering ***')


def re_ordering(text):
    l = text.split()
    el = [value for idx, value in enumerate(l) if value[0].isupper()]
    l.remove(el[0])
    return ' '.join(el + l)


print(re_ordering('wario LoBan hello'))
print(re_ordering('bull color pig Patrick'))


"""
Closest to Zero

[2, 4, -1, -3]  => -1
[5, 2, -2]      => None
[5, 2, 2]       => 2
[13, 0, -6]     => 0
"""


def closest(lst):
    m = min(lst, key=lambda x: abs(x))
    if not m or -m not in lst:
        return m


print(closest([2, 4, -1, -3]))
print(closest([5, 2, -2]))
print(closest([5, 2, 2]))
print(closest([5, -5, -2, 5, -3]))
print(closest([5, 1, -1, 2, -10]))


"""
List Filtering

filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

print('*** List Filtering ***')


def filter_list(l):
    return [i for i in l if type(i) is int]


print(filter_list([1, 2, 'a', 'b', '1']))


"""
Only one

 only_one() == False
  only_one(True, False, False) == True
  only_one(True, False, False, True) == False
  only_one(False, False, False, False) == False  
"""

print('*** Only one ***')


def only_one(*args):
    return args.count(True) == 1


print(only_one(True, False))


"""
Case-sensitive!

Your task is very simple. Given an input string s, case_sensitive(s), check whether all letters are lowercase or not. 
Return True/False and a list of all the entries that are not lowercase in order of their appearance in s.

For example, case_sensitive('codewars') returns [True, []], but case_sensitive('codeWaRs') returns [False, ['W', 'R']].
"""

print('*** Case-sensitive! ***')


def case_sensitive(s):
    letters = [i for i in s if i.isupper()]
    return [True if len(letters) == 0 else False, letters]


print(case_sensitive('asd'))
print(case_sensitive('cellS'))


"""
Is it a vowel on this position?

{
checkVowel('cat', 1)  ->   true // 'a' is a vowel
checkVowel('cat', 0)  ->   false // 'c' is not a vowel
checkVowel('cat', 4)  ->   false // this position doesn't exist
}
"""

print('*** Is it a vowel on this position? ***')


def check_vowel(strng, position):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if len(strng)-1 >= position >= 0 and strng[position].lower() in vowels else False


print(check_vowel('cat', 1))
print(check_vowel('Amanda', 0))


"""
The @ operator

I invented a new operator, @, which is left associative.

a @ b = (a + b) + (a - b) + (a * b) + (a // b)

Side note: ~~ is shorthand for Math.floor.

Given a string containing only integers and the operators, find out the value of that string.

The strings will always be "well formed", meaning with a space on each side of the operators, except in TypeScript, where string may appear like this: 0@1@2

1 @ 1 = (1 + 1) + (1 - 1) + (1 * 1) + (1 // 1) = 4
3 @ 2 = 13
6 @ 9 = 66

4 @ -4 = -9\
1 @ 1 @ -4 = -9 (1 @ 1 is 4, 4 @ -4 is -9)
2 @ 2 @ 2 = 40
0 @ 1 @ 2 = 0
5 @ 0 = None
"""

print('The @ operator')


def operator(a, b):
    return (a + b) + (a - b) + (a * b) + (a // b) if a != 0 or b != 0 else None


def evaluate(equation):
    l = list(map(int, (equation.split(' @ '))))
    try:
        res = operator(l[0], l[1])
        for i in l[2:]:
            res = operator(res, i)
        return res
    except Exception:
        return None


print(evaluate('1 @ 1'))
print(evaluate('1 @ 1 @ -4'))


"""
Sort by Example

Example:

Arr: [1,3,4,4,4,4,5]

Example Arr: [4,1,2,3,5]

Result: [4,4,4,4,1,3,5]
"""


def example_sort(arr, example_arr):
    # your code here
    res = []
    for i in example_arr:
        for j in arr:
            if j == i:
                res.append(i)
    return res


print(example_sort([1,3,4,4,4,4,5], [4,1,2,3,5]))


"""
Largest Elements

Write a program that outputs the top n elements from a list.

Example:

largest(2, [7,6,5,4,3,2,1])
# => [6,7]
"""

print('*** Largest Elements ***')


def largest(n, xs):
    """Find the n highest elements in a list"""
    return (sorted(xs, reverse=True)[:n])[::-1]


print(largest(2, [7,6,5,4,3,2,1]))


"""
Simple Fun #20: First Reverse Try

Example

For arr = [1, 2, 3, 4, 5], the output should be [5, 2, 3, 4, 1]
"""

print('*** Simple Fun #20: First Reverse Try ***')


def first_reverse_try(arr):
    if len(arr) <= 1: return arr
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


print(first_reverse_try([1, 2, 3, 4, 5]))


"""
Slice the middle of a list backwards

Write a function that takes a list of at least four elements as an argument and 
returns a list of the middle two or three elements in reverse order.
"""

print('*** Slice the middle of a list backwards ***')


def reverse_middle(lst):
    if len(lst) % 2 == 0:
        l = len(lst) // 2
        return (lst[l-1:l+1])[::-1]
    else:
        l = len(lst) // 2
        return (lst[l-1:l+2])[::-1]


print(reverse_middle([1, 2, 3, 4, 5]))


"""
Smallest value of an array

min([1,2,3,4,5], 'value') // => 1
min([1,2,3,4,5], 'index') // => 0
"""

print('*** Smallest value of an array ***')


def find_smallest(numbers, to_return):
    return min(numbers) if to_return == 'value' else numbers.index(min(numbers))


print(find_smallest([5,4,3,2,1],"value"))
print(find_smallest([5,4,3,2,1],"index"))


"""
Are the numbers in order?

in_asc_order([1,2,4,7,19]) # returns True
in_asc_order([1,2,3,4,5]) # returns True
in_asc_order([1,6,10,18,2,4,20]) # returns False
in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order
"""

print('*** Are the numbers in order? ***')


def in_asc_order(arr):
   return sorted(arr) == arr


print(in_asc_order([2, 1]))
print(in_asc_order([9,8,7,6,5,4,3,2,1]))
print(in_asc_order([1,2,3,4,5]))


"""
Odd Ones Out!

odd_ones_out([1, 2, 3, 1, 3, 3]) = [1, 1]

In the above example:

    the number 1 appears twice
    the number 2 appears once
    the number 3 appears three times

2 and 3 both appear an odd number of times, so they are removed from the list. The final result is: [1,1]

Here are more examples:

odd_ones_out([1, 1, 2, 2, 3, 3, 3]) = [1, 1, 2, 2]
odd_ones_out([26, 23, 24, 17, 23, 24, 23, 26]) = [26, 24, 24, 26]
odd_ones_out([1, 2, 3]) = []
odd_ones_out([1]) = []
"""

print('*** Odd Ones Out! ***')


def odd_ones_out(numbers):
    return [i for i in numbers if numbers.count(i) % 2 == 0]


print(odd_ones_out([1, 1, 2, 2, 3, 3, 3]))
print(odd_ones_out([1, 2, 3]))


"""
Rotate for a Max


Take a number: 56789. Rotate left, you get 67895.

Keep the first digit in place and rotate left the other digits: 68957.

Keep the first two digits in place and rotate the other ones: 68579.

Keep the first three digits and rotate left the rest: 68597. Now it is over since keeping the first 
four it remains only one digit which rotated is itself.

You have the following sequence of numbers:

56789 -> 67895 -> 68957 -> 68579 -> 68597

and you must return the greatest: 68957.
"""

print('*** Rotate for a Max ***')


def max_rot(n):
    lst = list(str(n))
    res = [n]
    for i in range(len(lst)):
        lst.append(lst.pop(i))
        res.append(int(''.join(lst)))
    return max(res)


print(max_rot(56789))


"""
Sum of array singles

In this Kata, you will be given an array of numbers in which two numbers occur 
once and the rest occur only twice. Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, 
and their sum is 15. Every other number occurs twice.
"""


print('*** Sum of array singles ***')


def repeats(arr):
    return sum([i for i in arr if arr.count(i) == 1])


print(repeats([4,5,7,5,4,8]))


"""
Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""

print('*** Shortest Word ***')


def find_short(s):
    return len((sorted([i for i in s.split(' ')], key=len))[0])


print(find_short("bitcoin take over the world maybe who knows perhaps"))


"""
Is that a real phone number? (British version)

Your task is to write a function that verifies whether a given string 
contains a valid British mobile (cell) phone number or not.

If valid, return 'In with a chance'.

If invalid, or if you're given an empty string, return 'Plenty more fish in the sea'.

A number can be valid in the following ways:

Here in the UK mobile numbers begin with '07' followed by 9 other digits, e.g. '07454876120'.

Sometimes the number is preceded by the country code, the prefix '+44', which replaces the '0' in ‘07’,
 e.g. '+447454876120'.

And sometimes you will find numbers with dashes in-between digits or on either side, e.g. '+44--745---487-6120' 
or '-074-54-87-61-20-'. As you can see, dashes may be consecutive.
"""

print('*** Is that a real phone number? (British version) ***')


def validate_number(st):
    st = st.replace('-', '')
    if (st.startswith('07') and len(st[2:]) == 9) or (st.startswith('+447') and len(st[4:]) == 9):
        return 'In with a chance'
    return 'Plenty more fish in the sea'


print(validate_number("07454876120"))
print(validate_number("-07599-51-4555"))
print(validate_number("0754876120"))
print(validate_number("+447+4435512555"))
print(validate_number("0745--487-61-20"))


"""
Guess the Word: Count Matching Letters

count_correct_characters("dog", "car"); #0 (No letters are in the correct position)
count_correct_characters("dog", "god"); #1 ("o")
count_correct_characters("dog", "cog"); #2 ("o" and "g")
count_correct_characters("dog", "cod"); #1 ("o")
count_correct_characters("dog", "bog"); #2 ("o" and "g")
count_correct_characters("dog", "dog"); #3 (Correct!)
"""

print('*** Guess the Word: Count Matching Letters ***')


def count_correct_characters(correct, guess):
    l1, l2 = len(correct), len(guess)
    if l1 != l2:
        raise 'error'
    res = 0
    for i in range(l1):
        if correct[i] == guess[i]:
            res += 1
    return res


print(count_correct_characters("dog", "car"))
print(count_correct_characters("dog", "dog"))


"""
Remove the minimum

Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with the lowest index. 
If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.
Examples

* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
"""

print('*** Remove the minimum ***')


def remove_smallest(numbers):
    if len(numbers) < 2: return []
    idx = numbers.index(min(numbers))
    return [value for i, value in enumerate(numbers) if i != idx]


print(remove_smallest([1,2,3,4,5]))


"""
Consecutive items

You are given a list of unique integers arr, and two integers a and b. 
Your task is to find out whether or not a and b appear consecutively in arr, and return a boolean value 
(True if a and b are consecutive, False otherwise).

It is guaranteed that a and b are both present in arr.
"""

print('*** Consecutive items ***')


def consecutive(arr, a, b):
    aa = arr.index(a)
    bb = arr.index(b)
    return abs(aa-bb) == 1


print(consecutive([1, 3, 5, 7], 3, 7))
print(consecutive([1, 3, 5, 7], 3, 1))


"""
Possibilities Array

A non-empty array a of length n is called an array of all possibilities if it contains 
all numbers between [0,a.length-1].Write a method named isAllPossibilities that accepts an integer array 
and returns true if the array is an array of all possibilities, else false.

Example:

a=[1,2,0,3]
a.length-1=3 
a includes [0,3] ,hence the function should return true
"""

print('*** Possibilities Array ***')


def is_all_possibilities(arr):
    if len(arr) == 0: return False
    return sorted(arr) == [i for i in range(len(arr))]


print(is_all_possibilities([0,2,19,4,4]))
print(is_all_possibilities([3,2,1,0]))


"""
String Reversing, Changing case, etc.

Given 2 string parameters, show a concatenation of:

    the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
    a separator in between both strings: @@@
    the 1st string reversed with inverted case and then mirrored; e.g Water -> RETAwwATER 
"""

print('*** String Reversing, Changing case, etc. ***')


def reverse_and_mirror(s1, s2):
    s1_1 = ' '.join(list(map(lambda x: x.swapcase()[::-1], s1.split(' ')[::-1])))
    s1_2 = ' '.join(list(map(lambda x: x.swapcase(), s1.split(' '))))
    s2 = ' '.join(list(map(lambda x: x.swapcase()[::-1], s2.split(' ')[::-1])))
    return f'{s2}@@@{s1_1}{s1_2}'


print(reverse_and_mirror('FizZ', 'buZZ'))
print(reverse_and_mirror("way to inVert","caSe of string"))
print(reverse_and_mirror('String Reversing', 'Changing Case'))


"""
Naughty or Nice

Santa is coming to town and he needs your help finding out who's been naughty or nice. 
You will be given an entire year of JSON data following this format:

{
    January: {
        '1': 'Naughty','2': 'Naughty', ..., '31': 'Nice'
    },
    February: {
        '1': 'Nice','2': 'Naughty', ..., '28': 'Nice'
    },
    ...
    December: {
        '1': 'Nice','2': 'Nice', ..., '31': 'Naughty'
    }
}

Your function should return "Naughty!" or "Nice!" depending on the total number of 
occurrences in a given year (whichever one is greater). If both are equal, return "Nice!"
"""

print('*** Naughty or Nice ***')


def naughty_or_nice(data):
    naughty = 0
    nice = 0
    for i, j in data.items():
        for m, k in j.items():
            if k == "Naughty":
                naughty += 1
            else:
                nice += 1
    return "Naughty!" if naughty > nice else "Nice!"


print(naughty_or_nice(
    {"January": {"1": "Naughty", "2": "Nice", "3": "Naughty", "4": "Nice", "5": "Nice",
                 "6": "Nice", "7": "Naughty", "8": "Nice", "9": "Nice", "10": "Naughty", "11": "Nice",
                 "12": "Nice", "13": "Nice", "14": "Naughty", "15": "Naughty", "16": "Naughty", "17": "Nice",
                 "18": "Nice", "19": "Naughty", "20": "Nice", "21": "Naughty", "22": "Nice", "23": "Naughty",
                 "24": "Nice", "25": "Naughty", "26": "Nice", "27": "Nice", "28": "Naughty", "29": "Nice",
                 "30": "Nice", "31": "Nice"},
     "February": {"1": "Nice", "2": "Naughty", "3": "Nice", "4": "Nice", "5": "Nice", "6": "Nice", "7": "Nice",
                  "8": "Nice", "9": "Naughty", "10": "Naughty", "11": "Naughty", "12": "Nice", "13": "Nice",
                  "14": "Naughty", "15": "Naughty", "16": "Nice", "17": "Nice", "18": "Naughty", "19": "Nice",
                  "20": "Nice", "21": "Nice", "22": "Nice", "23": "Nice", "24": "Naughty", "25": "Naughty",
                  "26": "Nice", "27": "Naughty", "28": "Nice"},
     "March": {"1": "Nice", "2": "Naughty", "3": "Nice", "4": "Nice", "5": "Nice", "6": "Naughty", "7": "Nice",
               "8": "Nice", "9": "Nice", "10": "Naughty", "11": "Naughty", "12": "Nice", "13": "Naughty",
               "14": "Naughty", "15": "Naughty", "16": "Nice", "17": "Nice", "18": "Nice", "19": "Naughty",
               "20": "Nice", "21": "Naughty", "22": "Naughty", "23": "Nice", "24": "Nice", "25": "Nice",
               "26": "Nice", "27": "Nice", "28": "Naughty", "29": "Nice", "30": "Nice", "31": "Naughty"},
     "April": {"1": "Naughty", "2": "Naughty", "3": "Nice", "4": "Nice", "5": "Nice", "6": "Naughty",
               "7": "Naughty", "8": "Nice", "9": "Nice", "10": "Nice", "11": "Nice", "12": "Nice",
               "13": "Naughty", "14": "Nice", "15": "Naughty", "16": "Naughty", "17": "Nice", "18": "Naughty",
               "19": "Nice", "20": "Naughty", "21": "Naughty", "22": "Nice", "23": "Nice", "24": "Naughty",
               "25": "Nice", "26": "Naughty", "27": "Naughty", "28": "Nice", "29": "Nice", "30": "Nice"},
     "May": {"1": "Nice", "2": "Naughty", "3": "Naughty", "4": "Nice", "5": "Nice", "6": "Nice", "7": "Naughty",
             "8": "Nice", "9": "Nice", "10": "Nice", "11": "Naughty", "12": "Naughty", "13": "Naughty",
             "14": "Naughty", "15": "Nice", "16": "Naughty", "17": "Naughty", "18": "Nice", "19": "Nice",
             "20": "Nice", "21": "Nice", "22": "Nice", "23": "Naughty", "24": "Naughty", "25": "Nice",
             "26": "Nice", "27": "Nice", "28": "Naughty", "29": "Naughty", "30": "Naughty", "31": "Nice"},
     "June": {"1": "Naughty", "2": "Nice", "3": "Naughty", "4": "Nice", "5": "Naughty", "6": "Nice",
              "7": "Nice", "8": "Nice", "9": "Nice", "10": "Naughty", "11": "Naughty", "12": "Nice",
              "13": "Nice", "14": "Naughty", "15": "Nice", "16": "Naughty", "17": "Naughty", "18": "Naughty",
              "19": "Nice", "20": "Nice", "21": "Nice", "22": "Nice", "23": "Nice", "24": "Nice",
              "25": "Nice", "26": "Nice", "27": "Nice", "28": "Nice", "29": "Naughty", "30": "Nice"},
     "July": {"1": "Nice", "2": "Nice", "3": "Nice", "4": "Naughty", "5": "Nice", "6": "Nice", "7": "Nice",
              "8": "Nice", "9": "Naughty", "10": "Nice", "11": "Nice", "12": "Naughty", "13": "Nice",
              "14": "Naughty", "15": "Nice", "16": "Nice", "17": "Naughty", "18": "Nice", "19": "Naughty",
              "20": "Nice", "21": "Nice", "22": "Nice", "23": "Nice", "24": "Naughty", "25": "Naughty",
              "26": "Nice", "27": "Naughty", "28": "Naughty", "29": "Nice", "30": "Nice", "31": "Nice"},
     "August": {"1": "Naughty", "2": "Nice", "3": "Naughty", "4": "Nice", "5": "Nice", "6": "Nice", "7": "Nice",
                "8": "Nice", "9": "Naughty", "10": "Naughty", "11": "Nice", "12": "Naughty", "13": "Nice",
                "14": "Naughty", "15": "Nice", "16": "Nice", "17": "Naughty", "18": "Nice", "19": "Naughty",
                "20": "Nice", "21": "Nice", "22": "Naughty", "23": "Naughty", "24": "Naughty", "25": "Naughty",
                "26": "Nice", "27": "Nice", "28": "Nice", "29": "Naughty", "30": "Naughty", "31": "Nice"},
     "September": {"1": "Naughty", "2": "Nice", "3": "Naughty", "4": "Nice", "5": "Nice", "6": "Nice", "7": "Nice",
                   "8": "Naughty", "9": "Naughty", "10": "Nice", "11": "Naughty", "12": "Naughty", "13": "Nice",
                   "14": "Naughty", "15": "Nice", "16": "Nice", "17": "Nice", "18": "Nice", "19": "Nice",
                   "20": "Naughty", "21": "Nice", "22": "Nice", "23": "Nice", "24": "Nice", "25": "Nice",
                   "26": "Naughty", "27": "Nice", "28": "Nice", "29": "Naughty", "30": "Nice"},
     "October": {"1": "Nice", "2": "Naughty", "3": "Naughty", "4": "Naughty", "5": "Naughty", "6": "Nice",
                 "7": "Nice", "8": "Naughty", "9": "Nice", "10": "Nice", "11": "Naughty", "12": "Nice",
                 "13": "Nice", "14": "Nice", "15": "Nice", "16": "Nice", "17": "Naughty", "18": "Naughty",
                 "19": "Nice", "20": "Nice", "21": "Naughty", "22": "Nice", "23": "Nice", "24": "Naughty",
                 "25": "Nice", "26": "Nice", "27": "Nice", "28": "Naughty", "29": "Naughty", "30": "Nice", "31": "Nice"},
     "November": {"1": "Naughty", "2": "Nice", "3": "Naughty", "4": "Nice", "5": "Nice", "6": "Nice", "7": "Nice",
                  "8": "Nice", "9": "Nice", "10": "Nice", "11": "Nice", "12": "Naughty", "13": "Naughty",
                  "14": "Naughty", "15": "Naughty", "16": "Nice", "17": "Naughty", "18": "Nice", "19": "Nice",
                  "20": "Nice", "21": "Naughty", "22": "Naughty", "23": "Nice", "24": "Naughty", "25": "Naughty",
                  "26": "Nice", "27": "Nice", "28": "Nice", "29": "Nice", "30": "Naughty"},
     "December": {"1": "Nice", "2": "Nice", "3": "Nice", "4": "Naughty", "5": "Nice", "6": "Naughty", "7": "Nice",
                  "8": "Naughty", "9": "Nice", "10": "Naughty", "11": "Naughty", "12": "Naughty", "13": "Naughty",
                  "14": "Naughty", "15": "Naughty", "16": "Nice", "17": "Nice", "18": "Nice", "19": "Naughty",
                  "20": "Nice", "21": "Naughty", "22": "Naughty", "23": "Nice", "24": "Nice", "25": "Naughty",
                  "26": "Nice", "27": "Nice", "28": "Nice", "29": "Nice", "30": "Nice", "31": "Nice"}}))


"""
Is it a letter?

Write function isItLetter or is_it_letter which tells us if given character is a uppercase or lowercase letter.
"""


print('*** Is it a letter? ***')


def is_it_letter(s):
    return s.isalpha()


print(is_it_letter('1'))
print(is_it_letter('!'))
print(is_it_letter('a'))


"""
Running out of space

For example, running this function on the array ['i', 'have','no','space'] 
would produce ['i','ihave','ihaveno','ihavenospace']
"""

print('*** Running out of space ***')


def spacey(array):
    res = [array[0]]
    buff = array[0]
    for i in range(1, len(array)):
        res.append(buff + array[i])
        buff += array[i]
    return res


print(spacey(['i', 'have','no','space']))


"""
Holiday II - Plane Seating
"""

print('*** Holiday II - Plane Seating ***')


def plane_seat(a):
    section = {'Front-': range(1, 21), 'Middle-': range(21, 41), 'Back-': range(41, 61)}
    seats = {'Left': 'ABC', 'Middle': 'DEF', 'Right': 'GHK'}
    num, letter = int(a[:-1]), a[-1]
    res = []
    for i, j in section.items():
        if num in j:
            res.append(i)
            break
    for i, j in seats.items():
        if letter in j:
            res.append(i)
            break
    return ''.join(res) if len(res) == 2 else 'No Seat!!'


print(plane_seat('2B'))
print(plane_seat('58I'))
print(plane_seat('60D'))


"""
Turn any word into a beef taco

We want to input a word as a string, and return a list representing that word as a taco.

Key

all vowels (except 'y') = beef

t = tomato

l = lettuce

c = cheese

g = guacamole

s = salsa

NOTE
We do not care about case here. 'S' is therefore equivalent to 's' in our taco.

Ignore all other letters; we don't want our taco uneccesarily clustered or else it will be too difficult to eat.

Note that no matter what ingredients are passed, our taco will always have a shell.
"""

print('*** Turn any word into a beef taco ***')


def tacofy(word):
    word = list(word.lower())
    tacos = {'t': 'tomato', 'l': 'lettuce', 'c': 'cheese', 'g': 'guacamole', 's': 'salsa', 'a': 'beef', 'e': 'beef',
             'i': 'beef', 'o': 'beef', 'u': 'beef'}
    res = [tacos[i] for i in word if i in tacos]
    return ['shell'] + res + ['shell']


print(tacofy(''))
print(tacofy('a'))
print(tacofy('ogl'))
print(tacofy("MaXwElL"))
print(tacofy("alel"))


"""
Change two-dimensional array

Function receive a two-dimensional square array of random integers. On the main diagonal, all the negative integers must be changed to 0, while the others must be changed to 1 (Note: 0 is considered non-negative, here).

(You can mutate the input if you want, but it is a better practice to not mutate the input)

Example:

Input array

[
  [-1,  4, -5, -9,  3 ],
  [ 6, -4, -7,  4, -5 ],
  [ 3,  5,  0, -9, -1 ],
  [ 1,  5, -7, -8, -9 ],
  [-3,  2,  1, -5,  6 ]
]

Output array

[
  [ 0,  4, -5, -9,  3 ],
  [ 6,  0, -7,  4, -5 ],
  [ 3,  5,  1, -9, -1 ],
  [ 1,  5, -7,  0, -9 ],
  [-3,  2,  1, -5,  1 ]
]
"""

print('*** Change two-dimensional array ***')


def matrix(array):
    for i, arr in enumerate(array):
        array[i][i] = 0 if array[i][i] < 0 else 1
    return array


print(matrix([
  [-1,  4, -5, -9,  3 ],
  [ 6, -4, -7,  4, -5 ],
  [ 3,  5,  0, -9, -1 ],
  [ 1,  5, -7, -8, -9 ],
  [-3,  2,  1, -5,  6 ]]))


"""
Character Counter

You are going to be given a word. Your job will be to make sure that each character in that word has the exact 
same number of occurrences. You will return true if it is valid, or false if it is not.

For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"

The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. 
The length will be 0 < length < 100.
Examples

    "abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
    "abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, 
    but "d" only appears once!
    "123abc!" is a valid word because all of the characters only appear once in the word.
"""

print('*** Character Counter ***')


def validate_word(word):
    word = word.lower()
    num = word.count(word[0])
    return len(set(word)) == len(word) / num


print(validate_word("abcabc"))
print(validate_word("Abcabc"))
print(validate_word("AbcabcC"))


"""
Odd-Even String Sort

Given a string s, your task is to return another string such that even-indexed and odd-indexed 
characters of s are grouped and the groups are space-separated. Even-indexed group comes as first, followed 
by a space, and then by the odd-indexed part.
Examples

input:    "CodeWars" => "CdWr oeas"
           ||||||||      |||| ||||
indices:   01234567      0246 1357

Even indices 0, 2, 4, 6, so we have "CdWr" as the first group.
Odd indices are 1, 3, 5, 7, so the second group is "oeas".
And the final string to return is "Cdwr oeas".
"""

print('*** Odd-Even String Sort ***')


def sort_my_string(s):
    odd = ''.join([value for idx, value in enumerate(s) if idx % 2 != 0])
    even = ''.join([value for idx, value in enumerate(s) if idx % 2 == 0])
    return f'{even} {odd}'


print(sort_my_string("YCOLUE'VREER"))
print(sort_my_string("CodeWars"))


"""
Mutate My Strings

 will give you two strings. I want you to transform stringOne into stringTwo one letter at a time.

Example:

stringOne = 'bubble gum';
stringTwo = 'turtle ham';

Result:
bubble gum
tubble gum
turble gum
turtle gum
turtle hum
turtle ham
"""

print('*** Mutate My Strings ***')


def mutate_my_strings(s1,s2):
    res = f'{s1}\n'
    s1 = list(s1)
    s2 = list(s2)
    for idx, value in enumerate(s1):
        if s1[idx] != s2[idx]:
            s1[idx] = s2[idx]
            res += f'{"".join(s1)}\n'
    return res


print(mutate_my_strings("bubble gum", "turtle ham"))


"""
Integer Difference

Write a function that accepts two arguments: an array/list of integers and another integer (n).

Determine the number of times where two integers in the array have a difference of n.

For example:

[1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
[1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)
"""

print('*** Integer Difference ***')


def int_diff(lst, n):
    res = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs(lst[i] - lst[j]) == n:
                res += 1
    return res


print(int_diff([1, 1, 5, 6, 9, 16, 27], 4))
print(int_diff([1,2,3,4], 0))


"""
String Scramble

Given a string and an array of index numbers, return the characters of the string rearranged to be in 
the order specified by the accompanying array.

Ex:

scramble('abcd', [0,3,1,2]) -> 'acdb'

The string that you will be returning back will have: 'a' at index 0, 'b' at index 3, 'c' at index 1, 'd' at index 2, 
because the order of those characters maps to their corresponding numbers in the index array.

In other words, put the first character in the string at the index described by the first element of the array

You can assume that you will be given a string and array of equal length and both containing valid characters 
(A-Z, a-z, or 0-9).
"""

print('*** String Scramble ***')


def scramble(strng, array):
    res = ['a'] * len(array)
    for idx, value in enumerate(array):
        res[value] = strng[idx]
    return ''.join(res)


print(scramble('abcd', [0,3,1,2]))


"""
String basics

    Remove all hashtags
    Remove the leading "uid" from each user ID
    Return an array of strings --> split the string
    Each user ID should be written in only lowercase characters
    Remove leading and trailing whitespaces
"""

print('*** String basics ***')


def get_users_ids(st):
    res = st.split(',')
    for idx, value in enumerate(res):
        res[idx] = value.lower().replace("#", "").replace("uid", "", 1).strip()
    return res


print(get_users_ids("uidMultipleuid"))
print(get_users_ids("uid12 ab, uid#, uidMiXeDcHaRs"))


"""
Sum it continuously

Make a function "add" that will be able to sum elements of list continuously and return a new list of sums.

For example:

add [1,2,3,4,5] == [1, 3, 6, 10, 15], because it's calculated like 
this : [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4, 1 + 2 + 3 + 4 + 5]
"""

print('*** Sum it continuously ***')


def add(lst):
    res = []
    buf = 0
    for idx, value in enumerate(lst):
        buf += lst[idx]
        res.append(buf)
    return res


print(add([1,2,3,4,5]))


"""
Least Larger

Given an array of numbers and an index, return either the index of the smallest number that is 
larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).
Notes

Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.
Example

least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
"""

print('*** Least Larger ***')


def least_larger(a, i):
    num = a[i]
    l = [i for i in a if i > num]
    return a.index(min(l)) if l else -1


print(least_larger([4, 1, 3, 5, 6], 0))
print(least_larger([4, 1, 3, 5, 6], 4))
print(least_larger([1, 3, 5, 2, 4], 0))


"""
Lottery machine

our task is to write an update for a lottery machine. 
Its current version produces a sequence of random letters and integers (passed as a string to the function). 
Your code must filter out all letters and return unique integers as a string, in their order of first appearance. 
If there are no integers in the string return "One more run!"
Examples

"hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5"
"""

print('*** Lottery machine ***')


def lottery(s):
    l = ''.join(list(collections.OrderedDict.fromkeys([i for i in s if i.isdigit()]).keys()))
    return l if l else "One more run!"


print(lottery("hPrBKWDH8yc6Lt5NQZWQ"))
print(lottery("ynMAisVpHEqpqHBqTrwH"))
print(lottery("555"))


"""
Sum of Minimums!

Given a 2D ( nested ) list ( array, vector, .. ) of size m * n, your task is to find the sum of the 
minimum values in each row.

For Example:

[ [ 1, 2, 3, 4, 5 ]        #  minimum value of row is 1
, [ 5, 6, 7, 8, 9 ]        #  minimum value of row is 5
, [ 20, 21, 34, 56, 100 ]  #  minimum value of row is 20
]

So the function should return 26 because the sum of the minimums is 1 + 5 + 20 = 26.
"""


print('*** Sum of Minimums! ***')


def sum_of_minimums(numbers):
    return sum([min(i) for i in numbers])


print(sum_of_minimums([ [ 1, 2, 3, 4, 5 ], [ 5, 6, 7, 8, 9 ], [ 20, 21, 34, 56, 100 ] ]))


"""
Evens times last

Given a sequence of integers, return the sum of all the integers that have an even index (odd index in COBOL), 
multiplied by the integer at the last index.

Indices in sequence start from 0.

If the sequence is empty, you should return 0.
"""

print('*** Evens times last ***')


def even_last(numbers):
    if len(numbers) == 0: return 0
    return sum([value for idx, value in enumerate(numbers) if idx% 2 == 0]) * numbers[-1]


print(even_last([2, 3, 4, 5]))
print(even_last([]))


"""
Double Every Other

Write a function that doubles every second integer in a list, starting from the left.

Example:

For input array/list :

[1,2,3,4]

the function should return :

[1,4,3,8]
"""

print('*** Double Every Other ***')


def double_every_other(lst):
    res = []
    for idx, value in enumerate(lst):
        if idx % 2 != 0:
            res.append(value * 2)
        else:
            res.append(value)
    return res


print(double_every_other([1,2,3,4]))


"""
Check the exam

The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. 
The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, 
giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, 
represented as an empty string (in C the space character is used).

If the score < 0, return 0.

For example:

    Correct answer    |    Student's answer   |   Result         
 ---------------------|-----------------------|-----------
 ["a", "a", "b", "b"]   ["a", "c", "b", "d"]  →     6
 ["a", "a", "c", "b"]   ["a", "a", "b", "" ]  →     7
 ["a", "a", "b", "c"]   ["a", "a", "b", "c"]  →     16
 ["b", "c", "b", "a"]   ["" , "a", "a", "c"]  →     0
"""


print('*** Check the exam ***')


def check_exam(arr1, arr2):
    res = 0
    for idx, value in enumerate(arr2):
        if value and value == arr1[idx]:
            res += 4
        elif not value:
            res += 0
        else:
            res -= 1
    return res if res > 0 else 0


print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))
print(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]))


"""
Ones and Zeros

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

Examples:

Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
"""

print('*** Ones and Zeros ***')


def binary_array_to_number(arr):
    return int(''.join(list(map(str, arr))), 2)


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))


"""
Find the missing element between two arrays

Given two integer arrays where the second array is a shuffled duplicate of the first 
array with one element missing, find the missing element.

Please note, there may be duplicates in the arrays, so checking if a numerical value exists 
in one and not the other is not a valid solution.

find_missing([1, 2, 2, 3], [1, 2, 3]) => 2

find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]) => 8
"""

print('*** Find the missing element between two arrays ***')


def find_missing(arr1, arr2):
    # version 1
    # return sum(arr1) - sum(arr2)
    sorted_arr1 = sorted(arr1)
    sorted_arr2 = sorted(arr2)
    lst = list(itertools.zip_longest(sorted_arr1, sorted_arr2))
    for i in lst:
        if i[0] == i[1]:
            continue
        return i[0]


print(find_missing([1, 2, 2, 3], [1, 2, 3]))
print(find_missing([6, 1, 3, 6, 8, 2], [3, 6, 6, 1, 2]))


"""
Divisible by previous digit?

Take a number and check each digit if it is divisible by the digit on its left checked and return an array of booleans.

The booleans should always start with false becase there is no digit before the first one.
Examples

73312        => [false, false, true, false, true]
2026         => [false, true, false, true]
635          => [false, false, false]
"""

print('*** Divisible by previous digit? ***')


def divisible_by_last(n):
    res = [False]
    n = str(n)
    for i in range(1, len(n)):
        try:
            if int(n[i]) % int(n[i-1]) == 0:
                res.append(True)
            else:
                res.append(False)
        except ZeroDivisionError:
            res.append(False)
    return res


print(divisible_by_last(73312))
print(divisible_by_last(635))
print(divisible_by_last(2026))


"""
Partial Word Searching

Write a method that will search an array of strings for all strings that contain another string, 
ignoring capitalization. Then return an array of the found strings.

The method takes two parameters, the query string and the array of strings to search, and returns an array.

If the string isn't contained in any of the strings in the array, the method returns an array containing 
a single string: "Empty" (or Nothing in Haskell, or "None" in Python and C)
Examples

If the string to search for is "me", and the array to search is ["home", "milk", "Mercury", "fish"], 
the method should return ["home", "Mercury"].
"""

print('*** Partial Word Searching ***')


def word_search(query, seq):
    res = [i for i in seq if query.lower() in i.lower()]
    return res if res else ['None']


print(word_search("ab", ["za", "ab", "abc", "zab", "zbc"]))
print(word_search("abcd", ["za", "aB", "Abc", "zAB", "zbc"]))
