import re
import random
from collections import OrderedDict

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


"""
Removing Elements

Take an array and remove every second element from the array. 
Always keep the first element and start removing with the next element.
Example:

["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!
"""

print('*** Removing Elements ***')


def remove_every_other(my_list):
    lst = []
    for i in range(0, len(my_list), 2):
        lst.append(my_list[i])
    return lst


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(remove_every_other([[1, 2]]))


"""
Remove duplicates from list

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.

The order of the sequence has to stay the same.

Examples:

Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]
"""

print('*** Remove duplicates from list ***')


def distinct(seq):
    return list(OrderedDict.fromkeys(seq).keys())


print(distinct([1, 1, 1, 2, 3, 4, 5]))


"""
Remove First and Last Character Part Two

You are given a string containing a sequence of character sequences separated by commas.

Write a function which returns a new string containing the same character 
sequences except the first and the last ones but this time separated by spaces.

If the input string is empty or the removal of the first and last items would cause 
the resulting string to be empty, return an empty value (represented as a generic value NULL in the examples below).
Examples

"1,2,3"      =>  "2"
"1,2,3,4"    =>  "2 3"
"1,2,3,4,5"  =>  "2 3 4"

""     =>  NULL
"1"    =>  NULL
"1,2"  =>  NULL
"""

print('*** Remove First and Last Character Part Two ***')


def array(string):
    return ' '.join(string.split(',')[1:-1]) or None


print(array('1,2,3'))
print(array('1,2,3,4'))
print(array(''))
print(array('1,2'))
print(array('1'))


"""
Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
Examples (Input -> Output):

* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""

print('*** Double Char ***')


def double_char(s):
    return ''.join([i*2 for i in s])


print(double_char('Hello World'))


"""
Counting sheep...

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example,

[true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true]

The correct answer would be 17.
"""


def count_sheeps(sheep):
    return sheep.count(True)


print(count_sheeps([True, True, False, True, True, False, True, False]))


"""
Flick Switch

Task

Create a function that always returns True for every item in a given list. 
However, if an element is the word "flick", switch to always returning the opposite boolean value.
Examples

["codewars", "flick", "code", "wars"] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞[False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
"""


def flick_switch(lst):
    l = []
    flag = True
    for i in lst:
        if i == 'flick':
            if flag is True:
                flag = False
            else:
                flag = True
            l.append(flag)
        else:
            l.append(flag)
    return l


print(flick_switch(["codewars", "flick", "code", "wars"]))
print(flick_switch(['flick', 'chocolate', 'adventure', 'sunshine']))


"""
get ascii value of character

Get ASCII value of a character.
"""

print('*** get ascii value of character ***')


def get_ascii(ch: str) -> int:
    return ord(ch)


"""
Fake Binary
"""

print('*** Fake Binary ***')


def fake_bin(x):
    return ''.join('0' if int(i) < 5 else '1' for i in x)


print(fake_bin("45385593107843568"))


"""
To square(root) or not to square(root)

Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.
Example

[4,3,9,7,2,1] -> [2,9,3,49,4,1]
"""

print('*** To square(root) or not to square(root) ***')


def square_or_square_root(arr):
    res = []
    for i in arr:
        x = i ** 0.5
        if x.is_integer():
            res.append(int(x))
        else:
            res.append(i ** 2)
    return res


print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))


"""
Is it a number?

isDigit("3")
isDigit("  3  ")
isDigit("-3.23")

should return false:

isDigit("3-4")
isDigit("  3   5")
isDigit("3 5")
isDigit("zero")
"""

print('*** Is it a number? ***')


def is_digit(s):
    try:
        float(s.strip())
        return True
    except:
        return False


print(is_digit('3'))
print(is_digit('  3  '))
print(is_digit('-3.23'))
print(is_digit('3-4'))
print(is_digit(' 3  5'))


"""
Simple validation of a username with regex
Write a simple regex to validate a username. Allowed characters are:

    lowercase letters,
    numbers,
    underscore

Length should be between 4 and 16 characters (both included).
"""

print('*** Simple validation of a username with regex ***')


def validate_usr(username):
    return re.match(r'^[a-z0-9_]{4,16}$', username) is not None


print(validate_usr('asddsa'))
print(validate_usr('Hass'))



"""
OOP: Object Oriented Piracy 


You are a leader of a small pirate crew. And you have a plan. With the help of OOP you wish to make a 
pretty efficient system to identify ships with heavy booty on board!

Unfortunately for you, people weigh a lot these days, so how do you know if a ship is full of gold and not people?

You begin with writing a generic Ship class / struct:

class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

Every time your spies see a new ship enter the dock, they will create a new ship object based on their observations:

    draft - an estimate of the ship's weight based on how low it is in the water
    crew - the count of crew on board

Titanic = Ship(15, 10)

Task

You have access to the ship "draft" and "crew". "Draft" is the total ship weight and "crew" 
is the number of humans on the ship.

Each crew member adds 1.5 units to the ship draft. If after removing the weight of the crew, 
the draft is still more than 20, then the ship is worth looting. Any ship weighing that much must have a lot of booty!

Add the method

is_worth_it

to decide if the ship is worthy to loot. For example:

Titanic.is_worth_it()
False
"""

print('*** OOP: Object Oriented Piracy  ***')


class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft - (self.crew * 1.5) > 20


worthy_ship = Ship(100,20)
print(worthy_ship.is_worth_it())


"""
Finish Guess the Number Game

Imagine you are creating a game where the user has to guess the correct number. 
But there is a limit of how many guesses the user can do.

    If the user tries to guess more than the limit, the function should throw an error.
    If the user guess is right it should return true.
    If the user guess is wrong it should return false and lose a life.

Can you finish the game so all the rules are met?
"""

print('*** Finish Guess the Number Game ***')


class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives > 0:
            if n == self.number:
                return True
            else:
                self.lives -= 1
                return False
        else:
            raise("Omae wa mo shindeiru")


guesser = Guesser(10, 2)
print(guesser.guess(1))
print(guesser.guess(2))

guesser_2 = Guesser(10, 2)
print(guesser.guess(10))
print(guesser.guess(10))


"""
Color Ghost

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" 
when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"
"""


print('*** Color Ghost ***')


class Ghost(object):
    COLORS = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = random.choice(Ghost.COLORS)


ghosts = [Ghost().color for _ in range(100)]
print(ghosts)


"""
Invert values

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
"""

print('*** Invert values ***')


def invert(lst):
    return [-i for i in lst]


print(invert([1,-2,3,-4,5]))


"""
Sum without highest and lowest number

Sum all the numbers of a given array ( cq. list ), except the highest and the 
lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if 
there are more than one with the same value.

Mind the input validation.
Example

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
"""

print('*** Sum without highest and lowest number ***')


def sum_array(arr):
    if arr is None or len(arr) < 2: return 0
    return sum((sorted(arr))[1:-1])


print(sum_array([6, 2, 1, 8, 10]))
