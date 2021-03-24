file = open ("out.csv","r")

totala = 0
totals = 0

lsta = []
lsts = []

line = file.readline()

while line:
    print(line)
    
    records = line.split(",")
    a = int(records[-1])
    s = int(records[-2])

    totala += a
    totals += s

    lsta.append(a)
    lsts.append(s)

    line = file.readline()

file.close()   

print(totala, totals)
print(max(lsta), max(lsts))