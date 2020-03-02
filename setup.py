import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="denver",
    version="0.0.2",
    author="Yoann Lamouroux",
    author_email="ylamouroux@vente-privee.com",
    description="A secret environment management",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.vptech.eu/ylamouroux/denver",
    packages=setuptools.find_packages(),
    install_requires=['click'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Operating System :: POSIX"
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "denver = denver.denver:display_eval"
        ]
    }
)
