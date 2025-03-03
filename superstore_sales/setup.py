# setup.py

from setuptools import setup, find_packages

setup(
    name='superstore_sales',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
    ],
    author='Josue Gomez Parada',
    author_email='josue.gomez.parada@gmail.com',
    description='A project to analyze and clean SuperStore Sales data',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jgp-13/superstore_sales',  # GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)