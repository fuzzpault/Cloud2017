#!/usr/bin/env python
import mincemeat
import sys
import time

# Demo program for finding the average word length.
# Paul Talaga April 13 2017

# Don't forget to start a client!
# ./mincemeat.py -l -p changeme

data = ["Humpty Dumpty sat on a wall",
        "Humpty Dumpty had a great fall",
        "All the King's horses and all the King's men",
        "Couldn't put Humpty together again and again",
        ]
# The data source can be any dictionary-like object
  
datasource = dict(enumerate(data))

def mapfn(k, v):
    for w in v.split():
        yield 'WordCount',1
        yield 'letterCount', len(w)

def reducefn(k, vs):
    result = sum(vs)
    return result

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results
print "Average word lengh %s" % (str(float(results['letterCount']) / results['WordCount']))





