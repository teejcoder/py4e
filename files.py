# OPENING FILES
# fhand = open('./files/mbox.txt')
# print(fhand)

# TEXT FILES AND LINES
mboxhand = open('./files/mbox.txt')
count = 0   
for line in mboxhand:
    line = line.rstrip()
    count += 1
print('line count in mbox.txt:',count)

# stuff = 'Hello World!'
# stuff
# print('stuff:', stuff)

# stuff = 'X\nY'
# print('stuff:',stuff)
# print('stuff length:', len(stuff))

# READING FILES
fhand = open('./files/mbox-short.txt')
count = 0
for line in fhand:
    count += 1
print('line count in mbox-short.txt:', count)

fhand = open('./files/mbox-short.txt')
inp = fhand.read()
mboxname = inp[:21]
print('length of input:',len(inp))
print('first 20 characters of mbox:',mboxname)

# SEARCHING THROUGH A FILE
# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     # STRIPPING WHITESPACE
#     line = line.rstrip()
#     if line.startswith('From:'):
#         print('SEARCHINGFORTHISLINE:',line)

#PROCESSING LINE-BY-LINE SKIPPING UNINTERESTNG LINES
# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From:'):
#         continue
#     print('printing interestings lines', line)

# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     # Skip 'uninteresting lines'
#     if not line.startswith('From:'):
#         continue
#     # Process our 'interesting' line
#     print(line)

#USING FIND() METHOD
# fhand = open('./files/mbox-short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if line.find('@uct.ac.za') == -1:
#         continue
#     print('university email:',line)


# LETTING THE USER CHOOSE THE FILE NAME
# fname = input('enter the filename:\n')
# fhand = open(fname)
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count += 1
# print(f'there were {count} subject lines in {fname}')

# SAME AS ABOVE BUT WITH BEING GRACEFUL WITH ERRORS
# fname = input('enter a filename: \n')
# try:
#     fhand = open(fname)
# except:
#     print('file cannot be opened', fname)
#     exit()
# count = 0
# for line in fhand:
#     if line.startswith('Subject:'):
#         count += 1
# print(f'{count} amount of subject lines in {fname}')

# WRITING FILES
# fout = open('./files/output.txt', 'w')
# line1 = 'add this to fout text file.'
# line2 = 'this is line2, make sure this is added as well..'
# xx = line1 + ' ' + line2
# fout.write(xx)
# fout.close()
# print(fout)

# Exercise 1: Write a program to read through a file and 
# print the contents of the file (line by line) all in upper case.

# fopen = input('enter the filename: ')
# try:
#     fhand = open(fopen)
# except:
#     print('cannot find filename: ', fopen)
#     exit()
# for line in fhand:
#     line = line.rstrip()
#     line = line.upper()
#     print(line)


fopen = input('enter filename')
try:
    fhand = open(fopen)
except:
    print('file cannot be found: ')
    exit()
lines = 0
confscore = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        lines += 1
        n = float(line[-6:])
        confscore += n
avg = confscore / lines
print(avg)