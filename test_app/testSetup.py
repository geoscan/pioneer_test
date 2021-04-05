# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('testPioneer.py')]

setup(name='testPionner',
      version='0.0.1',
      description='test',
      executables=executables)