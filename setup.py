from setuptools import setup, find_packages

setup(
    name='libraries',
    version='0.3.7',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
)
