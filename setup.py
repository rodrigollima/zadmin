import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zadmin",
    version="0.0.1",
    author="Rodrigo Lima",
    author_email="rodrigoxone@gmail.com",
    description="A small package to manage Zimbra SOAP Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigollima/zadmin",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
