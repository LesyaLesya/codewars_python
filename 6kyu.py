import string
import re
import collections
import sys
from time import sleep
import time
from collections import OrderedDict

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
Number Format

Format any integer provided into a string with "," (commas) in the correct places.

Example:

For n = 100000 the function should return '100,000';
For n = 5678545 the function should return '5,678,545';
for n = -420902 the function should return '-420,902'.


"""
print('*** Number Format ***')


def number_format(n):
    # print(format(n, ','))
    return "{:,d}".format(n)


print(number_format(100000))
print(number_format(5678545))
print(number_format(-420902))
print(number_format(5020520718))


"""
Consonant value

Given a lowercase string that has alphabetic characters only and no spaces, return the highest value 
of consonant substrings. Consonants are any letters of the alphabet except "aeiou".

We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.

For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

-- The consonant substrings are: "z", "d" and "cs" and the values are z = 26, d = 4 and cs = 3 + 19 = 22. 
The highest is 26.
solve("zodiacs") = 26

For the word "strength", solve("strength") = 57
-- The consonant substrings are: "str" and "ngth" with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. 
The highest is 57.
"""
print('*** Consonant value ***')


def solve(s):
    alphabet_dict = {key: value for key, value in zip(list(string.ascii_lowercase), range(1, 27))}
    list_s = re.split('a|e|i|o|u', s)
    values = []
    for i in list_s:
        summa = 0
        for j in i:
            summa += alphabet_dict.get(j)
        values.append(summa)
    return max(values)


print(solve("strength"))
print(solve("zodiacs"))


"""
All Star Code Challenge

This Kata is intended as a small challenge for my students

The scroller works by replacing the current text string with a similar text string, 
but with the first letter shifted to the end; this simulates movement.

Your father is far too busy with the business to worry about such details, so, naturally, 
he's making you come up with the text strings.

Create a function named rotate() that accepts a string argument and returns an array of strings with each letter 
from the input string being rotated to the end.

rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]

Note: The original string should be included in the output array. The order matters. Each element of the output 
array should be the rotated version of the previous element. The output array SHOULD be the same length 
as the input string. The function should return an empty array with a 0 length string, '', as input.

"""
print('*** All Star Code Challenge ***')


def rotate(str_):
    l = []
    for i in range(len(str_)):
        str_ = str_[1:] + str_[0]
        l.append(str_)
    return l


print(rotate("Hello"))
print(rotate(" "))
print(rotate("123"))
print(rotate(""))


"""
Find The Parity Outlier

You are given an array (which will have a length of at least 3, but could be very large) 
containing integers. The array is either entirely comprised of odd integers or entirely 
comprised of even integers except for a single integer N. Write a method that takes the array 
as an argument and returns this "outlier" N.
Examples

[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)


"""

print('*** Find The Parity Outlier ***')


def find_outlier(integers):
    ev = 0
    odd = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            ev += 1
        else:
            odd += 1
    if ev > odd:
        n = [i for i in integers if i % 2 != 0]
        return n[0]
    else:
        n = [i for i in integers if i % 2 == 0]
        return n[0]


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))


"""
Last non-zero digit of factorial

Your task is to find the last non-zero digit of n!n!n! (factorial).

n!=1×2×3×⋯×nn! = 1 \times 2 \times 3 \times \dots \times nn!=1×2×3×⋯×n

Example:
If n=12n = 12n=12, your function should return 666 since 
12!=47900160012 != 479001\bold{6}0012!=479001600
Input

Non-negative integer n
Range: 0 - 2.5E6
Output

Last non-zero digit of n!n!n!
"""
print('*** Last non-zero digit of factorial ***')


def last_digit(n):
    sys.set_int_max_str_digits(int(2.5E6))

    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    n = list(str(fact))
    for i in n[::-1]:
        if i != '0':
            return int(i)


print(last_digit(3))
print(last_digit(99))
print(last_digit(387))
print(last_digit(1673))
print(last_digit(10000))


"""
Identify Best Planet

 A space agency recently launched a new satellite with the primary goal of identifying the most suitable 
 planet within a given solar system to support human life. The satellite is equipped to scan entire solar 
 systems and add each detected planet to a list. The satellite uses the following format when inputting 
 planets into an array: [elements]_[surface area]. In this format, each element is represented by its 
 chemical symbol from the periodic table. For example, a planet composed of hydrogen (H), oxygen (O), 
 and nitrogen (N), with a surface area of 100 thousand square miles, wouled be labeled as follows:

    HON_100

  You will receive a list that includes all the planets in a solar system, as well as an inclusive
 maximum size that a planet can be for human life. Your task is to identify the planet that possesses all 
 the essential elements for human life while being as large as possible. The required elements for human 
 life are: Hydrogen (H), Carbon (C), Nitrogen (N), Oxygen (O), Phosphorus (P), and Calcium (Ca). 
 These elements are represented as follows:

