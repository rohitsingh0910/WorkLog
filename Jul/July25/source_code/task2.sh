#!/bin/bash
printf "a\nb\nc\nd\ne\n" > lines.txt
wc -l < lines.txt > count.txt
cat count.txt
ls . nofile 1>ok.txt 2>err.txt
ls . nofile > both.txt 2>&1
ls -1 | tee list.txt | wc -l
ls -1 | tee -a list.txt | wc -l
cat <<'EOF' > db.conf
host=localhost
port=5432
user=$USER
pass=secret
EOF
cat db.conf
echo "apple banana apple orange banana apple" > text.txt
tr -s ' ' '\n' < text.txt | sort | uniq -c | sort -nr | head -3 > top3.txt
cat top3.txt

