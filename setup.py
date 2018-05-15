#!/usr/bin/env python

from distutils.core import setup

setup(name='Insurer_One_Python',
      version='1.0',
      description='Acts as the mock server for an insurance company, with accessible API for other applications',
      url='https://github.com/joey0589/SOA',
      packages=['eve', 'psycopg2', 'json']
     )