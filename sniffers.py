import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mikran_com.settings")

import urllib
from django.utils.timezone import utc
from xml.dom import minidom
from curr_conv.models import Rates

def nbp_sniffer():
    xmldoc = minidom.parse(urllib.urlopen('http://www.nbp.pl/kursy/xml/LastA.xml'))
    childs = xmldoc.childNodes[0]
    data = childs.getElementsByTagName('data_publikacji')[0].firstChild.nodeValue
    #print data
    nrtabeli = childs.getElementsByTagName('numer_tabeli')[0].firstChild.nodeValue 
    #print nrtabeli

    rates = childs.getElementsByTagName('pozycja')
    for rate in rates:
        r = Rates()
        r.created = data;
        r.base = 'PLN'
        r.supplier = nrtabeli
        kod = rate.getElementsByTagName('kod_waluty')[0].firstChild.nodeValue
        r.symbol=kod
        nazwa = rate.getElementsByTagName('nazwa_waluty')[0].firstChild.nodeValue
        r.name = nazwa
        przelicz = rate.getElementsByTagName('przelicznik')[0].firstChild.nodeValue
        r.unit = int(przelicz)
        average = rate.getElementsByTagName('kurs_sredni')[0].firstChild.nodeValue
        r.average = average.replace(',','.');

        #print kod,nazwa,przelicz,averageb

        r.spread='0.2'
        r.save()

nbp_sniffer()
