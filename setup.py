from distutils.core import setup

SHORT_DESC = '''A YAML reader that relaxes the syntax by allowing comments, inline comments,
and blank lines, among other things.'''


LONG_DESC = '''Extends the syntax of YAML files to accomodate things that an administrator
appreciates - comments inside a configuration file. Applies some additional sanity checks
to the data and fails verbosely, providing a detailed error message.'''

setup(
    name = 'reyaml',
    packages = ['reyaml'], # this must be the same as the name above
    version = '0.2',
    description=SHORT_DESC,
    long_description=LONG_DESC,
    description = 'Reader of humane YAML files',
    author = 'Alex Railean',
    author_email = 'ralienpp@gmail.com',
    url = 'https://github.com/ralienpp/reyaml',
    download_url = 'https://github.com/ralienpp/reyaml/tarball/0.2',
    keywords = ['yaml', 'parser', 'configuration', 'config'],
    license = 'BSD',
    classifiers = [
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Natural Language :: English',
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: BSD License'
      ],
    install_requires=[
        'PyYAML',
      ]
)
