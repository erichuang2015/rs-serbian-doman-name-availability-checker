
# Author = "Zemundo"
# GitHub https://github.com/zemundo
# Version = 1.2

# .RS Domain Availability Checker


import whois
import colorama
from termcolor import *
colorama.init()
print(colored('Enter Domain Keyword without .RS extension', 'yellow'))


tld = '.rs'


def checkDomain():
    w = whois.whois(domainWithTld)
    data.append(w)
    for s in data:
        if(s.text == '%ERROR:103: Domain is not registered'):
            print(colored('Available!', 'green'))
        else:
            print(colored('Taken!', 'red'))


while True:

    domen = str(input('Search for a domain name: '))
    domainWithTld = str(domen+tld)

    data = []

    checkDomain()
