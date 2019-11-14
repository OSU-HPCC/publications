## main.pdf       : Generate PDF file with publications
main.pdf : *.bib *.tex
	pdflatex main.tex
	biber main
	pdflatex main.tex

## clean		: Remove generated files and start over
.PHONY : clean
clean :
	rm -f *.aux
	rm -f *.bbl
	rm -f *.bcf
	rm -f *.blg
	rm -f *.log
	rm -f *.pdf
	rm -f *.run.xml

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
