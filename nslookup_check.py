import subprocess										# Import the subprocess module
for server in open('server_list.txt'):				# Open the file and read each line
	subprocess.Popen(('nslookup '+server))	# Run the nslookup command for each server in the list
