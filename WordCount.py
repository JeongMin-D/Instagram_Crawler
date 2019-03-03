import re
import string
import csv

f = open('test2.csv', 'r', encoding='utf-8-sig',  newline='')
title = f.read()
f.close()

title_replace = title.replace(',', '').replace('?','').replace('“','').replace(':','').replace('.','').replace("‘",'').replace("’",'').replace('”','').replace('%','').replace("'",'').replace('"','').replace('#','')
title_split = title_replace.split()
title_list = list(title_split)
title_set = set(title_list)
title_word_count = []
for title_word in title_set:
    title_word_count.append((title_list.count(title_word),title_word))
    n = 0
for result in sorted(title_word_count, reverse=True):
    n += 1
    print(result[1], ':', result[0])

f = open('bucks.csv', 'w', encoding='utf-8-sig', newline='')

csv_writer = csv.writer(f)

title_word_count = []

for title_word in title_set:
    title_word_count.append((title_list.count(title_word),title_word))
    n = 0

for result in sorted(title_word_count, reverse=True):
    n += 1
    print(result[1], ':', result[0])
    if result[0] >= 2:
        csv_writer.writerow([result[1], result[0]])

f.close()


