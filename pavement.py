from paver.easy import *
import paver.doctools
import os
import glob
import shutil
import sys

@task
def setup():
  sh('python -m pip install coverage')
  sh('python -m pip install nose')
  sh('python -m pip install radon==4.3.2')
  pass

@task
def test():
  sh('python -m nose --with-coverage --cover-erase --cover-branches --cover-html --cover-package=src test')
  pass

@task
def clean():
  for pycfile in glob.glob("*/*/*.pyc"):
    os.remove(pycfile)
  for pycache in glob.glob("*/__pycache__"):
    os.removedirs(pycache)
  for pycache in glob.glob("./__pycache__"):
    shutil.rmtree(pycache)
  for pycfile in glob.glob("radon.report"):
    os.remove(pycfile)
  try:
    shutil.rmtree(os.getcwd() + "/cover")
  except:
    pass
  pass

@task
def radon():
  sh('python -m radon cc src -a -nb')
  sh('python -m radon cc src -a -nb > radon.report')
  if (os.stat("radon.report").st_size != 0):
    raise Exception('radon found complex code')

@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
  pass