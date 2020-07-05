def swap_case(s):
    empty_list=[]
    for char in s:
        if char.isupper():
            empty_list.append(char.lower())
        else:
            empty_list.append(char.upper())
    return (''.join(empty_list))


if __name__ == '__main__':
