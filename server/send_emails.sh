#!/bin/bash -

export PYTHONPATH="${PYTHONPATH}:/srv/guten_better/server/guten_better_venv/lib/python2.7/site-packages/"

python /srv/guten_better/server/daily_sender.py
