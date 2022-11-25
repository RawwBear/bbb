a = [i**2 for i in range(20)]
print(a)

#zad4
imie = ['adam', 'karol', 'monika', 'kasia', 'maciek']
wiek = [13, 19, 45, 7, 55]
zipped = sorted(list(zip(imie, wiek))) #create sorted list filled with tupels (name, age)

index = 0
while zipped[index][1] < 18:
    index += 1

res = [zipped[i][0] for i in range(index, len(zipped))]
print(res)

#zad7
a = [i for i in range(7)]
b = [i for i in range(3,15,3)]
print(a, b)
c = []
i, j = 0, 0
while i < len(a.extend(b)):
    # if a[i] < b[j]:

    # Driver code
    if __name__ == '__main__':
        num = 50
        sieve_of_eratosthenes(num)