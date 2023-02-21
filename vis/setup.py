# from distutils.core import setup
from setuptools import find_packages, setup
import pathlib

setup(
    # Application name:
    name="kg-vis",
    
    # Version number (initial):
    version="0.0.1",
    
    # Application author details:
    author="Zhang",
    author_email="oo@zju.edu.cn",
    
    # Packages
    packages=["kg_vis"],

    package_dir={'kg_vis.templates': 'kg_vis/templates', 'kg_vis.static': 'kg_vis/static'},
    
    # Include additional files into the package
    include_package_data=True,
    
    # Details
    url="http://pypi.python.org/pypi/kg_vis/",
    
    #
    license="LICENSE.txt",
    description="A Knowledge Graph GUI based on Flask.",
    
    long_description_content_type='text/markdown',
    long_description= open('README.md').read(),

    # Dependent packages (distributions)
    install_requires=[
        "flask",
        "flaskwebgui",
        "openpyxl",
    ],
)

# To Build and Publish (for developer only), 
# Run: python setup.py sdist bdist_wheel; twine upload dist/*