def check_around(i, j, n, array):
    combination = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (-1, 1)]
    for x, y in combination:
        if i+x > n-1 or i+x < 0 or j+y > n-1 or j+y< 0:
            continue
        else:
            if is_prime(array[x+i][y+j]) == False: return 0
    return 1
