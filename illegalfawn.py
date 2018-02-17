# python 2.7

import re
import urllib2

print """https://github.com/notnop presents:
illegalFawn scrapper
"""


def get_data(adresa_web):
    download_agent = {'User-Agent': "illegalFawn - scrapper"}

    req = urllib2.Request(adresa_web, None, download_agent)
    content = urllib2.urlopen(req).read()
    return content


# get pastebin addresses
illegalfawn = []
print "#\t Connecting to illegalfawn..."

data = get_data("https://twitter.com/illegalFawn")

print "#\t Searching for pastes..."
for j in data.split():
    el_buscador = re.search('https://pastebin\.com/raw/(.){8}', j)
    if el_buscador:
        illegalfawn.append(el_buscador.group())

latest = illegalfawn[0]

raw_phish = get_data(latest).split()

# create file name
f_name = re.sub("/", "_", raw_phish[1]) + ".txt"

print "#\t Write phishing to %s..." % f_name

with open(f_name, "w") as handle:
    for i in raw_phish[3:]:
        handle.write(i + "\n")
    handle.close()

print "#\t See ya next time."
 