from urllib.request import urlopen
from bs4 import BeautifulSoup
from weasyprint import HTML
import re

# Codes from the article links need to be added here
codes = [31681373, 9163407, 40077432, 18165213, 46893386]

def main(codes):
    """Prints stackoverflow posts based on their code.

    1. Takes the code list
    2. Calls the stackprinter api with the first code
    3. Parses the print-friendly page
    4. Prints it into pdf
    5. Repeats until there are not codes left.
    """
    if len(codes) > 0:
        url = "http://www.stackprinter.com/export?format=HTML&service=stackoverflow&printer=false&question={}".format(codes[0])


        bs = BeautifulSoup(urlopen(url), 'lxml')
        title = bs.title.string.replace('/', ' or ')

        print("\n" + title + "\n" + url)

        HTML(url).write_pdf("{}.pdf".format(title))
        return main(codes[1:])

    print("\nPrinted all the pages...")

if __name__ == '__main__':
    main(codes)
