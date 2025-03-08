1. strings -n8 yarn.jpeg
	1.  strings extracts all printable ASCII 
	2.  -n option = minimum number of consecutive characters required
		1. we use this since we know the flag starts as SOC_CTF{
2. If flag not seen right away 
	1. strings -n8 yarn.jpeg | grep 'SOC_CTF{'
