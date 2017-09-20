import sys
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
    city = ""           # City where presentation was given
    state = ""          # State where presentation was given

    # Constructor
    def __init__(self, authors, year, title, journal, \\
            volume, issue, start_page, end_page, doi, \\
            category, universities, arxiv, meeting, \\
            city, state):
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

    # Returns the correct citation in markdown format
    def cite(self):
        # Journal articles
        if category == "article":
            cite_text = [ article, " (" + year + "). ", title + ". ", "*", journal ]
            if (volume == "") and (issue == "") and (start_page == "") and (end_page == ""):
                cite_text = "*."
            else:
                if volume != "":
                    cite_text.append(", " + volume + "*")
                else:
                    cite_text.append("*, ")
                if issue != "":
                    cite_text.append("(" + issue + ")")
                if start_page != "":
                    cite_text.append(", " + start_page)
                if end_page != "":
                    cite_text.append("-" + end_page)
                cite_text.append(".")
                cite_text = "".join(cite_text)

        return cite_text
