#!/usr/bin/bash

tail -n+2 data/taxa.txt | cut -f 11 | sort | uniq >tmp.csv
psql -d $DATABASE -c "\copy kingdom (name) from 'tmp.csv';"

tail -n+2 data/taxa.txt | cut -f 12 | sort | uniq >tmp.csv
psql -d $DATABASE -c "\copy phylum (name) from 'tmp.csv';"

tail -n+2 data/taxa.txt | cut -f 13 | sort | uniq >tmp.csv
psql -d $DATABASE -c "\copy class (name) from 'tmp.csv';"

tail -n+2 data/taxa.txt | cut -f 14 | sort | uniq >tmp.csv
psql -d $DATABASE -c "\copy \"order\" (name) from 'tmp.csv';"

tail -n+2 data/taxa.txt | cut -f 16 | sort | uniq >tmp.csv
psql -d $DATABASE -c "\copy family (name) from 'tmp.csv';"

rm tmp.csv
