# -*- coding: utf-8 -*-
from json import loads as json_loads
import os
import urllib

book_data_filename = './book_data.json'
output_dir = 'new_images'
book_data = None

with open(book_data_filename) as book_data_file:
    book_data = json_loads(book_data_file.read())

def get_image_type(url):
    return url.split('.')[-1].strip()

def download_book(book):
  name =  book['name'].encode('utf-8')
  img_type = get_image_type(book['cover_url'])
  output_file = os.path.join(output_dir, "{}.{}".format(name, img_type))
  urllib.urlretrieve(book['cover_url'], output_file)

for book in book_data:
    download_book(book)

print 'Done.'
