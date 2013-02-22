inFile = open('email2name.txt')

while True:
    line = inFile.readline().strip()
    if len(line)<=0:
        break
    i = line.find('@mit.edu')
    if i<0:
        print line
