from json import dumps as json_dumps
import sys

titles_filename = 'top_35.txt'
covers_filename = 'cover-image-list-no-names.txt'
titles_data = None
covers_data = None

with open(titles_filename) as titles_file:
    titles_data = titles_file.readlines()

with open(covers_filename) as covers_file:
    covers_data = covers_file.readlines()

# print "got titles data: ", titles_data
# print "got covers data: ", covers_data

combined = zip(titles_data, covers_data)

# print 'combined: ', combined

# Input has form:
# 'Pride and Prejudice by Jane Austen (845)\n'
def parse_title_data(title):
    title = title.strip()
    name, second = title.split(' by ')
    author, guten_id = second.split('(')
    guten_id = guten_id[:-1]
    # print 'got name: ', name
    # print 'author: ', author
    # print 'ID: ', guten_id
    return {'name': name, 'author': author, 'guten_id': guten_id}

output = []
for title_tuple in combined:
    title_data = parse_title_data(title_tuple[0])
    cover_url = title_tuple[1]
    title_data['cover_url'] = cover_url
    output.append(title_data)
print json_dumps(output)
