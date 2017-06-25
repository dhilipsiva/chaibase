#! /bin/bash
#
# postgres_bootstrap.sh
# Copyright (C) 2015 dhilipsiva <dhilipsiva@gmail.com>
#
# Distributed under terms of the MIT license.
#

set -x

createuser -P chaibase -d
createdb -O chaibase chaibase
./scripts/recreate.sh
