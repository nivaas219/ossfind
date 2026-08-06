from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ossfind",
    version="0.1.0",
    author="Nivaas V",
    author_email="nivaas9293@gmail.com",
    description="CLI tool to find open source contribution opportunities and swag programs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nivaas219/ossfind",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "ossfind=ossfind.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)