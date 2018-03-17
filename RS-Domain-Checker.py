

# Author = "Zemundo"
# GitHub https://github.com/zemundo
# Version = 1.3

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

            print(colored('{} is Available!'.format(domainWithTld), 'green'))
        else:

            print(colored('{} is Taken!'.format(domainWithTld), 'red'))


while True:

    domen = str(input('Search for a domain name: '))
    domainWithTld = str(domen+tld)

    data = []

    checkDomain()
