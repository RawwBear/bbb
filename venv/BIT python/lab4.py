word = 'sdfafdsahfdsa'
count = {}
for letter in word:
    count[letter] = count.get(letter, 0) + 1
print(count)

try:
    while True:
        print('s')
except BaseException:
    exit(1)