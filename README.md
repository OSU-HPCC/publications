# Publications Facilitated by OSU HPCC

## Introduction

These are the files used for tracking and generating a formatted list of publications facilitated by OSU HPCC. Publications are stored in Bibtex format in yearly `.bib` files. LaTeX is used to generate a document from `main.tex`.

## Usage

### Generating List for Website
You will need a Linux command-line environment with `make` and `pdflatex` installed. Run `make main.pdf` to generate the list of publications in PDF format. For more information run `make help`. Once the document is generated, the list can be pasted into the website content-mangagement system.

### Adding New Publications
To add a new publication to the list, download the Bibtex entry from the publisher's website and copy it into the year `.bib` file. Add the line `\nocite{<Bibtex-Entry ID>}` to the appropriate year `.tex` file.

#### Example
If the Bibtex entry is as follows:

```latex
@article{Feng_2018,
	doi = {10.1016/j.jaerosci.2018.05.010},
	url = {https://doi.org/10.1016/j.jaerosci.2018.05.010},
	year = 2018,
	month = {sep},
	publisher = {Elsevier {BV}},
	volume = {123},
	pages = {185--207},
	author = {Yu Feng and Jianan Zhao and Clement Kleinstreuer and Qingsheng Wang and Jun Wang and Dee H. Wu and Jiang Lin},
	title = {An in silico inter-subject variability study of extra-thoracic morphology effects on inhaled particle transport and deposition},
	journal = {Journal of Aerosol Science}
}
```

Copy the entry to the Bibtex file (`2018.bib`). Add the line `\nocite{Feng_2018}` to `2018.tex`. Run `make main.pdf`.

## Files

1. `.gitignore` - Ignore extra files generating by compiling LaTeX source.
2. Year `.tex` files (any file with the naming convention `YYYY.tex`) - Each year contains a citation for every author from the publication database that published in that respective year.
3. `main.tex` - The main LaTeX file. This file generates the document. Publications are grouped by year.
4. Year `.bib` files (any file with the naming convention `YYYY.bib`) - These are collectively the publication database. Bibtex entries are used to keep track of publications facilitated by OSU HPCC.
