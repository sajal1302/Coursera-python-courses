fname = input("Enter file name: ")
fh = open(fname)
lst = list()
sp=list()
for line in fh:
    x=line.rstrip()
    sp=x.split()
    for z in sp:
        if z in lst:
            continue
        else:
            lst.append(z)
lst.sort()
print(lst)