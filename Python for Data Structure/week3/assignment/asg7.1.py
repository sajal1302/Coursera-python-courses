# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for x in fh:
    y=x.rstrip()
    print(y.upper())