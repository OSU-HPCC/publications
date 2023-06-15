# Updating the Publications List on the HPCC Web Page


## Make HTML version of the publications list.

Create `main-apa-html.tex` by copying `main-apa.tex` and commenting out 
the babel package.

Run `htxelatex main-apa-html` followed by `biber main-apa-html` followed
by `htxelatex main-apa-html` (again).

The html generation has been added to the makefile, so all that is 
necessary to keep this going is to update each corresponding `-html.tex`
file with the other tex files when adding each new publication year.

## Copy Publication Data to the Web Page

The publications page `publications.pcf` is configured so that all of
the publication data is stored in two separate assets: 

1. publications-latex-css
1. publications-latex-html

To update the publication data, it is only necessary to update these assets.

Check out each asset; edit using the source code option.

For the CSS asset, copy the code between the lines `/* start css.sty */`
and `/* end css.sty */` from `main-apa-html.css` and use this code to 
replace everything between the corresponding lines in the 
`publications-latex-css` asset. (There is additional code in the CSS asset
that should *not* be replaced.)

For the HTML asset, copy the code from `main-apa-html.html` starting with 
the first `a` element after the date and ending with the final closing `dl`
element (which should be the last thing before the closing `body` tag. Use
the copied code to replace the *entire* source content of the 
`publications-latex-html` asset.

Check each asset back in and make sure the publications page shows the updates.


