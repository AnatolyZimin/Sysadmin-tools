import os

def isSQLite3(filename):
    from os.path import isfile, getsize

    if not isfile(filename):
        return False
    if getsize(filename) < 100: # SQLite database file header is 100 bytes
        return False
    else:
        fd = open(filename, 'rb')
        Header = fd.read(100)
        fd.close()

        if Header[0:16] == 'SQLite format 3\000':
            return True
        else:
            return False

log=open('sqlite_audit.txt','w')
for r,d,f in os.walk(r'.'):
  for files in f:
    if isSQLite3(files):
	  print files
	  print "[+] '%s' **** is a SQLITE database file **** " % os.path.join(r,files)
	  log.write("[+] '%s' **** is a SQLITE database file **** " % files+'\n')
    else:
	  log.write("[-] '%s' is NOT a sqlite database file" % os.path.join(r,files)+'\n')
	  log.write("[-] '%s' is NOT a sqlite database file" % files+'\n')
