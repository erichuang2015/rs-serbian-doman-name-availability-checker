
# Author = "Zemundo"
# GitHub https://github.com/zemundo
# Version = 1.1

# .RS Domain Availability Checker


import whois
import colorama
from termcolor import *
colorama.init()
print(colored('Enter Domain Keyword without .RS extension', 'yellow'))
while True:
    # Comment in the beginning of the file

    tld = '.rs'

    domen = str(input('Search for a domain name: '))
    ceoDomen = str(domen+tld)

    podaciNiz = []
    slobodanIliZauzet = False

    def checkDomain():
        w = whois.whois(ceoDomen)
        podaciNiz.append(w)
        for s in podaciNiz:
            if(s.text == '%ERROR:103: Domain is not registered'):
                slobodanIliZauzet = True
                print(colored('Available!', 'green'))
            else:
                slobodanIliZauzet = False
                print(colored('Taken!', 'red'))

    checkDomain()
