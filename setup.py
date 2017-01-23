"""
Bot written in Python for Sushi Go Round Web Games
Link: http://www.miniclip.com/games/sushi-go-round/en/

Test Environment:
OS: Windows 7
Browser: Chrome
Screen Resolution: 1920 x 1080

"""

classifiers = """\
Development Status : Beta
Intended Audience : Developers
License : -
Programming Language : Python
Operating System : Microsoft Windows
"""

from distutils.core import setup, Extension
import py2exe

libs = ['user32']
doclines = __doc__.split('\n')

setup(name='SuShiBot',
      version='0.09b',
      author='Jason Lim',
      author_email='',
      url='',
      download_url='',
      license='',
      platforms=['Win32'],
      description = doclines[1],
      classifiers = filter(None, classifiers.split('\n')),
      long_description = ' '.join(doclines[2:]),
      console=['sushi.py']
      )
