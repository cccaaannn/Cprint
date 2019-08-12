from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
     name='extprint',  
     version='0.2',
     scripts=['extprint'] ,
     author="Can Kurt",
     author_email="can.kurt.aa@gmail.com",
     description="prints stuff",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/cccaaannn/extprint",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )