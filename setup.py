from distutils.core import setup
import os, sys, glob

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name="Act-On-Place",
      scripts=['Act-On-Place'],
      version='0.1.0',
      maintainer="Juha Autero",
      maintainer_email="email@example.com",
      description="A PySide example",
      long_description=read('Act-On-Place.longdesc'),
      data_files=[('share/applications',['Act-On-Place.desktop']),
                  ('share/icons/hicolor/64x64/apps', ['Act-On-Place.png']),
                  ('share/Act-On-Place/qml', glob.glob('qml/*.qml')), ],)
