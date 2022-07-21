#### Appending sampleText_1.txt
import sys

text = ''' The file is appended from here.... \nWith This SAMPLE text'''
f = open('sampleText_1.txt', 'a')
f.write("%s" %text)
f.close()

f = open('sampleText_1.txt', 'r')
lines = f.readlines()
f.close()

print('Content of file is: ')
for line in lines:
    print(line)
