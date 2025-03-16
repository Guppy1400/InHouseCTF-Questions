1. wc -l http_logs.log / awk '{print $1}' http_logs.log | wc -l
	1. wc -l http_logs.log may not always give right answer if the log doesn't have anew line at the end 
2. awk '{print $7}' http_logs.log | sort | uniq -c | sort -nr | head -1 
	1.  '{print $7}'  = 7th field (column) from each line 
	2. sort 
		1. -n =  sorts numerically.
		2. -r = reverses order
	3. uniq -c = counts number of occurrences
	4. head -1 = only the top result
3. grep '404' http_logs.log | wc -l
4. grep '192.168.1.10' http_logs.log | wc -l 
