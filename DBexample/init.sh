#!/bin/sh

# check whether database file exists
FILE=database.db
if [[ -f "$FILE" ]]; then
	echo "$FILE exists."
else
	touch database.db
	echo "created $FILE."
fi

# fill database with values
python3 create_db.py
