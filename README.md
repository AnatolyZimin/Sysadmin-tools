# Sysadmin-tools
Some interesting Python scripts

batch_file_rename.py - This will batch rename a group of files in a given directory, once you pass the current and new extensions

create_dir_if_not_there.py - Checks to see if a directory exists in the users home directory, if not then create it

dir_test.py - Tests to see if the directory testdir exists, if not it will create the directory for you

env_check.py - This script will check to see if all of the environment variables I require are set

fileinfo.py - Show file information for a given file

folder_size.py - This will scan the current directory and all subdirectories and display the size.

logs.py - This script will search for all *.log files in the given directory, zip them using the program you specify and then date stamp them

move_files_over_x_days.py - This will move all the files from the src directory that are over 240 days old to the destination directory.

nslookup_check.py - This very simple script opens the file server_list.txt and the does an nslookup for each one to check the DNS entry

osinfo.py - Displays some information about the OS you are running this script on

ping_servers.py - This script will, depending on the arguments supplied will ping the servers associated with that application group.

ping_subnet.py - After supplying the first 3 octets it will scan the final range for available addresses

powerdown_startup.py - This goes through the server list and pings the machine, if it's up it will load the putty session, if its not it will notify you.

puttylogs.py - Zip up all the logs in the given directory

script_count.py - This scans my scripts directory and gives a count of the different types of scripts

script_listing.py - This will list all the files in the given directory, it will also go through all the subdirectories as well

testlines.py - This very simple script open a file and prints out 100 lines of whatever is set for the line variable
