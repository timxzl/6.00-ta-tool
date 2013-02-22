import codecs
##data = []
inFile = codecs.open('membership.html', encoding='utf-8')
while True:
    line = inFile.readline()
    if len(line)<=0:
        break
    i = line.find('<a href="mailto:')
    if i>=0:
        j = line.index(':', i+1)
        k = line.index('"', j+1)
        mail = line[j+1:k]
        p = line.index('>', k+1)
        q = line.index('</a>', p+1)
        name = line[p+1:q].strip()
        print mail + '\t' + name
##        data.append([mail, name])
##        if name.find('\xa0')>=0:
##            print [mail, name]
##            print line, i, j, k, p, q, mail, name
##            print len(line)
##            print ''.join(['^' if pos==i or pos==j or pos==k or pos==p or pos==q else line[pos] for pos in range(len(line))])
##            break

inFile.close()
