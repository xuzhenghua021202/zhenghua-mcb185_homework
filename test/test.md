# question 2 
	+  cat colors_extended.tsv | grep "#FF...." | grep "255           

# question 3 
	+ gunzip -c jaspar2024_core.transfac.gz | grep "ID" | uniq -c | cut -f 4 -d " " | sort | uniq -c
	