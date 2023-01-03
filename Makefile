## all			: Generate all outputs (PDF, HTML)
all : pdf html

## pdf			: Generate PDF outputs
pdf : main.pdf main-apa.pdf

## html			: Generate HTML outputs
html : main-html.html main-apa-html.html

# Automatically generate the yearly .tex files from the .bib files
20%.tex : 20%.bib
	sed -nE '/^@/{s/^@.*\{(.*),/\\nocite\{\1\}/;p}' $< > $@

## main.pdf		: Generate PDF file with publications
main.pdf : 20*.bib 20*.tex main.tex
	xelatex main.tex
	biber main
	xelatex main.tex

## main-apa.pdf		: Generate PDF file with publications (APA format)
main-apa.pdf : 20*.bib 20*.tex main-apa.tex
	xelatex main-apa.tex
	biber main-apa
	xelatex main-apa.tex

## main-html.html	: Generate HTML file with publications
main-html.html : 20*.bib 20*.tex main-html.tex
	htxelatex main-html
	biber main-html
	htxelatex main-html

## main-apa-html.html	: Generate HTML file with publications (APA format)
main-apa-html.html : 20*.bib 20*.tex main-apa-html.tex
	htxelatex main-apa-html
	biber main-apa-html
	htxelatex main-apa-html

.PHONY : clean clean-intermediates clean-outputs
## clean		: Remove generated files and start over
clean : clean-intermediates clean-outputs

## clean-intermediates	: Remove intermediate files only
clean-intermediates :
	rm -f *.aux
	rm -f *.bbl
	rm -f *.bcf
	rm -f *.blg
	rm -f *.log
	rm -f *.out
	rm -f *.run.xml
	rm -f *.4ct *.4tc *.idv *.lg *.tmp *.xdv *.xref

## clean-outputs	: Remove final output files only (PDF, HTML, CSS)
clean-outputs : 
	rm -f *.pdf *.css *.html

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
