# so2pdf
Script to create pdf from stackoverflow posts based on their codes. It works by calling the API of http://stackprinter.com which renders a print-friendly form of the post. This is useful if you like to read the posts offline or you want to archive them.

Currently it does not support the other stack excange pages.

## Required libraries
- urllib
- bs4
- weasyprint
- re

## Usage
1. Get the codes of the posts from their url. For instance, in the following url, https://stackoverflow.com/questions/31681373/making-svm-run-faster-in-python, the code you need is the number after '/questions/': '31681373'.
2. Insert the codes into the `codes` list within the script.
3. Run the script
    1. From terminal: `python path-to-so2pdf/so2pdf.py`
    1. From python: `run path-to-so2pdf/so2pdf.py`
4. It will generate the pdfs into the folder from which you run it.
