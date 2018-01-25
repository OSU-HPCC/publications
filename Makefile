## pubs		: Create formatted list of publications
pubs.md : articles.csv generate_pubs.py citation.py
	./generate_pubs.py --articles articles.csv --output pubs.md
	./change_format.sh

## clean		: Remove generated files and start over.
.PHONY : clean
clean :
	rm -f *.md
	rm -f *.docx

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
