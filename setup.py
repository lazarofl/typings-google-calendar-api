from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="typings-google-calendar-api",
    version="1.0.0",
    author="Lazaro Suleiman",
    author_email="lazaro.fl@gmail.com",
    description="Python typehint support for Google Calendar API resources",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lazarofl/typings-google-calendar-api",
    packages=find_packages(),
    install_requires=[
        'typing_extensions',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)