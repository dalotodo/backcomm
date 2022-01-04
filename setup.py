from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Backtrader Commission Library',
    url='https://github.com/dalotodo/backcomm',
    author='Pablo Perez',
    author_email='dalotodo69@gmail.com',
    # Needed to actually package something
    packages=['backcomm'],
    # Needed for dependencies
    install_requires=['backtrader'],
    # *strongly* suggested for sharing
    version='0.1.0',
    # The license can be anything you like
    license='MIT',
    description='This package provides commission utility classes to be used with backtrader',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read_text(),
    long_description_content_type='text/markdown'
)