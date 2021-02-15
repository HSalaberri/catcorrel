import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


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
