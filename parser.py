import csv
import nltk
with open('loglines.csv','rb') as csvfile:
    loglinereader = csv.reader(csvfile, delimiter=';')
    for i,row in enumerate(loglinereader):
        if i % 2==0:
            if i != 0:
                #print row[2]
                logline = row[2].decode('utf-8')
                print nltk.pos_tag(logline.split())

