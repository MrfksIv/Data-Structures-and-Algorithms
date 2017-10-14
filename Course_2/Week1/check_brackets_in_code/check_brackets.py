# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

def check(text):
    opening_brackets_stack = []
    last_opening_bracket = None
    for i, next_char in enumerate(text):

        # first handle the case where an opening bracket is present
        if next_char == '(' or next_char == '[' or next_char == '{':
            opening_brackets_stack.append(Bracket(next_char,i))
            # print('stack: {}'.format(opening_brackets_stack))
            # check the case that the the last character is an opening bracket
            if (i == len(text) - 2):
                return i + 1
        
        # check the case that the first character is an closing bracket:
        if (next_char == ')' or next_char == ']' or next_char == '}') and i == 0:
            return i + 1
        
        if next_char == ')' or next_char == ']' or next_char == '}':
            # print('FOUND CLOSING PAREN AT {}'.format(i+1))
            if len(opening_brackets_stack) == 0:
                # print('NO OPENING BRACKETS LEFT!')
                return i + 1
            last_opening_bracket = opening_brackets_stack.pop()
            # print('LAST OPENING BRACKET: {}'.format(last_opening_bracket.bracket_type))
            if (last_opening_bracket.bracket_type == '(' and next_char != ')') or (last_opening_bracket.bracket_type == '[' and next_char != ']') or (last_opening_bracket.bracket_type == '{' and next_char != '}'):
                return i + 1

    if len(opening_brackets_stack) == 0:
        # print('REACHED THE LAST IF')
        return 'Success'
    else:
        # print('REACHED THE LAST ELSE')
        return last_opening_bracket.position

if __name__ == "__main__":
    text = sys.stdin.read()
    result = check(text)
    print(result)
    # for i, next in enumerate(text):
    #     if next == '(' or next == '[' or next == '{':
    #         # Process opening bracket, write your code here
    #         pass

    #     if next == ')' or next == ']' or next == '}':
    #         # Process closing bracket, write your code here
    #         pass

    # Printing answer, write your code here