["H", "O", "N", "C", "P", "Ca"]

  If none of the planets meet the requirements, then return an empty string, "". 
Finally, multiple planets can contain all of the required elements; in this case, return the planet 
that is closest to the maximum possible size.

Example:

Your input is in the form of:

bestPlanet({"OHNCCaP_100", "OHC_200", "OCa_50", "OHCCaP_400", "OHNCCaP_225", "OHCa_250"}, 250)

You should return:

"OHNCCaP_225"
"""
print('*** Identify Best Planet ***')


REQUIRED_ELEMENTS = ['H', 'C', 'N', 'O', 'P', 'Ca']


def best_planet(solar_system, max_size):
    buf = []
    for i in solar_system:
        elem = re.findall('[A-Z][a-z]?', i.split('_')[0])
        size = int(i.split('_')[1])
        if all(item in elem for item in REQUIRED_ELEMENTS) and size <= max_size:
            buf.append((''.join(elem), size))
    if len(buf) == 0:
        return ''
    elif len(buf) == 1:
        return f'{buf[0][0]}_{buf[0][1]}'
    else:
        res = max(buf, key=lambda item: item[1])
        return f'{res[0]}_{res[1]}'


print(best_planet(
    ['PHNOCaC_212', 'RfInBeLaSgDs_188', 'PCaCNOAgHTsPu_304', 'NhFAlReNaSiCf_167',
     'OPClNCCaH_110', 'NdNaNhFAlNpTa_337', 'NAmUOCH_82'], 280))


"""
Unwanted dollars

If you're faced with an input box, like this:

                                           +--------------+
  Enter the price of the item, in dollars: |              |
                                           +--------------+

do you put the $ sign in, or not? Inevitably, some people will type a $ sign and others will leave it out. 
The instructions could be made clearer - but that won't help those annoying people who never read instructions anyway.

A better solution is to write code that can handle the input whether it includes a $ sign or not.

So, we need a simple function that converts a string representing a number (possibly with a $ sign in 
front of it) into the number itself.

Remember to consider negative numbers (the - sign may come either before or after the $ sign, if there is one), 
and any extraneous space characters (leading, trailing, or around the $ sign) that the users might put in. 
You do not need to handle input with trailing characters other than spaces (e.g. "1.2 3" or "1$"). 
If the given string does not represent a number, (either with or without a $ sign), return 0.0 .
"""
print('*** Unwanted dollars ***')


def money_value(s):
    m = s.replace(' ', '').replace('$', ''). replace(',', '.')
    try:
        return float(m)
    except ValueError:
        return 0.0


print(money_value("12.34"))
print(money_value(" $5.67"))
print(money_value("-0.89"))
print(money_value("-$ 0.1"))
print(money_value("$-2.3456"))
print(money_value("007"))
print(money_value(" $ 89"))
print(money_value("   .11"))
print(money_value("$.2"))
print(money_value("-.34"))
print(money_value("$$$"))
print(money_value("-"))

"""
UN-usual Sort

So, the unusualSort/unusual_sort function you'll have to code will sort letters as usual, 
but will put digits (or one-digit-long numbers ) after letters.
Examples

unusual_sort(["a","z","b"])  # -> ["a","b","z"]  as usual
unusual_sort(["a","Z","B"])  # -> ["B","Z","a"]  as usual

//... but ...
unusual_sort(["1","z","a"])  # -> ["a","z","1"]
unusual_sort(["1","Z","a"])  # -> ["Z","a","1"]
unusual_sort([3,2,1"a","z","b"])  # -> ["a","b","z",1,2,3]
unusual_sort([3,"2",1,"a","c","b"])  # -> ["a","b","c",1,"2",3]

