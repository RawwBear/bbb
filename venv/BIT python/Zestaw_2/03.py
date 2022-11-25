def next_words_fib(d):
    #golden ratio = F(n)/F(n-1)
    f1, f2 = 1, 1
    last = 0 #contains last przyblizenie of golden ratio
    while abs(f2 / f1 - last) > 0.1**d:
        last = f2 / f1
        f1, f2 = f2, f1 + f2
    return f2/f1

print(next_words_fib(4))