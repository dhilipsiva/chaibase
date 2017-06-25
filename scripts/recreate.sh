#! /bin/bash
#
# recreate.sh
# Copyright (C) 2017 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#


# rm db.sqlite3
./manage.py reset_db -c --noinput
find . -regex ".*/migrations/00.*.py" -exec rm {} +
./manage.py makemigrations
./manage.py migrate
./manage.py seed_db
