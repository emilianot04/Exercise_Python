"""
There are numerous phrases that are palindromes when spacing is ignored. Examples include “go dog”, “flee to me remote elf” and “some men interpret nine memos”, among many others. Extend your solution to Exercise 75 so that it ignores spacing while determining whether or not a string is a palindrome. For an additional challenge, further extend your solution so that is also ignores punctuation marks and treats uppercase and lowercase letters as equivalent.
"""

from string import digits

phrases = input('Insert phrases:')

palindrome = ''

# only for python 3
new_phrases= str.maketrans('', '', digits)
newstring = phrases.translate(new_phrases)

phrases_no_space = newstring.replace(" ", "")

palindrome = phrases_no_space[::-1]
if (phrases_no_space == palindrome):
    print( 'The phrases', newstring, 'is palindrome')
else:
    print( 'The phrases', newstring, 'is not palindrome')