from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

 
setup(name='pymakeplots',
       version='0.0.2',
       description='',
       url='https://github.com/TimothyADavis/pymakeplots',
       author='Timothy A. Davis',
       author_email='DavisT@cardiff.ac.uk',
       long_description=long_description,
       long_description_content_type="text/markdown",
       license='MIT',
       packages=['pymakeplots'],
       install_requires=[
           'numpy',
           'matplotlib',
           'scipy',
           'astropy',
       ],
       classifiers=[
         'Development Status :: 4 - Beta',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 3',
         'Operating System :: OS Independent',
       ],
       zip_safe=True)
       
