#! /bin/bash
#
# postgres_bootstrap.sh
# Copyright (C) 2015 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#


echo "chaibase"
createuser -P chaibase
createdb -O chaibase
