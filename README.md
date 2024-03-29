# CatCorrelator :moyai:: A basic collection of statistical tools for measuring categorical correlation

One of the key factors when statistically analyzing variables is their type or nature, namely, variables can exhibit a _continuous_ or _discrete_ behaviour; the later are also frequently referred to as _nominal_ or _categorical_ parameters in statistical literature. As a result of such a distinction, there are, in general terms, three types of parameter-pairs that can be addressed when, for instance, trying to compute variable-correlation: those between categorical variables, those between discrete variables and those with mixed types. It is of utmost importance to point out that each of the contexts will require from a tailored set of statistical techniques.

<p></p>
	
For measuring the correlation of continuous variables _Pearson's Correlation_ [1] is typically used and for mixed types, on the other hand, _Logistic Regression_ [2] or an adaptation of Pearson's Correlation by the name of _Point Biserial Correlation_ [3] can be applied.

<p></p>

In what concerns this project, however, all of the considered data-variables so far exhibit a nominal behaviour; therefore, correlation has been quantified by means of __Cramer's V__ [4] which is a correlation-technique based on _Pearson's chi-squared_ statistic [5] and also sometimes referred to as _Cramer's phi_. In addition, and given the symmetric nature of Crammer's V and the limited size of the corpus, __Theil's U__ (also known as the _Uncertainty Coefficient_) [6] has also been computed over the set of considered parameters in order to get a clearer and non-symmetric view of the parameter correlations without 'loosing' any instances to symmetry.

<p></p>

It is also worth mentioning that there are two major ways in which correlation between discrete variables can be calculated, by so-called _Distance Metrics_ (DM) such as the _Manhattan_ and the _Canberra_ distances [7, 8] and by means of _Contingency Table Analytics (CTA)_ such as the ones implemented in Cramer's V and Theil's U. The decision of using CTA techniques to conduct the statistical analysis in this research has been motivated by the fact that one of the biggest drawbacks of DM techniques is their strong sensitivity to input scale adaptations, making it hard to correctly compare correlation factors across several iterations of corpus extensions. In addition, DMs are also said to be not easily comparable when correlating variable pairs which can take different numbers of categories.

### Installation in VirtualEnv

The development and testing has been conducted under Python version 3.8.5. 

##### 1. Download Project and Unzip:

```bash
unzip catcorrel.zip
cd catcorrel/
```

##### 2. Install VirtualEnv and Pip (UNIX):

```bash
apt-get install python3-venv
apt install python3-pip
```

##### 3. Create VirtualEnv, Activate and Install Requirements:

```bash
python3 -m venv virtual_environment
source virtual_environment/bin/activate
pip3 install -r requirements.txt
```

##### 3. Run setup.py and install package

```bash
python3 setup.py sdist bdist_wheel
pip3 install catcorrel-x.x.x-py3-none-any.whl
```

##### 4. Deactivate VirtualEnv after Running, See "User Interface":

```bash
deactivate
```

### User Interface

```bash
usage: catcorrel [-h] -d DATA -o OUT_DIR

calculates categorical-correlation measures.

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  Path to dataset.
  -o OUT_DIR, --output OUT_DIR
                        Directory to store correlation-reports.
```

### Examples

##### 1. Measure correlation:
```bash
python3 -m catcorrel -d data/dataset.csv -o reports/
```

### Testing
```bash
pytest -s tests/
```

### Version - Release

<p>Current release of CatCorrelator is v0.0-alpha.1 [2021.02.x]. It supports both symmetric and asymmetric correlation measures. Future versions will include additional techniques.</p>

### Author and Support
CatCorrelator :moyai: has been developed by Haritz Salaberri. For any related questions please refer to [Haritz](mailto:hsalaberri@gmail.com).

### References

<p>[1]: Pearson, K. "Notes on Regression and Inheritance in the Case of Two Parents Proceedings of the Royal Society of London, 58, 240-242." (1895).</p>
<p>[2]: Wright, Raymond E. "Logistic regression." (1995).</p>
<p>[3]: Tate, Robert F. "Correlation between a discrete and a continuous variable. Point-biserial correlation." The Annals of mathematical statistics 25.3 (1954): 603-607.</p>
<p>[4]: Cramer, Harold. "Mathematical methods of statistics, Princeton Univ." Press, Princeton, NJ (1946).</p>
<p>[5]: Pearson, Karl. "X. On the criterion that a given system of deviations from the probable in the case of a correlated system of variables is such that it can be reasonably supposed to have arisen from random sampling." The London, Edinburgh, and Dublin Philosophical Magazine and Journal of Science 50.302 (1900): 157-175.</p>
<p>[6]: Theil, H. "Applied Economic Forecasting, Rand McNally and Company." (1966).</p>
<p>[7]: Black, P. E. "Dictionary of Algorithms and Data Structures, chapter Manhattan distance. US National Institute of Standards and Technology, 2006."</p>
<p>[8]: Lance, Godfrey N., and William T. Williams. "Mixed-Data Classificatory Programs I - Agglomerative Systems." Australian Computer Journal 1.1 (1967): 15-20.</p>

### License
Apache-2.0 License
