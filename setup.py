import setuptools
import os
import platform

with open("README.md", "r") as fh:
    long_description = fh.read()

print "I'm so trustfully!"
print platform.platform()
print platform.uname()
print platform.processor()

setuptools.setup(
    name="Trustfull",
    version="1.3.3.7",
    author="",
    author_email="no-sec-marko@example.com",
    description="Very conventional and trustful setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/no-sec-marko/lgtm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)
