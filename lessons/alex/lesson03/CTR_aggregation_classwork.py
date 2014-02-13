#!/usr/bin/python
# Import required libraries
from __future__ import division
import sys
import pandas as pd

def get_nytimes_datasets(n):
    """
    request NYT datasets
    @param int n     number of CSVs to obtain
    @return list      list of CSVs
    """
    assert n < 31
    df = pd.DataFrame()
    for i in range(1,n+1):
        url = 'http://stat.columbia.edu/~rachel/datasets/nyt'+str(i)+'.csv'
        print 'Retrieving...', url
        csv = pd.read_csv(url)
        print 'Obtained', len(csv), 'records'
        df = df.append(csv)
	print 'Finished data transfer'
    return df

def ratio(x,y):
    if y != 0:
        return x/y
    else:
        return 0

def calculate():
	z = get_nytimes_datasets(30)
	z["CTR"] = map(ratio, z["Clicks"], z["Impressions"])
	z.to_csv('nytimes_aggregation.csv')



# Start a counter and store the textfile in memory
age = 0
impressions = 0
clicks = 0

lines = sys.stdin.readlines()
lines.pop(0)
n = len(lines)

# For each line, find the sum of index 2 in the list.
for line in lines:

  clean_line = line.strip().split(',')
  age = age + int(clean_line[0])

  impressions = impressions + int(clean_line[2])
  clicks = clicks + int(clean_line[3])

  if age > int(oldest_person[0]):
  	oldest_person = c_line


print 'Total Unique Visitors: ', n
print 'Total Impressions: ', impressions
print 'Average Age: ', age/n
print 'Average Clicks per Impressions: ', clicks/impressions