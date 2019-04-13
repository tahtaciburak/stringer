import argparse
import sys
import re

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('infile',
                        default=sys.stdin,
                        type=argparse.FileType('r'),
                        nargs='?')

    args = parser.parse_args()
    data = args.infile.read()
    string = data.replace("\n","")
    regex_set = {
        "AKIA[0-9A-Z]{16}":"AWS ClientID",
        "[0-9a-zA-Z/+]{40}":"AWS Secret Key",
        "[0-9a-zA-Z_]{5,31}":"Bitly ClientID",
        "R_[0-9a-f]{32}":"Bitly Secret Key",
        "[0-9]{13,17}":"Facebook ClientID",
        "[0-9a-f]{32}":"Facebook Secret Key",
        "[0-9a-f]{32}":"Flicker ClientID",
        "[0-9a-f]{16}":"Flicker Secret Key",
        "[0-9A-Z]{48}":"Foursquare ClientID",
        "[0-9A-Z]{48}":"Foursquare Secret Key",
        "[0-9a-z]{12}":"LinkedIn ClientID",
        "[0-9a-zA-Z]{16}":"LinkedIn Secret Key",
        "[0-9a-zA-Z]{18,25}":"Twitter ClientID",
        "[0-9a-zA-Z]{35,44}":"Twitter Secret Key"
    }

    for rgx in regex_set:
        if len(re.findall(rgx,string)) > 0:
            print(string," ==> ",regex_set[rgx])

if __name__ == '__main__':
    main()