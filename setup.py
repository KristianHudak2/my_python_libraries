from setuptools import setup, find_packages

setup(
    name='libraries',
    version='1.3.6',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
)
