#!/bin/bash
mkdir -p session1_lab/{raw,processed,archive}
echo "d1" > session1_lab/raw/day1.txt
echo "d2" > session1_lab/raw/day2.txt
echo "d3" > session1_lab/raw/day3.txt

cp -av session1_lab/raw/*.txt session1_lab/processed/

mv -v session1_lab/processed/day3.txt session1_lab/archive/day3_final.txt

rmdir session1_lab/archive     # fails because not empty
rm -rI session1_lab            # capital -I is safer (ask once)
