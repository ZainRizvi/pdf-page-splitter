This script can be used to take any given file that's X pages long, and convert it to a file thats 2X pages long, where each page is the left and right halves of the original page

Usage:

`python pdfCropper.py {inputFile.pdf} {outputFile.pdf} [optional set of pages to skip]`
example: `python pdfCropper.py myScannedBook.pdf myParsedBook.pdf 0 2 5 6`