Note: digits will be sorted after "same-digit-numbers", eg: 1 is before "1", "2" after 2.

unusual_sort([3,"2",1,"1","3",2])  # -> [1,"1",2,"2",3,"3"]

You may assume that argument will always be an array/list of characters or one-digit-long numbers.
"""

print('*** UN-usual Sort ***')


def unusual_sort(array):
    buffer_letters = []
    buffer_nums = []
    buffer_nums_string = []
    for i in array:
        if type(i) == int:
            buffer_nums.append(i)
        elif i.isalpha():
            buffer_letters.append(i)
        else:
            buffer_nums_string.append(i)
    buffer_letters.sort()
    buffer_nums.sort()
    buffer_nums_string.sort()
    buffer_all_nums = buffer_nums + buffer_nums_string
    buffer_all_nums.sort(key=int)
    return buffer_letters + buffer_all_nums


print(unusual_sort(["a","z","b"]))
print(unusual_sort(["a","Z","B"]))
print(unusual_sort(["1","z","a"]))
print(unusual_sort(["1","Z","a"]))
print(unusual_sort([3,2,1, "a","z","b"]))
print(unusual_sort([3,"2",1,"a","c","b"]))
print(unusual_sort([3,"2",1,"1","3",2]))
print(unusual_sort(['0', '9', '8', '1', '7', '2', '6', '3', '5', '4']))
print(unusual_sort(['3', '2', '1', 'c', 'b', 'a']))
print(unusual_sort(['x', '1', 'y', '2', 'z', '3']))
print(unusual_sort(['c', 'b', 'a', '9', '5', '0', 'X', 'Y', 'Z']))


"""
Two Sum

Write a function that takes an array of numbers (integers for the tests) and a target number. 
It should find two different items in the array that, when added together, give the target value. 
The indices of these items should then be returned in a tuple / list (depending on your language) 
like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the 
items will be numbers; target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/

two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]
"""

print('*** Two Sum ***')


def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]


print(two_sum([1, 2, 3], 4))
print(two_sum([1234,5678,9012], 14690))
print(two_sum([2,2,3], 4))


"""
Grouped by commas

Finish the solution so that it takes an input n (integer) and returns a string that is the 
decimal representation of the number grouped by commas after every 3 digits.

Assume: 0 <= n < 2147483647
Examples

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
"""

print('*** Grouped by commas ***')


def group_by_commas(n):
    return "{:,}".format(n)


print(group_by_commas(1))
print(group_by_commas(10))
print(group_by_commas(100))
print(group_by_commas(1000))
print(group_by_commas(10000))
print(group_by_commas(100000))
print(group_by_commas(1000000))
print(group_by_commas(35235235))


"""
Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, 
but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in 
will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
spinWords( "This is a test") => returns "This is a test" 
spinWords( "This is another test" )=> returns "This is rehtona test"
"""

print('*** Stop gninnipS My sdroW! ***')


def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) >= 5 else i for i in sentence.split(' ')])


print(spin_words('Hey fellow warriors'))
print(spin_words('This is a test'))
print(spin_words('This is another test'))
print(spin_words('This sentence is a sentence'))
print(spin_words('Welcome'))


"""
Count characters in your string

The main idea is to count all the occurring characters in a string. 
If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""

print('*** Count characters in your string ***')


def count(s):
    # return {i: s.count(i) for i in s}
    return dict(collections.Counter(s))


print(count('aba'))
print(count(''))


"""
Simple Fun #305: Typist

John is a typist. He has a habit of typing: he never use the Shift key to switch case, just using only Caps Lock.

Given a string s. Your task is to count how many times the keyboard has been tapped by John.

You can assume that, at the beginning the Caps Lock light is not lit.
Input/Output

[input] string s

A non-empty string. It contains only English letters(uppercase or lowercase).

1 ≤ s.length ≤ 10000

[output] an integer

The number of times John tapped the keyboard.
Example

For s = "a", the output should be 1.

John hit button a.

For s = "aa", the output should be 2.

John hit button a, a.

For s = "A", the output should be 2.

John hit button Caps Lock, A.

For s = "Aa", the output should be 4.

John hit button Caps Lock, A, Caps Lock, a.
"""

print('*** Simple Fun #305: Typist ***')


