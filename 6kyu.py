import string
import re

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
    # sys.set_int_max_str_digits(int(2.5E6))

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
