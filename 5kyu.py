import re
import itertools

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
Human Readable Time

Write a function, which takes a non-negative integer (seconds) as input and returns 
the time in a human-readable format (HH:MM:SS)

    HH = hours, padded to 2 digits, range: 00 - 99
    MM = minutes, padded to 2 digits, range: 00 - 59
    SS = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""
print('*** Human Readable Time ***')


def make_readable(seconds):
    # m, s = divmod(seconds, 60)
    # h, m = divmod(m, 60)
    # return f'{h:02d}:{m:02d}:{s:02d}'
    hours = int(seconds / 3600)
    mins = int(seconds / 60 % 60)
    secs = int(seconds % 60)
    return f'{hours:02d}:{mins:02d}:{secs:02d}'


print(make_readable(0))
print(make_readable(5))
print(make_readable(11))
print(make_readable(60))
print(make_readable(125))
print(make_readable(86399))
print(make_readable(359999))


"""
Last digit of a large number

Define a function that takes in two non-negative integers aaa and bbb and 
returns the last decimal digit of aba^bab. Note that aaa and bbb may be very large!

For example, the last decimal digit of 979^797 is 999, since 97=47829699^7 = 478296997=4782969. 
The last decimal digit of (2200)2300({2^{200}})^{2^{300}}(2200)2300, 
which has over 109210^{92}1092 decimal digits, is 666. Also, please take 000^000 to be 111.

You may assume that the input will always be valid.
Examples

last_digit(4, 1)                # returns 4
last_digit(4, 2)                # returns 6
last_digit(9, 7)                # returns 9
last_digit(10, 10 ** 10)        # returns 0
last_digit(2 ** 200, 2 ** 300)  # returns 6

"""
print('*** Last digit of a large number ***')


def last_digit(n1, n2):
    return pow(n1, n2, 10)


print(last_digit(4, 1))
print(last_digit(4, 2))
print(last_digit(9, 7))
print(last_digit(10, 10 ** 10))
print(last_digit(2 ** 200, 2 ** 300))


"""
Lazy Repeater

The makeLooper() function (or make_looper in your language) takes a string (of non-zero length) as an argument. 
It returns a function. The function it returns will return successive characters of the string on successive 
invocations. It will start back at the beginning of the string once it reaches the end.

For example:

abc = make_looper('abc')
abc() # should return 'a' on this first call
abc() # should return 'b' on this second call
abc() # should return 'c' on this third call
abc() # should return 'a' again on this fourth call

"""

print('*** Lazy Repeater ***')


def make_looper(string):
    a = itertools.cycle(list(string))
    return lambda: next(a)


abc = make_looper("abc")
print(abc())
print(abc())
print(abc())
print(abc())


"""
String incrementer

Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
"""


print('*** String incrementer ***')


def increment_string(strng):
    letters = strng.rstrip('0123456789')
    nums = strng[len(letters):]
    if nums == '':
        return strng + '1'
    return letters + str(("%0"+"%dd" % len(nums)) % (int(nums) + 1))


print(increment_string('foo'))
print(increment_string('foobar001'))
print(increment_string('foobar1'))
print(increment_string('foobar00'))
print(increment_string('foobar99'))
print(increment_string('foobar099'))
print(increment_string('fo99obar99'))
print(increment_string(''))
print(increment_string('foobar00999'))


"""
Not very secure

In this example you have to validate if a user input string is alphanumeric. 
The given string is not nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

    At least one character ("" is not valid)
    Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
    No whitespaces / underscore
"""

print('*** Not very secure ***')


def alphanumeric(password):
    regexp = r'^[a-zA-Z0-9]+$'
    return True if re.match(regexp, password) else False


print(alphanumeric('hello world_'))
print(alphanumeric('PassW0rd'))
print(alphanumeric('    '))
print(alphanumeric('Y'))
print(alphanumeric('lnmcv`oXqaLn1afd87Gc'))
print(alphanumeric('|xdil7Oegh'))