def typist(s):
    res = 0
    if len(s) == 1:
        if s.isupper():
            return 2
        else:
            return 1
    else:
        if s[0].islower():
            res += 1
        else:
            res += 2
    for i in range(1, len(s)):
        if (s[i].isupper() and s[i-1].isupper()) or (s[i].islower() and s[i-1].islower()):
            res += 1
        elif (s[i].isupper() and s[i-1].islower()) or (s[i].islower() and s[i-1].isupper()):
            res += 2
    return res


print(typist('a'))
print(typist('aa'))
print(typist('A'))
print(typist('AA'))
print(typist('aA'))
print(typist('Aa'))
print(typist('DFjfkdaB'))


"""
Dbftbs Djqifs

Your task is to create a function encryptor that takes 2 arguments - key and message - 
and returns the encrypted message.

Make sure to only shift letters, and be sure to keep the cases of the letters the same. 
All punctuation, numbers, spaces, and so on should remain the same.

Also be aware of keys greater than 26 and less than -26. There's only 26 letters in the alphabet!
Examples

A message 'Caesar Cipher' and a key of 1 returns 'Dbftbs Djqifs'.

A message 'Caesar Cipher' and a key of -1 returns 'Bzdrzq Bhogdq'.
"""

print('*** Dbftbs Djqifs ***')


def encryptor(key, message):
    lower_letters = list(string.ascii_lowercase)
    upper_letters = list(string.ascii_uppercase)
    res = ''
    for i in message:
        if i.isalpha():
            if i in lower_letters:
                res += lower_letters[(lower_letters.index(i) + key) % 26]
            elif i in upper_letters:
                res += upper_letters[(upper_letters.index(i) + key) % 26]
        else:
            res += i
    return res


print(encryptor(13, ''))
print(encryptor(13, 'Caesar Cipher'))
print(encryptor(-5, 'Hello World!'))
print(encryptor(27, 'Whoopi Goldberg'))
print(encryptor(-62, 'c'))


"""
Timer Decorator

Write a timer() decorator that validates if a function it decorates is executed within (less than) 
a given seconds interval and returns a boolean True or False accordingly.

Example:

from time import sleep

@timer(1)
def foo():
    sleep(0.1)
    
@timer(1)
def bar():
    sleep(1.1)


>>> foo()
True

>>> bar()
False
"""

print('*** Timer Decorator ***')


def timer(limit):
    def decor(func):
        def outer(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            stop = time.time() - start
            return limit > stop
        return outer
    return decor


@timer(1)
def foo():
    sleep(0.1)


@timer(1)
def bar():
    sleep(1.1)


print(foo())
print(bar())


"""
CamelCase Method

Write a method (or function, depending on the language) that converts a string to camelCase, 
that is, all words must have their first letter capitalized and spaces must be removed.
Examples (input --> output):

"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
"""

print('*** CamelCase Method ***')


def camel_case(s):
    return ''.join([i.capitalize() for i in s.split()])


print(camel_case('test case'))
print(camel_case('say hello '))


"""
Who likes it?

You probably know the "like" system from Facebook and other pages. People can "like" 
blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

print('*** Who likes it? ***')


def likes(names):
    if len(names) <= 1:
        tail = ' likes this'
    else:
        tail = ' like this'

    if len(names) == 0:
        head = 'no one'
    elif len(names) == 1:
        head = names[0]
    elif len(names) == 2:
        names.insert(-1, " and ")
        head = ''.join(names)
    elif len(names) == 3:
        names.insert(-1, " and ")
        names.insert(1, ', ')
        head = ''.join(names)
    else:
        n = len(names) - 2
        head = f'{names[0]}, {names[1]} and {n} others'
    return head + tail


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))


"""
What's A Name In?
Task

Write a function, taking two strings in parameter, that tests whether or not the first string contains all of the 
letters of the second string, in order.

The function should return true if that is the case, and else false. Letter comparison should be case-INsensitive.
Examples

    "Across the rivers", "chris" --> true
      ^      ^  ^^   ^
      c      h  ri   s
                
    Contains all of the letters in "chris", in order.
----------------------------------------------------------
    "Next to a lake", "chris" --> false

    Contains none of the letters in "chris".
--------------------------------------------------------------------
    "Under a sea", "chris" --> false
         ^   ^
         r   s

    Contains only some of the letters in "chris".
--------------------------------------------------------------------
    "A crew that boards the ship", "chris" --> false
       cr    h              s i
       cr                h  s i  
       c     h      r       s i
                 ...
          
    Contains all of the letters in "chris", but not in order.
--------------------------------------------------------------------
    "A live son", "Allison" --> false
     ^ ^^   ^^^
     A li   son
            
    Contains all of the correct letters in "Allison", in order, but not enough of all 
"""


def name_in_str(str, name):
    idx = -1
    for i in name.lower():
        idx = str.lower().find(i, idx+1)
        if idx == -1:
            return False
    return True


print(name_in_str("Across the rivers", "chris"))
print(name_in_str("Next to a lake", "chris"))
print(name_in_str("A live son", "Allison"))
print(name_in_str("A crew that boards the ship", "chris"))


"""
Kebabize

Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"

Notes:

    the returned string should only contain lowercase letters
"""

print('*** Kebabize ***')


def kebabize(st):
    l = ''.join([i for i in st if i.isalpha()])
    words = []
    for i in range(len(l)):
        if l[i].isupper():
            if i == 0:
                words.append(l[i].lower())
            else:
                words.append(':' + l[i].lower())
        else:
            words.append(l[i])
    words = ((''.join(words)).split(':'))
    return '-'.join(words)


print(kebabize('myCamelCasedString'))
print(kebabize('42'))
print(kebabize('SOS'))
print(kebabize('myCamelHas3Humps'))


"""
Find the odd int

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
Examples

[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

print('*** Find the odd int ***')


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it([7]))
print(find_it([0]))
print(find_it([1,1,2]))
print(find_it([0,1,0,1,0]))
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))


