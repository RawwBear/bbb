def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            a, b = b, a
    return a

def nwd_2(a, b):#faster way to
    while b != 0:
        a, b = b, a % b
    return a

def nww(a, b):
    return a*b/nwd(a, b)

if __name__ == '__main__':
    print(nwd(57, 18))
    print(nwd_2(18, 57))
    print(nww(16, 18))
    print(16*9)