# aslookup

AS to IP Lookup

On first run, it'll download the latest AS data (updated hourly) from https://iptoasn.com/data/ip2asn-v4.tsv.gz
To get the freshest AS data, delete your local copy of ip2asn-v4.tsv.gz and re-run the script.
AS argument should not contain any spaces.

Usage examples:
- python aslookup.py microsoft
- python aslookup.py 205.198.42
- python aslookup.py 223.74.50
- python aslookup.py google
