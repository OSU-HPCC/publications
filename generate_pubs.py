#!/usr/bin/python3
import citation
import argparse

def main():
    # User-defined arguments
    parser = argparse.ArgumentParser(description = 'Script for generating \
            formatted list of citations for website.')
    parser.add_argument('--articles', type = str, required=True, \
            help = "Name of .csv file with journal articles.")
    parser.add_argument('--tech', type = str, required=True, \
            help = "Name of .csv file with technical reports.")
    parser.add_argument('--presentations', type = str, required=True, \
            help = "Name of .csv file with presentations.")
    parser.add_argument('--output', type = str, required=True, \
            help = "Name of ouput markdown file.")

    # Read in file names
    args = parser.parse_args()
    article_csv = args.articles
    neup_csv = args.tech
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

    # Final Formatted list
    final_list = []
    for year in years:
        final_list.append("\n\n# " + year)
        # Articles
        if thatYearsPubs(year, articles):
            final_list.append("\n\n## Articles")
            for pub in thatYearsPubs(year, articles):
                final_list.append("\n + " + pub.cite())
        # Technical Reports
        if thatYearsPubs(year, neups):
            final_list.append("\n\n## Technical Reports")
            for pub in thatYearsPubs(year, neups):
                final_list.append("\n + " + pub.cite())
        # Presentations
        if thatYearsPubs(year, presentations):
            final_list.append("\n\n## Presentations")
            for pub in thatYearsPubs(year, presentations):
                final_list.append("\n + " + pub.cite())

    # Write output to markdown file
    final_list.append("\n")
    final_list = "".join(final_list)
    f = open(outfile_csv, "w")
    f.write(final_list)
    f.close()

# Publication for extracting all the pubs
# from a specific year
def thatYearsPubs(year, pubs):
    yourPubs = []
    for publication in pubs:
        if publication.year == year:
            yourPubs.append(publication)
    return yourPubs

if __name__ == '__main__':
    main()
