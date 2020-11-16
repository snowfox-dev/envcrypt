import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="envcrypto",
    version="0.0.1",
    author="SnowFox",
    author_email="snowfoxdev@outlook.com",
    description="Symetrical Encryption of Environment Variables and Data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snowfox-dev/envcrypt.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
