# HPCC Publications
A series of scripts that generates a list of publications for the HPCC website.

## Requirements
- Linux environment that runs `make`.
- Working Python 3 distribution installed in `/usr/bin/python3`
- Working Bash installation installed in `/bin/bash`
- Optional: If the user wants the final list in a `.docx` format instead of a markdown format, they need to have Pandoc installed.

> For a non-standard installation of the above software, the user will need to update script shebangs.

## Usage
1. To add new publications to the list open `articles.csv` in your favorite spreadsheet program and add a new row with the appropriate entries.
2. Save the changes (make sure `articles.csv` remains in csv format and is named `articles.csv`).
3. Type `make pubs.md` into the command line.
4. Hit enter.
5. The scripts will create a (optionally two) new file called `pubs.md` (optionally `pubs.docx`) with the formatted list of publication arranged both alphabetically and by year.
6. Use Git (and GitHub) to track updates to the publications list.

> For simple data validation, type `make errors.md`. This will create a markdown file called `errors.md` with a list of citations that contain errors. New conditions can be added to the data validation script by adding appropriate if-statements to the functions beginning on line 110 of `error_check.py`.

## Files

### Starting Files

| File                           | Description                                                           |
|--------------------------------|-----------------------------------------------------------------------|
| README.md                      | This file.                                                            |
| articles.csv                   | List of publication in csv format.                                    |
| original_pub_list.odt          | Publications as I inherited them before project began.                |
| original_pub_list.pdf          | PDF version of `original_pub_list.odt`.                               |
| preprints.csv                  | Preprints that need to be added to `articles.csv` once published.     |
| Makefile                       | Project make file.                                                    |
| generate_pubs.py               | Creates formatted list of citations for use on website.               |
| citation.py                    | Python "library" for working with citations.                          |
| error_check.py                 | Checks for errors in publication list.                                |
| change_format.sh               | If user has pandoc installed, will create docx list of publications   |


### Resulting Files

| File                           |                                                                       |
|--------------------------------|-----------------------------------------------------------------------|
| pubs.md                        | Markdown formatted list of publications.                              |
| pubs.docx                      | docx formatted list of publications.                                  |
| errors.md                      | List of publications that contain possible errors.                    |

