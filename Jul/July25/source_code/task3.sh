#!/bin/bash
mkdir -p session1_lab/{raw,processed,archive}
echo "d1" > session1_lab/raw/day1.txt
echo "d2" > session1_lab/raw/day2.txt
echo "d3" > session1_lab/raw/day3.txt

cp -av session1_lab/raw/*.txt session1_lab/processed/

mv -v session1_lab/processed/day3.txt session1_lab/archive/day3_final.txt

rmdir session1_lab/archive
rm -rI session1_lab
touch log_{01..05}.txt
mkdir picked
cp -v log_0[1-3].txt picked/
mv -v log_05.txt log_5.txt
mv -i src dest
cp -n src dest
echo "alias rm='rm -i'" >> ~/.bashrc && source ~/.bashrc
