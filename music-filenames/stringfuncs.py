# Useful string manipulation functions
import string

SPECIALCHARS = "!\"/\\£$%^&*(){}[]@#?=+|"

def removeAreasWithParentheses(my_str):
    first = my_str.find('(')
    last = my_str.find(')')

    if first > last:
        raise Exception("closing parenthesis before opener")

    if my_str.find('(', first + 1) < last:
        # there is a nested parenthesis
        # recursive call to function
        substr = removeAreasWithParenthesis(my_str[ first+1 : last ])

        my_str = my_str[0:first] + substr + my_str[last:]


    new_str = my_str[0:first] + my_str[last:]
    return new_str


def removeSpecialChars(my_str):
    for letter in my_str:
        if letter in list(SPECIALCHARS):
            pos = my_str.find(letter)
            my_str = my_str[0:pos] + my_str[(pos+1):]

    return my_str


def checkFileFormat(my_str):

    full_stop_present = False
    for letter in my_str:
        if letter == '.':
            full_stop_present = True


    specialchars_present = False
    for letter in my_str:
        if letter in list(SPECIALCHARS):
            specialchars_present = True


    if full_stop_present and (not specialchars_present):
        return True
    else:
        return False
