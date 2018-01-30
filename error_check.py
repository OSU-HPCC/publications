#!/usr/bin/python3
import citation
import argparse
from datetime import datetime

def main():
    articles = citation.getPubs("articles.csv", "article")

    # User-defined name of articles csv
    parser = argparse.ArgumentParser(description = 'Script for checking \
            errors in the publication list.')
    parser.add_argument('--publist', type = str, required=True, \
            help = "Name of .csv file with journal articles.")

    args = parser.parse_args()
    article_csv = args.publist

    # Get publication list
    articles = citation.getPubs(article_csv, "article")

    # Sort publication in alphabetical order
    articles.sort(key = lambda x: x.authors)

    # Categories for data validation
    author_error = []
    year_error = []
    title_error = []
    journal_error = []
    volume_error = []
    issue_error = []
    start_page_error = []
    end_page_error = []
    doi_error = []

    final_list = []

    # Check each citation for errors
    for pub in articles:
        # Check authors
        if check_authors(pub):
            author_error.append(pub)
        # Check year
        if check_year(pub):
            year_error.append(pub)
        # Check title
        if check_title(pub):
            title_error.append(pub)
        # Check volume
        if check_volume(pub):
            volume_error.append(pub)
        # Check issue
        if check_issue(pub):
            issue_error.append(pub)
        # Check starting page
        if check_start_page(pub):
            start_page_error.append(pub)
        # Check ending page
        if check_end_page(pub):
            end_page_error.append(pub)
        # Check DOI
        if check_doi(pub):
            doi_error.append(pub)

    # Write out results to file
    final_list.append("# Citation Errors and Warnings")
    final_list.append("\nPlease check the following ")
    final_list.append("publications for possible errors in the respective fields.")
    if len(author_error) > 0:
        final_list.append("\n\n## Authors")
        for pub in author_error:
            final_list.append("\n + " + pub.cite())
    if len(year_error) > 0:
        final_list.append("\n\n## Year")
        for pub in year_error:
            final_list.append("\n + " + pub.cite())
    if len(title_error) > 0:
        final_list.append("\n\n## Title")
        for pub in title_error:
            final_list.append("\n + " + pub.cite())
    if len(volume_error) > 0:
        final_list.append("\n\n## Volume")
        for pub in volume_error:
            final_list.append("\n + " + pub.cite())
    if len(issue_error) > 0:
        final_list.append("\n\n## Issue")
        for pub in issue_error:
            final_list.append("\n + " + pub.cite())
    if len(start_page_error) > 0:
        final_list.append("\n\n## Starting Page")
        for pub in start_page_error:
            final_list.append("\n + " + pub.cite())
    if len(end_page_error) > 0:
        final_list.append("\n\n## Ending Page")
        for pub in end_page_error:
            final_list.append("\n + " + pub.cite())
    if len(doi_error) > 0:
        final_list.append("\n\n## DOI")
        for pub in doi_error:
            final_list.append("\n + " + pub.cite())
    if len(author_error + year_error + title_error + journal_error + \
            volume_error + issue_error + start_page_error + \
            end_page_error + doi_error) == 0:
        final_list.append("\n\n\n# No errors found.")
    final_list.append("\n")
    final_list = "".join(final_list)
    f = open("errors.md", "w")
    f.write(final_list)
    f.close()

# New data validation conditions can
# be added by adding if-statements
# to the respective function

# Check for errors in author field
def check_authors(pub):
    result = False
    # Insure nonempty
    if pub.authors == "":
        result = True
    # List of authors ending with a period
    elif pub.authors[-1] != ".":
        result = True
    # Check for elipses in the author list
    if "..." in pub.authors:
        result = True
    return result

# Check for errors in the year field
def check_year(pub):
    result = False
    # Check for a four-digit year within an appropriate range
    if len(pub.year) != 4:
        result = True
    else:
        try:
            test_year = int(pub.year)
            if (test_year < 2008 or test_year > datetime.now().year):
                result = True
        except ValueError:
            result = True
    # Insure nonempty
    if pub.year == "":
        result = True
    return result

# Check for errors in title field
def check_title(pub):
    result = False
    # Insure nonempty
    if pub.title == "":
        result = True
    # Insure title does not end with a period
    elif pub.title[-1] == ".":
        result = True
    return result

# Check for errors in journal field
def check_journal(pub):
    result = False
    # Insure journal does not end with a period
    if pub.journal[-1] == ".":
        result = True
    # Insure nonempty
    if pub.journal == "":
        result = True
    return result

# Check for errors in volume field
def check_volume(pub):
    result = False
    # Insure volume is empty or an integer
    if pub.volume == "":
        result = False
    else:
        try:
            check_me = int(pub.volume)
        except ValueError:
            result = True
    return result

# Check for errors in issue field
def check_issue(pub):
    result = False
    # Insure issue is empty or an integer
    if pub.issue == "":
        result = False
    else:
        try:
            check_me = int(pub.issue)
        except ValueError:
            result = True
    return result

# Check for errors in start_page field
def check_start_page(pub):
    result = False
    # Insure starting page is empty or an integer
    if pub.start_page == "":
        result = False
    elif pub.start_page[0] == "e":
        result = False
    # Exception for "Physics in Medicine and Biology"
    elif pub.start_page[0] == "N":
        result = False
    else:
        try:
            check_me = int(pub.start_page)
        except ValueError:
            result = True
    return result

# Check for errors in end_page field
def check_end_page(pub):
    result = False
    # Insure ending page is empty or an integer
    if pub.end_page == "":
        result = False
    else:
        try:
            check_me = int(pub.end_page)
        except ValueError:
            result = True
    return result

# Check for errors in the doi field
def check_doi(pub):
    result = False
    # Ensure DOI is nonempty and follows the DOI format
    if pub.doi == "":
        result = True
    elif pub.doi[:3] != "10.":
        result = True
    elif "/" not in pub.doi:
        result = True
    else:
        try:
            check_me = float(pub.doi[3:pub.doi.find("/")])
            if check_me < 1000:
                result = True
        except ValueError:
            result = True
    return result

if __name__ == '__main__':
    main()
