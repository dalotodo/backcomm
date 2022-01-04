from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["backtrader"]

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Backtrader Commission Library',
    url='https://github.com/dalotodo/backcomm',
    author='Pablo Perez',
    author_email='dalotodo69@gmail.com',
    # Needed to actually package something
    packages=find_packages(),
    # Needed for dependencies
    install_requires=requirements,
    # *strongly* suggested for sharing
    version='0.1.0',
    # The license can be anything you like
    license='MIT',
    description='This package provides commission utility classes to be used with backtrader',
    # We will also need a readme eventually (there will be a warning)
    long_description=readme,
    long_description_content_type='text/markdown'
)