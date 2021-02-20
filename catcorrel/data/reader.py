import pandas as pd


def load_csv(fpth: str) -> pd.DataFrame:
    """
    This function loads a given CSV data-file into a Pandas DataFrame.

    :param fpth:
    """
    return pd.read_csv(fpth, sep=';')
    #return pd.read_csv(fpth)