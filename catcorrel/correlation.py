import math
import logging
import numpy as np
import pandas as pd
import scipy.stats as ss

from collections import Counter

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class CatCorrelator:
    """
    Component that calculates categorical-correlation measures.

    Methods
    -------
        measure(self, data: pd.DataFrame, nft: int, mkey: str) -> np.ndarray
            Instance-method that calculates categorical correlation measures.

        cramersv(x:pd.Series, y:pd.Series) -> float
            Static-method that calculates Cramer's V

        theilsu(cls, x:pd.Series, y:pd.Series) -> float
            Class-method that calculates Theil's U

        centropy(x:pd.Series, y:pd.Series) -> float
            Static-method that calculates conditional entropy
    """
    def measure(self, data: pd.DataFrame, nft: int, mkey: str) -> np.ndarray:
        """
        This instance-method calculates the categorical correlation
        measures based on the indicated approach.

        Currently supported approaches are "mkey=crmv" for Cramer's V
        (symmetric correlation) and "mkey=thlv" for Theil's U
        (asymmetric correlation).

        https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_V
        https://en.wikipedia.org/wiki/Uncertainty_coefficient

        :param data:
        :param nft:
        :param mkey:
        """
        # Initialize correlation matrix
        corr = np.zeros((nft, nft))

        # Calculate measure for every combination of categories
        for idx0, cat0 in enumerate(data.columns):
            for idx1, cat1 in enumerate(data.columns):

                # Convert to Pandas Series for performance reasons
                y = pd.Series(data[cat0])
                x = pd.Series(data[cat1])

                # Use Cramer's V
                if mkey == "crmv":
                    corr[idx0][idx1] = round(self.cramersv(x, y), 2)

                # Use Theil's U instead
                elif mkey == "thlv":
                    corr[idx0][idx1] = round(self.theilsu(x, y), 2)

                # Will not calculate correlations
                else:
                    log.info(f"Key \"{mkey}\" is not recognized.")

        # Return correlation-measures matrix
        return corr

    @staticmethod
    def cramersv(x: pd.Series, y: pd.Series) -> float:
        """
        Static-method that calculates Cramer's V
        for category-to-category association.

        This implementation uses the correction technique proposed by:
        Bergsma, Wicher. "A bias-correction for Cramér’s V and Tschuprow’s T."
        Journal of the Korean Statistical Society 42, no. 3 (2013): 323-328.

        :param x:
        :param y:
        """
        # Initialize correlation matrix
        cm = pd.crosstab(x, y)

        # Calculate Chi and Phi coefficients
        chi2 = ss.chi2_contingency(cm)[0]
        n = cm.sum().sum()
        phi2 = chi2/n
        r, k = cm.shape

        phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
        rcorr = r-((r-1)**2)/(n-1)
        kcorr = k-((k-1)**2)/(n-1)

        return np.sqrt(phi2corr/min((kcorr-1), (rcorr-1)))

    @classmethod
    def theilsu(cls, x: pd.Series, y: pd.Series) -> float:
        """
        Class-method that calculates Theil's U, AKA the
        uncertainty coefficient for category-to-category association.

        :param cls:
        :param x:
        :param y:
        """
        # Compute conditional entropy
        s_xy = cls.centropy(x, y)
        x_ctr = Counter(x)

        # Calculate total occurrences
        tocr = sum(x_ctr.values())

        # Calculate coefficients
        p_x = list(map(lambda n: n/tocr, x_ctr.values()))
        s_x = ss.entropy(p_x)

        # Decide on final value
        if s_x == 0:
            return 1

        else:
            return (s_x - s_xy)/s_x

    @staticmethod
    def centropy(x: pd.Series, y: pd.Series) -> float:
        """
        Static-method that calculates the
        conditional entropy of x given y: S(x|y)

        https://en.wikipedia.org/wiki/Conditional_entropy

        :param x:
        :param y:
        """
        # Create counters
        y_ctr = Counter(y)
        xy_ctr = Counter(list(zip(x, y)))

        # Calculate total occurrences
        tocr = sum(y_ctr.values())

        # Initialize conditional entropy
        entropy = 0.0

        # Consider every entry
        for entry in xy_ctr.keys():

            # Calculate probabilities
            p_xy = xy_ctr[entry]/tocr
            p_y = y_ctr[entry[1]]/tocr

            # Update entropy value
            entropy += p_xy * math.log(p_y/p_xy)

        return entropy
