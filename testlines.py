line="Test you want to print\n"	# This sets the variable for the text that you want to print
f=open('mylines.txt','w')				# Create the file to store the output
for i in range(1,101):					# Loop 100 times
  f.write(line)								# Write the text to the file
f.close()									# Close the file
