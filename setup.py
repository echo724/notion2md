from setuptools import find_packages, setup
import setuptools
import io
# Read in the README for the long description on PyPI
with io.open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()
setup(
      name='notion2md',
      version='1.0.0',
      description='Export notion page to markdown.',
      long_description=readme,
      long_description_content_type="text/markdown",
      url='https://github.com/echo724/notion2md.git',
      author='Eunchan Cho',
      author_email='eunchan1001@gmail.com',
      license='MIT',
      install_requires=[
        'notion>=0.0.25',
        'requests>=2.22.0',
      ],
      packages=setuptools.find_packages(),
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3.7',
          ],
)
