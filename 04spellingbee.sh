gunzip -c dictionary.gz | grep -v "[^oznrica]" | grep "r" | grep -c -E "^.{4,}"
