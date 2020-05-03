#!/usr/bin/env bash

cat *.json > _all_in_one.json

mongoimport _all_in_one.json --db VDSS_5 --collection test
