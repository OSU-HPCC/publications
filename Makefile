## pubs.md	: Create formatted list of publications
pubs.md : articles.csv generate_pubs.py citation.py
	./generate_pubs.py --articles articles.csv --output pubs.md
	./change_format.sh

## errors.md	: Check for errors in publication list
errors.md : articles.csv error_check.py citation.py
	./error_check.py --publist articles.csv

## clean		: Remove generated files and start over
.PHONY : clean
clean :
	rm -f pubs.md
	rm -f pubs.docx
	rm -f errors.md

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<
