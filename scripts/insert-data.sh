#!/usr/bin/bash

tail -n+2 data/taxa.txt | cut -f 1,10 | sort | uniq >tmp.csv
psql -d $DATABASE -c "\copy taxon (taxon_id, scientific_name) from 'tmp.csv';"

rm tmp.csv
