import setuptools
from os import path
import dimorphite_dl

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="dimorphite_dl",
    version=dimorphite_dl.__version__,
    author="Patrick J. Ropp, Jesse C. Kaminsky, Sara Yablonski & Jacob D. Durrant",
    author_email="durrantj@pitt.edu",
    description="Dimorphite-DL: an open-source program for enumerating the ionization states of drug-like small molecules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Feriolet/dimorphite_dl",
    packages=find_packages(),
    package_data={
        "": ["*.smi", "*.smarts", "training_data/*.json"]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Chemistry"
    ],
    python_requires='>=3.6',
    extras_require={
        'rdkit': ['rdkit>=2017.09'],
    },
    entry_points={'console_scripts':
                      ['dimorphite_dl = dimorphite_dl.run_dock:main']}
)
