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
