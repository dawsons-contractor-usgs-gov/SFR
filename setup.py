from setuptools import setup
import glob

setup(
    name='sfr',
    version='0.0.1',
    description='Processing codes for building sfr features ',
    url='http://github.com/usgs-bcb/SFR',
    author='Ben Gotthold',
    author_email='bcb@usgs.gov',
    license='unlicense',
    packages=['urb'],
    include_package_data=True,
    install_requires=[
        'gdal==3.0.1'
        'pyshp==2.1.0'
    ],
    zip_safe=False
)