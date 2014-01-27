#!/usr/bin/python3

import argparse
import iso3166

def main():

    parser = argparse.ArgumentParser()

    iso3166_alpha3_default = iso3166_alpha3_codes()
    parser.add_argument(
            '-c',
            '--countries',
            nargs='+',
            help='a comma separated list of ISO3166-alpha3 codes of the'\
                    ' country guides to generate. Defaults to the list of all'\
                    ' countries on the planet.',
            default = []
            )

    return

def iso3166_alpha3_codes():
    """
    returns a list of the iso3166 alpha3 codes for all the countries on the
    planet.
    """

    countries = isdo3166.countries
    codes = [ c['alpha3'] for c in countries ]
    return codes

if __name__ == '__main__':
    main()