"""
Split Strings

Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing 
second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

print('*** Split Strings ***')


def solution(s):
    res = [s[i:i+2] for i in range(0, len(s), 2)]
    for i in range(len(res)):
        if len(res[i]) == 1:
            res[i] += '_'
    return res


print(solution("asdfadsf"))
print(solution("asdfads"))


"""
Simple Fun #15: Addition without Carrying

 A little boy is studying arithmetics. He has just learned how to add two integers, 
 written one below another, column by column. But he always forgets about the important part - carrying.

Given two integers, find the result which the little boy will get.
Example

For param1 = 456 and param2 = 1734, the output should be 1180

    456
   1734
+ ____
   1180

The little boy goes from right to left:

6 + 4 = 10 but the little boy forgets about 1 and just writes down 0 in the last column

5 + 3 = 8

4 + 7 = 11 but the little boy forgets about the leading 1 and just writes down 1 under 4 and 7.

There is no digit in the first number corresponding to the leading digit of the second one, 
so the little boy imagines that 0 is written before 456. Thus, he gets 0 + 1 = 1
"""

print('*** Simple Fun #15: Addition without Carrying ***')


def addition_without_carrying(a,b):
    str_a = str(a)
    str_b = str(b)
    if len(str_a) > len(str_b):
        diff = len(str_a) - len(str_b)
        str_b = '0' * diff + str_b
    elif len(str_a) < len(str_b):
        diff = len(str_b) - len(str_a)
        str_a = '0' * diff + str_a
    return int(''.join([str(int(x) + int(y))[-1] for x, y in zip(str_a, str_b)]))


print(addition_without_carrying(999,999))
print(addition_without_carrying(456,1734))
print(addition_without_carrying(99999,0))


"""
Calculate String Rotation

 Write a function that receives two strings and returns n, where n is equal to the number of 
 characters we should shift the first string forward to match the second. The check should be case sensitive.

For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been 
rotated 5 characters forward to produce the second string, so 5 would be returned.
If the second string isn't a valid rotation of the first string, the method returns -1.
Examples:

"coffee", "eecoff" => 2
"eecoff", "coffee" => 4
"moose", "Moose" => -1
"isn't", "'tisn" => 2
"Esham", "Esham" => 0
"dog", "god" => -1
"""

print('*** Calculate String Rotation ***')


def shifted_diff(first, second):
    if first == second: return 0
    for i in range(len(first)):
        res = first[i+1:] + first[:i+1]
        if res == second:
            return len(first[i+1:])
    return -1


print(shifted_diff("eecoff", "coffee"))
print(shifted_diff("Moose","moose"))
print(shifted_diff("isn't","'tisn"))


"""
Simple Fun #110: Array Operations

 You are given an array of integers a and a non-negative number of operations k, 
 applied to the array. Each operation consists of two parts:

