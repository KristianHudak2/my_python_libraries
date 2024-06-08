from setuptools import setup, find_packages

setup(
    name='libraries',
    version='1.0.4',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
)
