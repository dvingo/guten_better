import re
import subprocess

filename = 'top_100.txt'

def parse_title(line):
    r =  ' '.join([re.sub(r' by .+', '', line).strip(), 'book cover'])
    return r

def get_cover_images(search):
    num = 10
    results = subprocess.check_output(['fim', search, '-n', str(num)])
    #print 'img results: ', results
    return results.split('\n')[:-1]

def url_to_img_tag(url):
    #print 'url: ', url
    return '<img src={}>'.format(url)

def start_html():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <title></title>
      </head>
      <body>

    '''

def end_html():
    return '''</body></html>'''

with open(filename) as f:
    print start_html()
    for line in f:
        title = parse_title(line)
        covers = get_cover_images(title)
        #print 'got covers ', covers
        print '<h1>{}</h1>'.format(title)
        for cover in covers:
            print url_to_img_tag(cover)
        print '<hr />'
    print end_html()
