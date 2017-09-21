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
                cite_text.append("*.")
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
                cite_text.append(".")
                cite_text = "".join(cite_text)
        # NEUP Project
        if self.category == "neupProject":
            cite_text = [ self.authors, " (" + self.year + "). ", \
                    "*" + self.title + "*. ", self.universities ]
            if self.doi != "":
                cite_text.append(". DOI: [" + self.doi + \
                        "](https://doi.org/" + self.doi + ")")
            cite_text.append(".")
            cite_text = "".join(cite_text)
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
        if pubType == 'neup_proj':
            for row in readCSV:
                # skip column headers
                if row[0] == "citation":
                    continue
                pubs.append(Citation(authors = row[1], \
                        year = row[2], \
                        title = row[3], \
                        universities = row[4],
                        doi = row[5], \
                        arxiv = row[6], \
                        category = row[7]))
        if pubType == 'presentation':
            for row in readCSV:
                # skip column headers
                if row[0] == "citation":
                    continue
                pubs.append(Citation(authors = row[1], \
                        year = row[2], \
                        month = row[3], \
                        title = row[4], \
                        meeting = row[5], \
                        city = row[6], \
                        state = row[7], \
                        category = row[8]))
    return pubs
