import sys
import csv
# Create a citation object and a means for generating it

class Citation(object):
    authors = ""        # Publication authors
    year = ""           # Year published
    title = ""          # Title of publication
    journal = ""        # Journal title
    volume = ""         # Volume number
    issue = ""          # Issue number
    start_page = ""     # Starting page of article
    end_page = ""       # Ending page of article
    doi = ""            # DOI number for published works
    category = ""       # article, neup project, preprint, or presentation
    universities = ""   # For NEUP projects
    arxiv = ""          # Preprints
    meeting = ""        # Presented at the annual ...
    month = ""          # Month for presentations at conferences
    city = ""           # City where presentation was given
    state = ""          # State where presentation was given

    # Constructor
    def __init__(self, authors = "", year = "", title = "", journal = "", \
            volume = "", issue = "", start_page = "", end_page = "", doi = "", \
            category = "", universities = "", arxiv = "", meeting = "", \
            city = "", state = "", month = ""):
        self.authors = authors
        self.year = year
        self.title = title
        self.journal = journal
        self.volume = volume
        self.issue = issue
        self.start_page = start_page
        self.end_page = end_page
        self.doi = doi
        self.category = category
        self.universities = universities
        self.arxiv = arxiv
        self.meeting = meeting
        self.city = city
        self.state = state
        self.month = month

    # Returns the correct citation in markdown format
    def cite(self):
        # Journal articles
        if self.category == "article":
            cite_text = [ self.authors, " (" + self.year + "). ", \
                    self.title + ". ", "*", self.journal ]
            if (self.volume == "") and (self.issue == "") and \
                    (self.start_page == "") and (self.end_page == ""):
                cite_text.append("*")
            else:
                if self.volume != "":
                    cite_text.append(", " + self.volume + "*")
                else:
                    cite_text.append("*, ")
                if self.issue != "":
                    cite_text.append("(" + self.issue + ")")
                if self.start_page != "":
                    cite_text.append(", " + self.start_page)
                if self.end_page != "":
                    cite_text.append("-" + self.end_page)
                if self.doi != "":
                    cite_text.append(". DOI: [" + self.doi + \
                            "](https://doi.org/" + self.doi + ")")
        # Technical Report
        if self.category == "neupProject":
            cite_text = [ self.authors, " (" + self.year + "). ", \
                    "*" + self.title + "*. ", self.universities ]
            if self.doi != "":
                cite_text.append(". DOI: [" + self.doi + \
                        "](https://doi.org/" + self.doi + ")")
        # Presentation
        if self.category == "presentation":
            cite_text = [ self.authors, " (" + self.year + ", ", self.month + "). ", \
                    "*" + self.title + "* ", self.meeting + ", ", self.city + ", ", \
                    self.state ]
        cite_text.append(".")
        cite_text = "".join(cite_text)
        return cite_text

# Read csv file and create list of publications
def getPubs(filename, pubType):
    # List of citations
    pubs = []
    # Read in .csv file
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        if pubType == 'article':
            for row in readCSV:
                # skip column headers
                if row[0] == "authors":
                    continue
                pubs.append(Citation(authors = row[0], \
                        year = row[1], \
                        title = row[2], \
                        journal = row[3], \
                        volume = row[4], \
                        issue = row[5], \
                        start_page = row[6], \
                        end_page = row[7], \
                        doi = row[8], \
                        category = row[9]))
        if pubType == 'neup_proj':
            for row in readCSV:
                # skip column headers
                if row[0] == "authors":
                    continue
                pubs.append(Citation(authors = row[0], \
                        year = row[1], \
                        title = row[2], \
                        universities = row[3],
                        doi = row[4], \
                        arxiv = row[5], \
                        category = row[6]))
        if pubType == 'presentation':
            for row in readCSV:
                # skip column headers
                if row[0] == "authors":
                    continue
                pubs.append(Citation(authors = row[0], \
                        year = row[1], \
                        month = row[2], \
                        title = row[3], \
                        meeting = row[4], \
                        city = row[5], \
                        state = row[6], \
                        category = row[7]))
    return pubs
