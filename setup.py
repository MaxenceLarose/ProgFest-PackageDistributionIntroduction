import setuptools

setuptools.setup(
    name="ProgFestPDI_test",
    version="0.0.1",
    author="Maxence Larose",
    author_email="maxence.larose.1@ulaval.ca",
    description="A small example package",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MaxenceLarose/PackageDistributionIntroduction",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    # install_requires=['matplotlib>=3', 'numpy'],
)
