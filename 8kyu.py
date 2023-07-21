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
Array plus array

I'm new to coding and now I want to get the sum of two arrays...
Actually the sum of all their elements. I'll appreciate for your help.

P.S. Each array includes only integer numbers. Output is a number too.
"""
print('*** Array plus array ***')


def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


print(array_plus_array([1, 2, 3], [4, 5, 6]))
print(array_plus_array([-1, -2, -3], [-4, -5, -6]))


"""
Reversed sequence

Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]
"""
print('*** Reversed sequence ***')


def reverse_seq(n):
    lst = []
    for i in range(n, 0, -1):
        lst.append(i)
    return lst


print(reverse_seq(5))


"""
What is between?

Complete the function that takes two integers (a, b, where a < b) and return an array of 
all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]


"""
print('*** What is between? ***')


def between(a, b):
    lst = []
    for i in range(a, b+1):
        lst.append(i)
    return lst


print(between(1, 4))


"""
Add Length

What if we need the length of the words separated by a space to be added at the 
end of that same word and have it returned as an array?

Example(Input --> Output)

"apple ban" --> ["apple 5", "ban 3"]
"you will win" -->["you 3", "will 4", "win 3"]

Your task is to write a function that takes a String and returns an Array/list 
with the length of each word added to each element .

Note: String will have at least one element; words will always be separated by a space.

"""
print('*** Add Length ***')


def add_length(str_):
    lst = str_.split(' ')
    new_arr = [f'{i} {str(len(i))}' for i in lst]
    return new_arr


print(add_length('apple ban'))


"""
Find the position!

When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

"""
print('*** Find the position! ***')


def position(alphabet):
    pos = ord(alphabet) - 96
    return f'Position of alphabet: {pos}'


print(position('a'))
print(position('b'))
print(position('z'))


"""
A Needle in the Haystack

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
"""
print('*** A Needle in the Haystack ***')


def find_needle(haystack):
    idx = haystack.index('needle')
    return f'found the needle at position {idx}'


print(find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] ))


"""
Sentence Smash

Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. 
You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
Example

['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
"""

print('*** Sentence Smash ***')


def smash(words):
    return ' '.join(words)

print(smash(['hello', 'world', 'this', 'is', 'great']))


"""
L1: Set Alarm
Write a function named setAlarm/set_alarm/set-alarm/setalarm (depending on language) which receives two parameters. 
The first parameter, employed, is true whenever you are employed and the second parameter, vacation 
is true whenever you are on vacation.

The function should return true if you are employed and not on vacation (because these are the circumstances 
under which you need to set an alarm). It should return false otherwise. Examples:

employed | vacation 
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false
"""

print('*** L1: Set Alarm ***')


def set_alarm(employed, vacation):
    return employed and not vacation


print(set_alarm(True, True))
print(set_alarm(True, False))
print(set_alarm(False, True))
print(set_alarm(False, False))


"""
Short Long Short

Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. The strings will not be the same 
length, but they may be empty ( zero length ).

Hint for R users:

    The length of string is not always the same as the number of characters

For example: (Input1, Input2) --> output

("1", "22") --> "1221"
("22", "1") --> "1221"
"""

print('*** Short Long Short ***')


def solution(a, b):
    if len(a) > len(b):
        return f'{b}{a}{b}'
    else:
        return f'{a}{b}{a}'


print(solution("1", "22"))
print(solution("22", "1"))
print(solution('13', '200'))
print(solution('Soon', 'Me'))


"""
No zeros for heros

Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450 -> 145
960000 -> 96
1050 -> 105
-1050 -> -105
"""
print('*** No zeros for heros ***')


def no_boring_zeros(n):
    if n == 0:
        return n
    while n % 10 == 0:
        n /= 10
    return int(n)
    # n = list(str(n))
    # if len(n) == 1:
    #     return int(n[0])
    # else:
    #     for i in reversed(n):
    #         if i == '0':
    #             del n[-1]
    #         else:
    #             break
    #     return int(''.join(n))


print(no_boring_zeros(14500))
print(no_boring_zeros(1050))
print(no_boring_zeros(0))
print(no_boring_zeros(2016))


"""
Will there be enough space?

Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough 
space left on the bus! He wants you to write a simple program telling him if he will be able to fit all the passengers.
Task Overview:

You have to write a function that accepts three parameters:

    cap is the amount of people the bus can hold excluding the driver.
    on is the number of people on the bus excluding the driver.
    wait is the number of people waiting to get on to the bus excluding the driver.

If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
Usage Examples:

cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting
"""

print('*** Will there be enough space? ***')


def enough(cap, on, wait):
    if on + wait <= cap:
        return 0
    else:
        return abs(cap - (on + wait))


print(enough(10, 5, 5))
print(enough(100, 60, 50))
print(enough(20, 5, 5))


"""
Draw stairs

Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.

For example n = 3 result in:

"I\n I\n  I"

or printed:

I
 I
  I
"""

print('*** Draw stairs ***')


def draw_stairs(n):
    return '\n'.join((' '*i) + 'I' for i in range(n))


print(draw_stairs(3))
print(draw_stairs(7))
