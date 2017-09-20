from citation import *
import csv

# List of citations
pubs = []

# Read csv file and create
with open('articles.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        # skip column headers
        if row[0] == "citation":
            continue
        pubs.append(Citation(authors = row[1], \
                year = row[2], \
                title = row[3], \
                journal = row[4], \
                volume = row[5], \
                issue = row[6], \
                start_page = row[7], \
                end_page = row[8], \
                doi = row[9], \
                category = row[10]))

print(pubs[0].cite())
print(pubs[-1].cite())
