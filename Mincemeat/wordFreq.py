#!/usr/bin/env python
import mincemeat
import sys

# Demo program for reading in a file and printing the top 10 words in the file.
# Paul Talaga April 13 2017

# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

if len(sys.argv) < 2:
  print "Give me a file on the command-line"
  sys.exit(1)

file = open(sys.argv[1],'r')
data = file.readlines()
file.close()

# The data source can be any dictionary-like object
datasource = dict(enumerate(data))

def mapfn(k, v):
    for word in v.split():
      word = word.strip()
      if len(word) >= 1:
        yield word, 1

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")

resultlist = []

# Convert the dictionary into an array of tuples
for k in results.keys():
  resultlist.append((k,results[k]))
  
# Sort the array of tuples by the 2nd element in the tuple
resultlist = sorted(resultlist, key=lambda a: -a[1])

# Print the first 10 elements of the array
print resultlist[:10]


