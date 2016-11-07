#!/usr/bin/env python

# AS to IP Lookup

# On first run, it'll download the latest ASN data (updated hourly) from https://iptoasn.com/data/ip2asn-v4.tsv.gz
# To get the freshest ASN data, delete your local copy of ip2asn-v4.tsv.gz and re-run the script.
# AS argument should not contain any spaces.

# Usage examples:
# python asnlookup.py microsoft
# python asnlookup.py 205.198.42
# python asnlookup.py 223.74.50
# python asnlookup.py google

# author: @_0rbz (Fabrizio Siciliano)

import requests
import gzip
import sys
import os

class color:
    g = '\033[92m'
    b = '\033[0m'

if len(sys.argv) != 2:
    print 'Usage: python %s [ASN-NAME]' % sys.argv[0]
    exit()

as_name = sys.argv[1]
as_db = "https://iptoasn.com/data/ip2asn-v4.tsv.gz"
as_db_name = "ip2asn-v4.tsv.gz"

if os.path.isfile(as_db_name):

    f = gzip.open(as_db_name, "rb")
    search = f.readlines()
    f.close()

    for x, line in enumerate(search):
        if as_name.lower() in line.lower():
            for line in search[x:x+1]: print color.g + line + color.b,

else:

    with open(as_db_name, "wb") as f:
        print "Downloading latest ASN Data [%s]..." % as_db_name
        response = requests.get(as_db, stream=True)
        length = response.headers.get('content-length')
        if length is None:
            f.write(response.content)
        else:
            datax = 0
            length = int(length)
            for data in response.iter_content(chunk_size=4096):
                datax += len(data)
                f.write(data)
                end = int(42 * datax / length)
                sys.stdout.write("\r|%s%s|" % ('=' * end, ' ' * (42-end)) )
                sys.stdout.flush()

    f = gzip.open(as_db_name, "rb")
    search = f.readlines()
    f.close()

    for x, line in enumerate(search):
        if as_name.lower() in line.lower():
            for line in search[x:x+1]: print color.g + line + color.b,
