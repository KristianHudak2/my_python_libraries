from setuptools import setup, find_packages

setup(
    name='libraries',
    version='1.3.5',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
)
