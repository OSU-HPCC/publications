import citation
import argparse

# User-defined arguments
parser = argparse.ArgumentParser(description = 'Script for generating \
        formatted list of citations for website.')
parser.add_argument('--articles', type = str, required=True, \
        help = "Name of .csv file with journal articles.")
parser.add_argument('--neup', type = str, required=True, \
        help = "Name of .csv file with NEUP projects.")
parser.add_argument('--presentations', type = str, required=True, \
        help = "Name of .csv file with presentations.")
parser.add_argument('--output', type = str, required=True, \
        help = "Name of ouput markdown file.")

# Read in file names
args = parser.parse_args()
article_csv = args.articles
neup_csv = args.neup
presentations_csv = args.presentations
outfile_csv = args.output

# Get publication lists
articles = citation.getPubs(article_csv, "article")
neups = citation.getPubs(neup_csv, "neup_proj")
presentations = citation.getPubs(presentations_csv, "presentation")

# Make sure publication are in alphabetical order
articles.sort(key = lambda x: x.authors)
neups.sort(key = lambda x: x.authors)
presentations.sort(key = lambda x: x.authors)

# Get all years with publications
years = []
for pub in articles:
    years.append(pub.year)
for pub in neups:
    years.append(pub.year)
for pub in presentations:
    years.append(pub.year)

# Remove non-unique values
years = list(set(years))
years.sort(reverse = True)
print(years)
