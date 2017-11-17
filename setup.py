from setuptools import setup

setup(name='python_cmdtool',
      version='0.1.0',
      packages=['python_cmdtool'],
      entry_points={
          'console_scripts': [
              'cli = python_cmdtool.__main__:main'
          ]
      },
      )