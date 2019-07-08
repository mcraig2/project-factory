""" Template script to process the data.

Usage:
    process_data.py --input=<str> --output=<str>
    process_data.py -h --help

"""

from docopt import docopt
import pandas as pd


def read_data(fname):
    """ Read in the data.

        :param fname: the filename to read in

        :return: the output as a DataFrame """
    return pd.DataFrame({{'a': 1}})


def process_data(df):
    """ Process the data that was just read in from CSV

        :param df: the raw unprocessed data

        :return: an output DataFrame that is processed. """
    return df


if __name__ == '__main__':
    ARGS = docopt(__doc__, version='1.0')
    (read_data(fname=ARGS['--input'])
     .pipe(process_data)
     .to_csv(ARGS['--output'], index=False))
