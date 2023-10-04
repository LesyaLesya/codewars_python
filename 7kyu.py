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
