#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL',0)
data = featureFormat(data_dict, features)
#print data[0]


### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
len_data = len(data_dict)
#print data_dict.items()[0][1]['salary']
print "__________________________________________________\n\n"
print "biggest enron outlier, , comment line:13 for this"
temp = 0
name = ""
for i in range(0, len_data):
    if data_dict.items()[i][1]['bonus'] > temp and data_dict.items()[i][1]['bonus'] != 'NaN':
        temp = data_dict.items()[i][1]['bonus']
        name = data_dict.items()[i][0]
print temp
print "biggest enron outlier is :", name,"\n"


print "__________________________________________________\n\n"
print "more enron outliers, , un-comment line:13 for this\n"

print "serching for some other outliers in data....\n"
for i in range(0, len_data):
    if data_dict.items()[i][1]['bonus'] > 5000000 and data_dict.items()[i][1]['salary'] > 1000000 and data_dict.items()[i][1]['bonus'] != 'NaN':
        temp = data_dict.items()[i][1]['bonus']
        name = data_dict.items()[i][0]
        print temp
        print name,"\n"