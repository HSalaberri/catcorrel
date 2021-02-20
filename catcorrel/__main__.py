# -*- coding: utf-8 -*-

"""
usage: catcorrel [-h] -d DATA -o OUT_DIR

calculates categorical-correlation measures.

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  Path to dataset.
  -o OUT_DIR, --output OUT_DIR
                        Directory to store correlation-reports.
"""
import os
import logging
import argparse

from typing import List, Any

from catcorrel.correlation import CatCorrelator
from catcorrel.utils import prepare_F250, heatmap
from catcorrel.data.reader import load_csv

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def main(args: List[str]):
    """
    Main entry point that calculates categorical-correlation
    measures between the categories in a provided dataset.

    :param args:
    """
    log.info("Calculating categorical-correlations...")
    
    # Read and prepare data
    dpth = prepare_F250(args.data)
    #dpth = args.data
    
    # Load data
    data = load_csv(dpth)
    log.info(data)

    # Create CatCorrelator instance
    crlt = CatCorrelator()

    # Get number of features
    nft = data.shape[1]
    log.info(data.shape)

    # Calculate symmetric correlation with Cramer's V
    crmv_corr = crlt.measure(data, nft, "crmv")
    log.info(crmv_corr)
    
    # Calculate asymmetric correlation with Theil's U
    #thlv_corr = crlt.measure(data, nft, "thlv")
    #log.info(thlv_corr)

    # Create correlation-heatmaps 
    heatmap(crmv_corr, data, "YlGnBu", "Symmetric correlation through Cramer's V", os.path.join(args.out_dir, 'cramersv_old.png'))
    #heatmap(thlv_corr, data, "YlGnBu", "Asymmetric correlation through Theil's U", os.path.join(args.out_dir, 'theilsu_old.png'))
    
    # Create histograms


def parse_args() -> List[Any]:
    """
    Function that creates a new argument parser and parses arguments.
    """
    # Prepare parser with arguments
    parser = argparse.ArgumentParser(prog='catcorrel',
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
