# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def not_matching(left, right):
    return (left + right) not in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    index_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            index_stack.append(i)

        if next in ")]}":
            # Process closing bracket, write your code here
            if opening_brackets_stack == []:
                return i + 1
            top = opening_brackets_stack.pop()
            top_index = index_stack.pop()
            #if (top == '(' and next != ')') or (top == '[' and next != ']') or (top == '{' and next != '}'):
            if not_matching(top, next):
                return i + 1

    if opening_brackets_stack == []:
        return 'Success'
    else:
        return index_stack[0] + 1



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
