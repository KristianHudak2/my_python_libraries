from setuptools import setup, find_packages

setup(
    name='my_python_libraries',
    version='1.3.7',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    
)
