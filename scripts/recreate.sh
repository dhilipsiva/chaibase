#! /bin/bash
#
# recreate.sh
# Copyright (C) 2017 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#


rm db.sqlite3
find . -regex ".*/migrations/00.*.py" | xargs rm
./manage.py makemigrations
./manage.py migrate
./manage.py seed_db
