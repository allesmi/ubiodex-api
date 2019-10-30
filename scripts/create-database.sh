#!/usr/bin/bash

psql -d $DATABASE -f ubiodexapi/schema.sql
