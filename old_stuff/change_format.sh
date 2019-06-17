#!/bin/bash

# Name: change_format.sh
# Usage: If user has pandoc installed, the script
#        will convert publication list from
#        markdown format to docx format.

HAVEPANDOC=$(which pandoc)

if [ "$HAVEPANDOC" != "" ]
then
	pandoc pubs.md -o pubs.docx
fi
