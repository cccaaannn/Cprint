import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extprint",
    version="0.0.7",
    author="Can Kurt",
    author_email="can.kurt.aa@gmail.com",
    description="extended print",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cccaaannn/extprint",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)