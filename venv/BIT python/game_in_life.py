def check_around(x,y):
    combination = [(1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (-1, 1)]
    #lista combination zawiera możliwe przesunięcia o wektor dla wybranego punktu poczatkowego, w ten sposób możliwe
    #jest sprawdzenie otaczających wybrany punkt sasiadow
    suma = 0
    for twx,twy in combination:
        #sprawdzamy czy sąsiedzi są żywi czy martwi
        komx = twx + x
        komy = twy + y
        if komx > len(tab[0])- 1:
            #przesuniecia prawo/lewo
            #jeśli nasz punkt sąsiaduje z koncem planszy to komórką sąsiednią będzie komórka
            #z drugiego końca planszy czyli współrzędna x sąsiada będzie wynosić 0
            komx = 0
        elif komy > len(tab) - 1:
            #przesuniecia góra/dół
            komy  = 0

        if tab[komy][komx] == 'X':
            suma += 1
    if tab[y][x] == 'X':
        #sprawdzam czy moja komórka jest żywa czy martwa
        if suma == 2 or suma == 3:
            return True
    else:
        if suma == 3:
            return True


def new_generation(tab): #tworze na podstawie poprzedniego pokolenia, czyli tab
    for i in tab:
        for j in range(len(i)):
            if check_around(tab[i][j]) == True:
                i[j] = 'X'
            else:
                i[j] = '.'
    return tab


with open('2016_pr_maj_5.1.txt', 'w')as odp:
    with open('gra.txt', 'r')as file:
        lines = file.readlines()
        tab = []
        for line in lines:
            line = line.strip()
            tab.append(list(line))
            #pierwszy wiersz naszej listy składa się z znaków które tworzą listę wewnętrzna
        print(new_generation(tab))
        # for i in tab:
        #     print(i)