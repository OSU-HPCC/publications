# Publications Facilitated by OSU HPCC

## Introduction

These are the files used for tracking and generating a formatted list of publications facilitated by OSU HPCC. Publications are stored in Bibtex format in yearly `.bib` files. LaTeX is used to generate a document from `main.tex` and `main-apa.tex`.

## Usage

### Generating List for Website
You will need a Linux command-line environment with `make` and `xelatex` installed. Run `make` to generate the list of publications in PDF format. For more information run `make help`. Once the document is generated, the list can be pasted into the website content-mangagement system.

### Adding New Publications
To add a new publication to the list, download the Bibtex entry from the publisher's website or from the DOI service (see `curl` option below) and copy it into the year `.bib` file. Make sure that the BibTeX entry ID (the string `Feng_2018` in the example) is unique.

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

Copy the entry to the Bibtex file (`2018.bib`). Run `make`.

If you know a DOI, you can get its BibTeX entry programmatically with the `curl` command.

This option will get output like the example above (except that any slashes within the DOI within the URL field will be rendered as `%2F`):
```bash
curl -LH "Accept: application/x-bibtex" https://doi.org/10.1016/j.jaerosci.2018.05.010
```

This option will get a BibTeX entry without any line breaks or `%2F` in the URL:
```bash
curl -LH "Accept: text/bibliography; style=bibtex" https://doi.org/10.1016/j.jaerosci.2018.05.010
```

There is also at least one non-BibTeX option. This one will produce something like an APA style citation:
```bash
curl -LH "Accept: text/bibliography; charset=utf-8" https://doi.org/10.1016/j.jaerosci.2018.05.010
```

More info on the similar options with the `Accept` header can be found at https://citation.crosscite.org/docs.html.

### Adding a new publication year

Create `.bib` and `.tex` files for the year (e.g. 2019). (The `.tex` file only has to exist; its content will be managed automatically by the makefile.)

Edit `main.tex` and `main-apa.tex`. Add the line `\addbibresource{2019.bib}` before the the `\begin{document}` section and add a section after like this:
```
\begin{refsection}
\input{2019}
\printbibliography[title={2019}]
\end{refsection}
```


## Files

1. `.gitignore` - Ignore extra files generating by compiling LaTeX source.
2. Year `.tex` files (any file with the naming convention `YYYY.tex`) - Each year contains a citation for every author from the publication database that published in that respective year. (The contents of these files are generated automatically from the corresponding `.bib` files.)
3. `main.tex` and `main-apa.txt` - The main LaTeX file. These files generate the document with different citation formats. Publications are grouped by year.
4. Year `.bib` files (any file with the naming convention `YYYY.bib`) - These are collectively the publication database. Bibtex entries are used to keep track of publications facilitated by OSU HPCC.
