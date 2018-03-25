from setuptools import setup
from os import path

# Get the long description from the README file
with open(path.join(path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='pytest-easy-api',
    version='0.0.1',
    description='Simple API testing with pytest',
    long_description=long_description,
    url='https://github.com/thaffenden/pytest-easy-api',
    author='Tristan Haffenden',
    author_email="tristanehaffenden@gmail.com",
    packages=['pytest_easy_api'],
    install_requires=['requests'],
    tests_require=['pytest', 'flask', 'pytest-cov'],
)
