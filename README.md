# Project Gutenberg browser and reader

## Comsumption

https://pypi.python.org/pypi/Gutenberg

https://www.npmjs.com/package/gutenberg

## Frontend Setup

To get an interactive development environment run:

    lein figwheel
open your browser at [localhost:3449](http://localhost:3449/).
This will auto compile and send all changes to the browser without the
need to reload. After the compilation process is complete, you will
get a Browser Connected REPL. An easy way to try it is:

    (js/alert "Am I connected?")

and you should see an alert in the browser window.

To clean all compiled files:

    lein clean

To create a production build run:

    lein do clean, cljsbuild once min

## Get book covers

Python script will fetch images for the books in "top_100.txt"

Install fim first:
```sh
npm install -g fetch-image
```

python get_cover_images.py > images.html
