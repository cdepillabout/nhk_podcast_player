#!/usr/bin/env python3

from distutils.core import setup

setup(name='nhk_podcast_player',
      version='1.0',
      description='automatically downloads nhk podcasts and plays them using mplayer',
      author='(cdep) illabout',
      author_email='cdep.illabout@gmail.com',
      #url='http://www.python.org/sigs/distutils-sig/',
      packages=['nhk_podcast_player'],
      package_dir={'nhk_podcast_player': 'src/nhk_podcast_player'},
      #package_data={'postured': ['sounds/bell17.wav']},
      scripts=['scripts/nhk-player'],
     )

