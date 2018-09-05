from urllib.request import urlopen
from bs4 import BeautifulSoup
from weasyprint import HTML
import re


codes = [31681373, 9163407, 40077432, 989, 18165213, 46893386]

def main(codes):

    if len(codes) > 0:
        url = "http://www.stackprinter.com/export?format=HTML&service=stackoverflow&printer=false&question={}".format(codes[0])

        print(url)

        bs = BeautifulSoup(urlopen(url), 'lxml')
        title = bs.title.string.replace('/', ' or ')

        HTML(url).write_pdf("{}.pdf".format(title))
        return main(codes[1:])

    print("Printed all the pages...")

if __name__ == '__main__':
    main(codes)
