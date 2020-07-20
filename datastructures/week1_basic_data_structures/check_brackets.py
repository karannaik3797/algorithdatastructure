# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    if text =='':
        return"Success"
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            B = Bracket(next,i)
            opening_brackets_stack.append(B)
        if next in ")]}":
            if opening_brackets_stack == []:
                return i+1
            else:
                S = opening_brackets_stack.pop()
                if not (are_matching(S.char,next)):
                    return i+1
    if opening_brackets_stack==[]:
        return"Success"
    else:
        S = opening_brackets_stack.pop()
        return (S.position +1)
    
def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
