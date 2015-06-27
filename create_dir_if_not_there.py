import os												# Import the OS module
home=os.path.expanduser("~")				# Set the variable home by expanding the users set home directory
print home												# Print the location
if not os.path.exists(home+'/testdir'):		# Check to see if the directory exists
  os.makedirs(home+'/testdir')					# If not create the directory, inside their home directory