find the maximum element value of the array;
replace each element a[i] with (maximum element value - a[i]).```
How will the array look like after `k` such operations?

# Example

 For `a = [-4, 0, -1, 0]` and `k = 2`, the output should be `[0, 4, 3, 4]`.

initial array: [-4, 0, -1, 0] 1st operation: find the maximum value --> 0 replace each element: --> 
[(0 - -4), (0 - 0), (0 - -1), (0 - 0)] --> [4, 0, 1, 0] 2nd operation: find the maximum value --> 
4 replace each element: --> [(4 - 4), (4 - 0), (4 - 1), (4 - 0)] --> [0, 4, 3, 4]

For `a = [0, -1, 0, 0, -1, -1, -1, -1, 1, -1]` and `k = 1`, 

the output should be `[1, 2, 1, 1, 2, 2, 2, 2, 0, 2]`.

initial array: [0, -1, 0, 0, -1, -1, -1, -1, 1, -1] 1st operation: find the maximum value --> 
1 replace each element: --> [(1-0),(1- -1),(1-0),(1-0),(1- -1),(1- -1),(1- -1),(1- -1),(1-1),(1- -1)] --> 
[1, 2, 1, 1, 2, 2, 2, 2, 0, 2]
"""

print('*** Simple Fun #110: Array Operations ***')


def array_operations(a, k):
    MAX = max(a)
    res = [MAX - i for i in a]
    for i in range((k-1)%2):
        MAX = max(res)
        res = [MAX - i for i in res]
    return res


print(array_operations([-4, 0, -1, 0],2))


"""
Are we alternate?

Create a function isAlt() that accepts a string as an argument and validates whether the vowels (a, e, i, o, u) 
and consonants are in alternate order.

is_alt("amazon")  # True
is_alt("apple")   # False
is_alt("banana")  # True
"""

print('*** Are we alternate? ***')


def is_alt(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    even = [value for idx, value in enumerate(s) if idx % 2 == 0]
    odd = [value for idx, value in enumerate(s) if idx % 2 != 0]
    return (all(i in vowels for i in even) and all(i not in vowels for i in odd)) or \
           (all(i in vowels for i in odd) and all(i not in vowels for i in even))


print(is_alt('amazon'))
print(is_alt('orange'))


"""
Highest Rank Number in an Array

Complete the method which returns the number which is most frequent in the given input array. 
If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3
"""


print('*** Highest Rank Number in an Array ***')


def highest_rank(arr):
    if len(arr) == len(set(arr)): return max(arr)
    return max(sorted(arr, reverse=True), key=arr.count)


print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))
print(highest_rank([1, 1, 2, 2, 3]))


"""
Sort Arrays (Ignoring Case)

["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]
"""

print('*** Sort Arrays (Ignoring Case) ***')


def sortme(words):
    return sorted(words, key=lambda x: x.lower())


print(sortme(["C", "d", "a", "B"]))


"""
Sort the odd

[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

print('*** Sort the odd ***')


def sort_array(source_array):
    odd = []
    res = []
    for i in source_array[:]:
        if i % 2 != 0:
            odd.append(i)
            res.append('odd')
        else:
            res.append(i)
    for i in sorted(odd):
        idx = res.index('odd')
        res[idx] = i

    return res


print(sort_array([5, 8, 6, 3, 4]))
print(sort_array([1, 3, 5, 11, 2, 8, 4]))


"""
Proof Read 

You've just finished writing the last chapter for your novel when a virus suddenly infects your document. 
It has swapped the 'i's and 'e's in 'ei' words and capitalised random letters. Write a function which will:

a) remove the spelling errors in 'ei' words. (Example of 'ei' words: their, caffeine, deceive, weight)

b) only capitalise the first letter of each sentence. Make sure the rest of the sentence is in lower case.

Example: He haD iEght ShOTs of CAffIEne. --> He had eight shots of caffeine.
"""


print('*** Proof Read ***')


def proofread(st):
    return '. '.join(list(map(lambda x: x.lower().replace('ie', 'ei').capitalize(), st.split('. '))))


print(proofread("THe neIghBour's ceiLing FEll on His Head. The WiEght of It crusHed him To thE gROuNd."))


"""
String array duplicates

For example:

    dup(["abracadabra","allottee","assessee"]) = ["abracadabra","alote","asese"].

    dup(["kelless","keenness"]) = ["keles","kenes"].
"""

print('*** String array duplicates ***')


def dup(arry):
    res = []
    for i in arry:
        s = ''
        previous = None
        for j in i:
            if j != previous:
                s += j
            previous = j
        res.append(s)
    return res


print(dup(["eklless","keenness"]))
print(dup(["abracadabra","allottee","assessee"]))


"""
Alphabetized

alphabetized("The Holy Bible") # "BbeehHilloTy"
"""

print('*** Alphabetized ***')


def alphabetized(s):
    letters = ''.join(sorted([i for i in s if i.isalpha()], key=lambda s: s.lower()))
    return letters


print(alphabetized("The Holy Bible"))
print(alphabetized(""))
print(alphabetized("CodeWars can't Load Today"))
print(alphabetized(" a"))
print(alphabetized("!@$%^&*()_+=-`,"))


