def reverse_number(number: int) -> int:
    is_signed = False
    if number < 0:
        is_signed = True
    str_num = str(number)
    r_str_num = reversed(str_num)
    num = ''.join(r_str_num)
    k = int(num.strip('-'))
    if is_signed:
        return 0 - k
    return k 


def r_number(number: int):
    result = ''
    while number:
        r = number % 10
        result += str(r)
    return int(result)


print(reverse_number(-1239488498394893842))
