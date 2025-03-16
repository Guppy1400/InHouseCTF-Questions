1. jq -r '.[] | select(.status == 403) | .user' api_access_logs.json | sort | uniq
	1. jq -r '.[]' 
		1. reads each entry in the JSON file
		2. -r = raw output 
	2. select(.status == 403 
		1. filters logs where the status code is 403 
	3. .user
		1. extracts only the user field
	4. sort | uniq
		1.  sorts the usernames alphabetically and removes duplicates

2. jq -r '.[] | select(.user == "cnoland") | .timestamp' api_access_logs.json | sort | head -n 1
	1. select(.user == "cnoland")
		1. finds all log entries related to cnoland
	2. .timestamp 
		1. extracts only the timestamps
	3. head -n 1
		1. displays only the first occurrence

3. jq -r '.[] | select(.user == "cnoland" and .status == 200)' api_access_logs.json
	1. select(.user == "cnoland" and .status == 200)
		1. looks for logs where cnoland successfully executed a request
		2. no output means never had a successful request

4. jq -r '[.[] | select(.user == "bthompson" and .status == 200)] | length' api_access_logs.json
	1. select(.user == "bthompson" and .status == 200) 
		1. finds all logs where bthompson successfully executed a request
	2. [   ] around part above 
		1. turns the filtered logs in an array
	3. length 
		1. counts how many objects are in array

5. jq -r '.[] | .user' api_access_logs.json | sort | uniq | wc -l
	1. .user 
		1. extracts the user
	2. sort | uniq
		1. sorts and removes duplicate usernames
	3. wc -l 
		1. counts the number users

6. jq -r 'length' api_access_logs.json
	1. length 
		1. counts how many objects are in array
