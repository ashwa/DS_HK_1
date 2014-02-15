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

def get_local_nytimes_datasets():
    df = pd.DataFrame()
    csv = pd.read_csv('nytimes_aggregation.csv')
    df = csv
    return df

def file_exists(filename):
    try:
        with open(filename): return True
    except:
        return False

def ratio(x,y):
    if y != 0:
        return x/y
    else:
        return 0

def calculate_CTR():
    if file_exists('nytimes_aggregation.csv'): 
        z = get_local_nytimes_datasets
    else:
        z = get_nytimes_datasets(30)
	
    print "Locating CSV file from the web...."
    z["CTR"] = map(ratio, z["Clicks"], z["Impressions"])
    z.to_csv('nytimes_aggregation.csv')

def calculate_AGE():
    a = get_local_nytimes_datasets
    a["CTRage"] = map(ratio, a["age"], a["CTR"])
    a.to_csv('nytimes_aggregation.csv')

def calculate_gender():
    g = get_local_nytimes_datasets
    g["CTRgender"] = map(ratio, g["gender"], g["CTR"])
    g.to_csv('nytimes_aggregation.csv')

def calculate_signedin():
    s = get_local_nytimes_database
    s["CTR_signedin"] = map(ratio, s["calculate_signedin"], s["CTR"])
    s.to_csv('nytimes_aggregation.csv')

