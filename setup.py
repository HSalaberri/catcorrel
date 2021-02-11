import setuptools

# Get project description from README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Establish setup parameters
setuptools.setup(name="ldsuite",
                 version="0.0-alpha.1",
                 author="Haritz Salaberri",
                 author_email="hsalaberri@gmail.com",
                 description="Collection of statistical tools for linguistic data science",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/HSalaberri/ldsuite",
                 packages=setuptools.find_packages(),
                 classifiers=["Programming Language :: Python :: 3",
                              "License :: OSI Approved :: Apache-2.0 License",
                              "Operating System :: OS Independent"],
                 python_requires='>=3.8.5')
