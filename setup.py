from typing import List

import setuptools


def read_multiline_as_list(file_path: str) -> List[str]:
    with open(file_path) as fh:
        contents = fh.read().split("\n")
        if contents[-1] == "":
            contents.pop()
        return contents


with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = read_multiline_as_list("requirements.txt")

# classifiers = read_multiline_as_list("classifiers.txt")

setuptools.setup(
    name="chan-url-lib",
    version="1.1.0",
    author="Nei Cardoso de Oliveira Neto",
    author_email="nei.neto@hotmail.com",
    description="Library to parse chan URLs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cardoso-neto/chan-url-lib",
    packages=setuptools.find_packages(),
    # classifiers=classifiers,
    keywords="",
    python_requires=">=3.7",
    install_requires=requirements,
)
