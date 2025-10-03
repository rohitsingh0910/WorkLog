#!/bin/bash
mkdir -p ~/bash-play/session2 && cd ~/bash-play/session2
echo "first"  > out.txt
echo "second" >> out.txt
cat out.txt
wc -l < out.txt
command > /dev/null
ls no_such_file 2> errors.log
ls . 1> ok.log 2> err.log
ls . no_such_file > all.log 2>&1
ls . no_such_file &> all.log
some_command 2>> error.log
ls -1 | wc -l
cat /etc/passwd | grep bash | wc -l
ls -1 | tee files.txt | wc -l
cat files.txt
cat <<'EOF' > config.ini
[user]
name = Alice
email = alice@example.com
EOF
cat config.ini
wc -w <<< "this is a quick test"
grep -R "main" . 2>err.log | tee matches.txt | wc -l > count.txt



