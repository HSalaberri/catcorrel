import logging
import numpy as np
import pandas as pd
import scipy.stats as ss

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class CatCorrelator:
    """
    Component that calculates categorical-correlation measures.
    
    Methods
    -------
        measure(self, data: pd.DataFrame, nft: int, mkey: str) -> np.ndarray
            Instance-method that calculates categorical correlation measures.
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
    def cramersv(x:pd.Series, y:pd.Series) -> float:
        """
        Static-method calculates Cramer's V
        for category-to-category association.
        
        This implementation uses the correction technique proposed by:
        Bergsma, Wicher. "A bias-correction for Cramér’s V and Tschuprow’s T."
        Journal of the Korean Statistical Society 42, no. 3 (2013): 323-328.

        :param x:
        :param y:
        """
        # Initialize correlation matrix
        cm = pd.crosstab(x,y)
        
        # Calculate Chi and Phi coefficients
        chi2 = ss.chi2_contingency(cm)[0]
        n = cm.sum().sum()
        phi2 = chi2/n
        r,k = cm.shape
        phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
        rcorr = r-((r-1)**2)/(n-1)
        kcorr = k-((k-1)**2)/(n-1)
        
        return np.sqrt(phi2corr/min((kcorr-1),(rcorr-1)))


