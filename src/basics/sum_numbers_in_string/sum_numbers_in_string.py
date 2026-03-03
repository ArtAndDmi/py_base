import re

def sum_numbers_in_string(input_string: str) -> int:
    num = ''
    num_list = []
    for c in input_string:
        if c.isdigit():
            num += c
        else:
            if num.isdigit():
                num_list.append(int(num))
            num = ''

    if num.isdigit():
        num_list.append(int(num))

    return sum(num_list)


def sum_numbers_in_string_regex(input_string: str) -> int:
    return sum([int(x) for x in re.findall(r'\d+(?=\.)', input_string)])


