Duplicate MACs: 98:E2:55 (2) & E0:BF:B2 (3)
1. awk -F ',' '{print $2}' ARP_Table.csv | sort | uniq -d | wc -l
	1. -F ','  = sets the delimiter to a comma 
	2. awk '{print $2}' = extracts the second column
	3. uniq -d = shows only lines that appear more than once
	4. wc -l = counts number of lines
2. awk -F ',' '{print $2}' ARP_Table.csv | sort | uniq -c | sort -nr | head -n 1
	1. uniq -c  = count unique occurrences 
	2. Sort 
		1. -n = Sorts numerically 
		2. -r = sorts in reverse order 
	3. head 
			-n  = displays specified number of rows top down 
3. wc -l ARP_Table.csv
	1. subtract 1 cause of header
4. awk -F ',' '{print $2}' ARP_Table.csv | sort | uniq | wc -l
	1. subtract 1 cause of header 
5. grep '60:A3:E3' ARP_Table.csv
6. awk -F ',' '$3 ~ /static/' ARP_Table.csv | wc -l
	1. ~  /x/ = contains 
7. https://www.devicekb.com/hardware/mac-vendors/maclookup 