"""
All Star Code Challenge #19

This Kata is intended as a small challenge for my students

All Star Code Challenge #19

You work for an ad agency and your boss, Bob, loves a catchy slogan. 
He's always jumbling together "buzz" words until he gets one he likes. 
You're looking to impress Boss Bob with a function that can do his job for him.

Create a function called sloganMaker() that accepts an array of string "buzz" words. 
The function returns an array of all possible UNIQUE string permutations of the 
buzz words (concatonated and separated by spaces).

Your boss is not very bright, so anticipate him using the same "buzz" word more than once, 
by accident. The function should ignore these duplicate string inputs.

sloganMaker(["super", "hot", "guacamole"]);
//[ 'super hot guacamole',
//  'super guacamole hot',
//  'hot super guacamole',
//  'hot guacamole super',
//  'guacamole super hot',
//  'guacamole hot super' ]

sloganMaker(["cool", "pizza", "cool"]); // => [ 'cool pizza', 'pizza cool' ]
"""

print('*** All Star Code Challenge #19 ***')


def slogan_maker(array):
    return list(map(' '.join, itertools.permutations(list(dict.fromkeys(array)))))


print(slogan_maker(["super", "hot", "guacamole"]))
print(slogan_maker(["super", "guacamole", "super", "super", "hot", "guacamole"]))


"""
Pick peaks

In this kata, you will write a function that returns the positions and the values of the "peaks" 
(or local maxima) of a numeric array.

For example, the array arr = [0, 1, 2, 5, 1, 0] has a peak at position 3 with a value of 5 (since arr[3] equals 5).

The output will be returned as an object with two properties: pos and peaks. Both of these 
properties should be arrays. If there is no peak in the given array, then the output should be {pos: [], peaks: []}.

Example: pickPeaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 3]) should return {pos: [3, 7], 
peaks: [6, 3]} (or equivalent in other languages)

All input arrays will be valid integer arrays (although it could still be empty), 
so you won't need to validate the input.

The first and last elements of the array will not be considered as peaks (in the context of a 
mathematical function, we don't know what is after and before and therefore, we don't know if it is a peak or not).

Also, beware of plateaus !!! [1, 2, 2, 2, 1] has a peak while [1, 2, 2, 2, 3] and [1, 2, 2, 2, 2] do not. 
In case of a plateau-peak, please only return the position and value of the beginning of the plateau. 
For example: pickPeaks([1, 2, 2, 2, 1]) returns {pos: [1], peaks: [2]} (or equivalent in other languages)
"""

print('*** Pick peaks ***')


def pick_peaks(arr):
    res = {'pos': [], 'peaks': []}
    for i in range(1, len(arr)-1):
        if arr[i] > arr[i-1]:
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    res['pos'].append(i)
                    res['peaks'].append(arr[i])
                    break
                elif arr[i] == arr[j]:
                    continue
                else:
                    break
    return res


print(pick_peaks([1,2,3,6,4,1,2,3,2,1]))
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,3]))
print(pick_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]))
print(pick_peaks([2,1,3,1,2,2,2,2,1]))
print(pick_peaks([2,1,3,1,2,2,2,2]))
print(pick_peaks([1,1,1,1]))


"""
Moving Zeros To The End

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""

print('*** Moving Zeros To The End ***')


def move_zeros(lst):
    zeros = lst.count(0)
    res = [i for i in lst if i != 0]
    res.extend([0]*zeros)
    return res


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))


"""
First non-repeating character

Write a function named first_non_repeating_letter† that takes a string input, and returns the 
first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't', since the letter t only occurs once 
in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same character, but the function should 
return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.

If a string contains all repeating characters, it should return an empty string ("");

† Note: the function is called firstNonRepeatingLetter for historical reasons, but your function 
should handle any Unicode character.
"""

print('*** First non-repeating character ***')


def first_non_repeating_letter(s):
    for i in s:
        if s.lower().count(i.lower()) == 1:
            return i
    return ""


print(first_non_repeating_letter('sTress'))
