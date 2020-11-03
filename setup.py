from setuptools import setup

with open('README.md', "r") as fh:
    long_description = fh.read()

setup(name='easy-mhi',
      version='1.3',
      description='Simple library that can be used to generate motion history images from video frames',
      py_modules=['mhi'],
      package_dir={'': 'src'},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      long_description=long_description,
      long_description_content_type="text/markdown",
      install_requires=[
          "Pillow ~= 8.0"
      ],
      url="https://github.com/larrett/mhi",
      project_urls={
          'Bug Reports': 'https://github.com/larrett/mhi/issues',
      },
      )
