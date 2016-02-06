
import requests


def get_next_text_chunk(guten_id, current_chunk_index=None, chunk_length=10000):
    """ Returns the next readable chunk for the given gutenberg text """

    text = get_guten_text(guten_id)

    start_idx = (current_chunk_index + 1) * chunk_length if current_chunk_index is not None else 0
    if start_idx >= len(text):
        return None

    end_idx = min(start_idx + chunk_length, len(text) - 1)

    return text[start_idx : end_idx]

def get_guten_text(guten_id):
    """ Grabs the plaintext version of the book at the given ID from the Web and returns
    a stripped and ready-to-read version"""

    url = 'http://www.gutenberg.org/files/{0}/{0}-0.txt'.format(guten_id)
    res = requests.get(url)

    text = res.text.encode('utf-8').strip()
    book_text = strip_garbage_from_guten_text(text)
    return book_text

def strip_garbage_from_guten_text(text):
    clean = text[text.find('***') + 3 :] # cut to the *** START...
    clean = clean[clean.find('***') + 3 :] # cut to the ...<title> ***
    clean = clean[: clean.rfind('*** END')] # cut the end with *** END ...
    return clean.strip()
