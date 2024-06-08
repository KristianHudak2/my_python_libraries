from setuptools import setup, find_packages

setup(
    name='libraries',
    version='1.3.2',
    packages=find_packages(where='src/libraries'),
    package_dir={'': 'src/libraries'},
    
)
