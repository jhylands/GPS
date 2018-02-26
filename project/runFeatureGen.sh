#!/usr/bin/env bash
for file in ../gps-data/FormJ1.1/*; do python converterCode/json2Vec.py "$file" "$file.csv"; done
