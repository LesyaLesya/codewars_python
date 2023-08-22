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
