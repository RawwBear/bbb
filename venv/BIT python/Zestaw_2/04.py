def in_sorted_tab(tab, num):
    for i in sorted(tab):
        if i == num: return True
    return False

print(in_sorted_tab([2, 3, 77, 1, 12], 13))

#przerob funkcje na czas logN - metoda bisekcji :)
def binary_search(tab, num):
    left, right = tab[0], tab[-1]
    mid = (left + right)//2
    #need to move out of the while
    while tab[mid] != num:
        if tab[mid] > num:
            right = mid
        elif tab[mid] <  num:
            left = mid
        else:
            return True
        mid = (left + right)//2
    return False

print(binary_search([i for i in range(10)],9))