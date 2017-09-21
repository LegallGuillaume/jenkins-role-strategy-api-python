from setuptools import setup, find_packages

version = __import__('pyjars').__version__

setup(
    name='pyjars',
    version=version,
    author='Guillaume Le Gall',
    author_email='glegall@wyplay.com',
    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)