"""
Organise duplicate numbers in list

group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
"""


print('*** Organise duplicate numbers in list ***')


def group(arr):
    lst = [[i]*arr.count(i) for i in arr]
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res


print(group([3, 2, 6, 2, 1, 3]))


"""
Compare Versions

compare_versions("11", "10");                    # returns True
compare_versions("11", "11");                    # returns True
compare_versions("10.4.6", "10.4");              # returns True
compare_versions("10.4", "11");                  # returns False
compare_versions("10.4", "10.10");               # returns False
compare_versions("10.4.9", "10.5");              # returns False
"""

print('*** Compare Versions ***')


def compare_versions(version1,version2):
    ver1 = [int(i) for i in version1.split('.')]
    ver2 = [int(i) for i in version2.split('.')]
    return ver1 >= ver2


print(compare_versions("11", "10"))
print(compare_versions("11", "11"))
print(compare_versions("10.4.6", "10.4"))
print(compare_versions("10.4", "11"))
print(compare_versions("10.4", "10.10"))


"""
More Zeros than Ones

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False
                   
        --> ['a','b','d']
    
'DIGEST'--> ['D','I','E','T']
"""

print('*** More Zeros than Ones ***')


def more_zeros(s):
    s = list(OrderedDict.fromkeys(s).keys())
    res = []
    for i in s:
        b = (bin(int.from_bytes(i.encode(), 'big')))[2:]
        if b.count('0') > b.count('1'):
            res.append(i)
    return res


print(more_zeros('abcde'))
print(more_zeros('thequickbrownfoxjumpsoverthelazydog'))
print(more_zeros('Forgiveness is the fragrance that the violet sheds on the heal that has crushed it'))
print(more_zeros('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'))


"""
Is Integer Array?

    returns true  / True if every element in an array is an integer or a float with no decimals.
    returns true  / True if array is empty.
    returns false / False for every other input.
"""

print('*** Is Integer Array? ***')


def is_int_array(arr):
    return isinstance(arr, list) and all(isinstance(i, (int, float)) and i == int(i) for i in arr)


print(is_int_array([]))
print(is_int_array([1, 2, 3, 4]))
print(is_int_array([1.2, 1.8, 3]))
print(is_int_array([1.0, 2.0, 3.0]))
print(is_int_array(None))
print(is_int_array(""))
print(is_int_array([1, 2, 3, None]))
print(is_int_array(["-1"]))
print(is_int_array([-11, -12, -13, -14]))


"""
Duplicate Arguments

Complete the solution so that it returns true if it contains any duplicate argument values. 
Any number of arguments may be passed into the function.

The array values passed in will only be strings or numbers. The only valid return values are true and false.

Examples:

solution(1, 2, 3)             -->  false
solution(1, 2, 3, 2)          -->  true
solution('1', '2', '3', '2')  -->  true
"""

print('*** Duplicate Arguments ***')


def duplicate_arguments(*args):
    for i in args:
        if args.count(i) > 1:
            return True
        else:
            continue
    return False


print(duplicate_arguments(1, 2, 3, 1, 2))
print(duplicate_arguments())
print(duplicate_arguments('a', 'b'))
print(duplicate_arguments('a', 'b', 'c', 'd', 'e', 'f', 'f', 'b'))
