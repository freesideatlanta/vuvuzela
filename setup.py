#!/usr/bin/env python
# we would like this to be the script that builds and deploys vuvuzela to tammy
# http://docs.python.org/distutils/setupscript.html

from distutils.core import setup

setup(  name='vuvuzela',
        version='0.1',
        package_dir={'vuvuzela': ''},
        packages=['vuvuzela'],
    )
