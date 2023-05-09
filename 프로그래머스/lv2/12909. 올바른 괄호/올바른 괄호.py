def solution(s):
    answer = True
    stack = []
    for a in s:
        if a == '(':
            stack.append(a)
        elif a== ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return True if len(stack) == 0 else False