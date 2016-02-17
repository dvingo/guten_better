Overview of the various scripts in this directory.

`get_cover_images.py`

Parses the `top_100.txt` file of Gutenberg books and performs a search against
gooogle image search, fetching `n` image urls. Outputs a html file to stdout
with a section for each book and the images for that title.

This is intended for a user to select the best image to use as a cover.

The human should make a text file of one image url per line corresponding
to the book's line in `top_100.txt`.

`make_book_data.py` will consume both these files and produce a json data
structure that can be consumed by an application.

`download_cover_images.py` will read in the json file from the previous step
and download the images in a local directory.
