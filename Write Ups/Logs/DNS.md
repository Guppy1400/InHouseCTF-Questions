1.  grep -o 'secure-bank.com' dns_record_analysis.log | wc -l
	1. -o outputs only the matching part instead of the whole line.
	2. wc -l counts how many lines are in the output
2. awk '{print $5}' dns_record_analysis.log | grep -o -i 'MX' | wc -l
	1. {print $5} = print the fifth column
	2. grep -i = case-insensitive
3. awk '{print $5}' dns_record_analysis.log | sort | uniq -c | sort -nr | head -1
	1. uniq -c = counts how many times each appears
	2. sort 
		1. -n sorts numerically.
		2. -r reverses the order
	3. head -1 = display the top result
