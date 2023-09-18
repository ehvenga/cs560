#!/bin/sh
for file in *.py; do
    cat disclaimer.txt $file >> $file.$$
    mv $file.$$ $file
done
