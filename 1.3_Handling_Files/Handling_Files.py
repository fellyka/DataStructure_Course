#### Read the sampleText.txt that comes with this folder
#### Then display what is written in the file
import sys
try:
    f = open('sampleText.txt', 'r')
    while True:
       line = f.readline()
       if len(line) == 0:
           break
       print(line)
except IOError:
       print('The file entered does not exist')
       sys.exit(1)
f.close()
