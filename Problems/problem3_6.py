import sys

infile = sys.argv[1]
outfile = sys.argv[2]


inf = open(infile)
outf = open(outfile, "w")
for line in inf:
  line = line.strip("\n")
  charct = len(line)
  charctstr = str(charct)
  outf.write(charctstr+"\n")

inf.close()
outf.close()
