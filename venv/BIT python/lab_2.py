def foo(a=10):
    return a

if __name__ == '__main__':
    A = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(10):
        print(A[i])

    A = [1, 2, 3]
    a, b, c = A
    print(a, b, c)

    B = foo(5)
    print(foo())#print function with default variable
