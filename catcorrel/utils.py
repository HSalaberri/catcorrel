import re
import logging
import numpy as np
import pandas as pd
import random as rnd
import seaborn as sns
import matplotlib.pyplot as plt

from typing import Dict, List

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def heatmap(cm: np.ndarray, data: pd.DataFrame,
            clr: str, title: str, spth: str):
    """
    This function creates a heatmap for the
    given data and its correlation measures.

    :param cm:
    :param data:
    :param clr:
    :param title:
    :param spth:
    """
    # Set seaborn
    sns.set()
    plt.subplots(figsize=(10, 7))

    # Create heatmap
    sns.heatmap(cm, vmin=0, vmax=1, annot=True, fmt="g",
                xticklabels=data.columns, yticklabels=data.columns,
                linewidths=.5, cmap=clr)
    plt.title(title, size=12)
    plt.tight_layout()

    # Save
    fig = plt.gcf()
    fig.savefig(spth, dpi=150)

    # Flush
    plt.cla()


def histogram(data: pd.DataFrame, spth: str,
              title: str, xdesc: str, clr: str):
    """
    This function creates an histogram for the given data.

    :param data:
    :param spth:
    :param title:
    :param xdesc:
    :param clr:
    """
    # Get data
    cts, vls = np.unique(data, return_counts=True)

    # Create plot
    x_locs = np.arange(len(vls))

    plt.bar(x_locs, vls, align='center', color=clr)
    plt.xticks(x_locs, cts)
    plt.title(title, size=14)
    plt.xlabel(xdesc, size=12)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel('Counts', size=12)
    plt.tight_layout()

    # Save
    fig = plt.gcf()
    fig.savefig(spth, dpi=150)

    # Flush
    plt.cla()


def shuffle(dpth: str, header:str) -> str:
    """
    This function randomizes a given file by shuffling its lines.
    
    :param dpth:
    :param header:
    """
    # Read and shuffle lines    
    with open(dpth, mode="r", encoding="utf-8") as rdf:
        
        # Get lines and remove header
        lines = list(rdf)
        lines.remove(header)
    
    # Shuffle randomly
    rnd.shuffle(lines)

    # Get shuffled save-path
    dpth = re.sub('\.csv$', '', dpth)
    dpth_rnd = dpth + '_rnd.csv'

    # Save shuffled data
    with open(dpth_rnd, mode="w", encoding="utf-8") as fh:
        
        # Write header and then data-points
        fh.write(header.decode('utf-8'))
        fh.writelines(lines)

    return dpth_rnd


def prepare_F250(fpth: str) -> str:
    """
    This function prepares the F250 dataset
    for categorical correlation measuring.

    :param fpth:
    """
    prl = []
    
    # Store attribute-values for QA
    atrs = [{} for _ in range(8)]

    # Read all lines at once
    with open(fpth, 'r') as fh:
        lines = fh.readlines()
        
    # Got lines
    if lines:
        
        # Process every line but header-line
        for line in lines[1:]:

            # Prepare line and account for its attributes
            pline = prepare_F250Inst(line, atrs)
            prl.append(pline)

    else:
        raise Exception(f"No lines read from \"{fpth}\".")
    
    # Log for QA
    [log.info(atr) for atr in atrs]
    
    # Write prepared F250
    ppth = fpth.replace('.csv', '_prep.csv')
    
    with open(ppth, 'w') as fhw:
        
        # Write cooked header and prepared lines
        fhw.write(lines[0].replace('LANG_NAME;', '').replace('SOURCE;', ''))
        fhw.writelines("\n".join(prl))
        
    return ppth


def prepare_F250Inst(dp: str, atrs: List[Dict[str, int]]) -> str:
    """
    This function prepares a given instance from the F250 dataset.
    
    :param dp:
    :param atrs:
    """
    # Split
    lpts = dp.strip().split(';')
            
    # QA
    if len(lpts) == 8:
        
        # Prepare-consider every attribute
        pline = ""

        for idx, lpt in enumerate(lpts):
                    
            # Prepare
            lptr = lpt.lower().replace(',', '').replace('/', '')
                    
            # Store for QA
            if lptr not in atrs[idx]:
                atrs[idx][lptr] = 1
                    
            else:
                atrs[idx][lptr] = atrs[idx][lptr] + 1
            
            # Don't consider LANG_NAME and SOURCE
            if (idx != 1) and (idx != 4):
                
                # Concatenate prepared value
                if pline == "":
                    pline = lptr
                else:
                    pline = pline + ";" + lptr

        # return processed line
        return pline

    else:
        raise Exception(f"Incorrect attributes in line: \"{dp}\".")
