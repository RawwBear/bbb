def is_palindrome(w):
    w = w.lower().replace(' ', '')
    i = 0
    while i < len(w)//2:
        if w[i] != w[-i - 1]:
            return False
        i += 1
    return True

if __name__ == '__main__':
    print(is_palindrome('Marzena pokazala Zakopane z ram'))