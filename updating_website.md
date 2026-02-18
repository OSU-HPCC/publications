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

The `Publications` page (id:10064) is configured so that all of
the publication data is stored in two separate assets under the
`_shared_content` directory: 

1. 311427 (id:12155) -- CSS
1. 311428 (id:21256) -- HTML

To update the publication data, it is only necessary to update these assets.

Acquire editing locks on each asset; edit using the "raw code" option.

For the CSS asset, copy the code between the lines `/* start css.sty */`
and `/* end css.sty */` from `main-apa-html.css`; use this code to 
replace everything between the corresponding lines in the CSS asset. 
(There is additional code in the CSS asset that should *not* be replaced.)

For the HTML asset, copy the code from `main-apa-html.html` starting with 
the first `a` element after the date and ending with the final closing `dl`
element (which should be the last thing before the closing `body` tag. Use
the copied code to replace the *entire* source content of the HTML asset.

Save changes and release the editing locks when done. Refresh the 
publications page and make sure it shows the updates.


