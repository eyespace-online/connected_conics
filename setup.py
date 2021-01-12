import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="connected_conics",
    version="0.0.3",
    author="Jake Brown",
    author_email="jake@eyespacelenses.com",
    description="Functions for geometric analysis of connected conic sections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/eyespacelenses/connected_conics",
    packages=setuptools.find_packages(),
    install_requires=[
        "scipy",
        "numpy",
        "pyyaml",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)