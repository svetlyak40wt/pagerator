from setuptools import setup, find_packages

setup(
    name = 'pagerator',
    version = '0.1.1',
    description = 'A helper to build iterables when you need to fetch results already divided into the pages.',
    author = 'Alexander Artemenko',
    author_email = 'svetlyak.40wt@gmail.com',
    keywords = 'helper utility',
    license = 'New BSD License',
    url = 'http://github.com/svetlyak40wt/pagerator/',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = find_packages(),
)
