#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='emharvest',
    version='0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    description='A system for parsing TFS EPU data structures',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kyle Morris',
    author_email='kyle.morris@diamond.ac.uk',
    url='https://github.com/kylelmorris/EMinsight',
    install_requires=[
        'glom',
        'tqdm',
        'pandas<2',
        'numpy<2',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'scipy',
        'xmltodict',
        'rich',
        'starparser',
        'mrcfile',
        'mmcif',
        'gemmi',
        'starfile',
        'pyem',
        'fpdf',
        'Pillow',
        'PyQt5',
        # Add any additional dependencies here
    ],
    python_requires='>=3.6', # Specify your Python version requirement
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        # More classifiers: https://pypi.org/classifiers/
    ],
    entry_points={
        'console_scripts': [
            'emharvest.harvest.py = emharvest.harvest_v0.2:main',
            'emharvest.py = emharvest.emharvest:main',
            'emharvest.print_atlas.py = emharvest.print_atlas:main',
            'emharvest.print_dataacquisition.py = emharvest.print_dataacquisition:main',
            'emharvest.print_screening.py = emharvest.print_screening:main',
            'emharvest.print_session.py = emharvest.print_session:main',
        ]
    }
)