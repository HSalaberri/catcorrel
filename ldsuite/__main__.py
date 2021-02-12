# -*- coding: utf-8 -*-

"""

"""
import os
import logging
import argparse

from typing import List, Any

from ldsuite.correlation import CatCorrelator

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main(args: List[str]):
    """
    Main entry point that calculates categorical-correlation
    measures between the categories in a provided dataset.

    :param args:
    """
    log.info("Calculating categorical-correlations...")

    # Create CatCorrelator instance
    crlt = CatCorrelator()

    # Calculate symmetric correlation with Cramer's V
    crlt.cramer(args.data, os.path.join(args.out_dir, 'cramers_v.jpg'), args.prt)
    
    # Calculate asymmetric correlation with Theil's U
    crlt.theil(args.data, os.path.join(args.out_dir, 'theils_u.jpg'), args.prt)
    

def parse_args() -> List[Any]:
    """
    Function that creates a new argument parser and parses arguments.
    """
    # Prepare parser with arguments
    parser = argparse.ArgumentParser(prog='ldsuite',
                                     description='calculates categorical-' +
                                                 'correlation measures.')

    parser.add_argument('-d', '--data',
                        dest='data',
                        type=str,
                        help='Path to dataset.',
                        required=True)
    
    parser.add_argument('-o', '--output',
                        dest='out_dir',
                        type=str,
                        help='Directory to store correlation-reports.',
                        required=True)

    # Parse arguments and return
    return parser.parse_args()


if __name__ == '__main__':

    # Get input args and run
    main(parse_args())
