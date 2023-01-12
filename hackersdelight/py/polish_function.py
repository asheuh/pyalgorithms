import re

def polish_function(expression):
    expression = re.sub(r'\s+', '', expression)
    maps = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    stack = []
    error = ''
    for item in expression:
        try:
            if item == ')':
                prev = stack.pop()
                res = None
                op = ''
                while prev != '(':
                    if prev in maps and res is not None:
                        op = prev
                    elif res is None:
                        parsed = prev
                        while parsed:
                            # we handle cases where we a 5 * 234. Without this 5 * 2 will be evaluated
                            prev = stack.pop()
                            if prev not in maps and prev not in '()':
                                parsed = prev + parsed
                            else:
                                stack.append(prev)
                                break
                        res = int(parsed) 
                    else:
                        res = maps[op](int(prev), res)
                    prev = stack.pop()
                stack.append(res)
            else:
                stack.append(item)
        except ZeroDivisionError:
            error = 'Cannot divide by zero value.'

        except Exception as e:
            stack.append(item)
    if error:
        return error
    return stack[0]

if __name__ == '__main__':
    expression = '((((5 + 15) * 6 * 7) * 2) / (9 - 2))'
    result = polish_function(expression)
    print(result)

