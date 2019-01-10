import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="printipigeon",
    version="0.0.6",
    author="Fons van der Plas",
    author_email="fonsvdplas@gmail.com",
    description="Package for sending images to the printi.me API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fons-/printi-pigeon",
    packages=setuptools.find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
