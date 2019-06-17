library("tidyverse")
library("RefManageR")

dois <- read_csv("data/pub_dois.txt")

bib_entries <- GetBibEntryWithDOI(dois$doi, "pubs.bib", delete.file = F)
