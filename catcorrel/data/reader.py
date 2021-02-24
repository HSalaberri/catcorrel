import pandas as pd


def load_csv(fpth: str, sep: str) -> pd.DataFrame:
    """
    This function loads a given CSV data-file into a Pandas DataFrame.

    :param fpth:
    :param sep:
    """
    return pd.read_csv(fpth, sep=sep)
