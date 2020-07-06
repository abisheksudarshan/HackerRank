if __name__ == '__main__':
    s = input()
    isalnum=False
    alpha=False
    digits=False
    lower=False
    upper=False

    for i in range(len(s)):
        if s[i].isdigit()==True:
            digits=True
            isalnum=True
        if s[i].islower()==True:
            lower=True
            alpha=True
            isalnum=True
        if s[i].isupper()==True:
            upper=True
            alpha=True
            isalnum=True

    print(isalnum)
    print(alpha)
    print(digits)
    print(lower)
    print(upper)
