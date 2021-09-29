all : main.pdf main-apa.pdf

# Automatically generate the yearly .tex files from the .bib files
20%.tex : 20%.bib
	sed -nE '/^@/{s/^@.*\{(.*),/\\nocite\{\1\}/;p}' $< > $@

## main.pdf       : Generate PDF file with publications
main.pdf : 20*.bib 20*.tex main.tex
	pdflatex main.tex
	biber main
	pdflatex main.tex

main-apa.pdf : 20*.bib 20*.tex main-apa.tex
	pdflatex main-apa.tex
	biber main-apa
	pdflatex main-apa.tex

#main-apa.html : 20*.bib 20*.tex main-apa.tex main-apa.pdf
#	htlatex main-apa

## clean		: Remove generated files and start over
.PHONY : clean
clean :
	rm -f *.aux
	rm -f *.bbl
	rm -f *.bcf
	rm -f *.blg
	rm -f *.log
	rm -f *.out
	rm -f *.pdf
	rm -f *.run.xml
#	rm -f *.4ct *.4tc *.idv *.lg *.xref

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
