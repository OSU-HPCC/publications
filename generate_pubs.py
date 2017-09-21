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

print(articles[0].cite())
print(neups[0].cite())
print(presentations[0].cite())
