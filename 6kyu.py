import string
import re
import collections
import sys
from time import sleep
import time

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
