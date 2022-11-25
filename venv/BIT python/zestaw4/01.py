import re
text = "Sed ut libero dignissim, finibus urna in, varius odio. Suspendisse tristique et felis quis fringilla. In mattis " \
       "facilisis accumsan. In lectus augue, cursus sit amet ante quis, mattis laoreet diam. Sed scelerisque ut nulla " \
       "non iaculis. Suspendisse potenti. Aenean molestie erat eu commodo scelerisque. Morbi rutrum ut est eget semper. " \
       "Integer euismod porta euismod. Sed volutpat, magna quis convallis luctus, tortor ante facilisis tortor, " \
       "eu ultrices massa lorem nec orci. Suspendisse egestas maximus erat quis viverra. Curabitur egestas fermentum " \
       "turpis, in porta eros molestie vitae. Nunc congue magna risus, in efficitur mi posuere a. Duis vel libero ut " \
       "justo pulvinar facilisis et sed ex."

count = {}
new_text = text.lower().replace(',',' ')
# for word in new_text:
#     count[word] = count.get(word,0) + 1
# print(count)