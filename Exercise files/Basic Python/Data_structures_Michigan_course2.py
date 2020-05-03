
fname = input("Enter file name: ")
fh = open(fname)
sum_ = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    new = line.find(X-DSPAM)
    print(new)
    pos1 = line.find(":")
    num = line[pos1+1:]
    number = float(num.strip())
    sum_ = sum_ + number
    count = count +1
average = sum_/count
print("Average spam confidence: ",average)
#%%
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(len(c))
#%%
fruit = 'Banana'
fruit[0] = 'b'
print(fruit)
#%%
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
nlst = []
for line in fh:
    word = line.split()
    lst.append(word)
for words in lst:
   	for i in range (0,len(words)):
           nword = words[i]
           if not nword in nlst:
               nlst.append(nword)
nlst.sort()
print(nlst)
#%%
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From:"): continue
    words = line.split()
    print(words[1])
    count= count +1
 
print("There were", count, "lines in the file with From as the first word")
#%%
stuff = dict()
print(stuff['candy'])
#%%
stuff = dict()
print(stuff.get('candy',-1))
#%%
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = []
counts = {}
for line in handle:
    if not line.startswith("From:"): continue
    words = line.split()
    lst.append(words[1])
for word in lst:
    counts[word] = counts.get(word,0)+1
bigword = None
bigcount = None
for keys,values in counts.items():
    if bigcount is None or values > bigcount:
        bigcount = values
        bigword = keys
print(bigword,bigcount)
#%%
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = []
x = []
counts = {}
for line in handle:
    if not line.startswith("From"): continue
    words = line.split()
    try:
        nwords = (words[5])
        lst.append(nwords)
    except:
        continue
for word in lst:
    time = word.split(":")
    a = (time[0])
    x.append(a)
x.sort()
nhours = None
for hours in x:
    counts[hours] = counts.get(hours,0)+1
for hours in counts.items():
    print(hours[0],hours[1])
#%% 
## Above problem in a modified manner
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst = []
x = []
counts = {}
for line in handle:
    if not line.startswith("From"): continue
    words = line.split()
    try:
        nwords = (words[5])
        lst.append(nwords)
    except:
        continue
for word in lst:
    time = word.split(":")
    a = (time[0])
    x.append(a)
#x.sort()
nhours = None
for hours in x:
    counts[hours] = counts.get(hours,0)+1
print(sorted((k,v) for k,v in counts.items()))
"""
for hours in counts.items():
    print(hours[0],hours[1])
"""