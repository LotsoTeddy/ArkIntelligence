from typing import List

from setuptools import find_packages, setup


def fetch_requirements(paths) -> List[str]:
    """
    This function reads the requirements file.

    Args:
        path (str): the path to the requirements file.

    Returns:
        The lines in the requirements file.
    """
    if not isinstance(paths, list):
        paths = [paths]
    requirements = []
    for path in paths:
        with open(path, "r") as fd:
            requirements += [r.strip() for r in fd.readlines()]
    return requirements


setup(
    name="ArkIntelligence",
    version="1.0.0",
    author="Yaozheng Fang",
    author_email="",
    description="An advanced SDK for Ark agent building.",
    long_description="An advanced SDK for Ark agent building.",
    url="https://github.com/yourusername/example",
    packages=find_packages(),
    install_requires=fetch_requirements("requirements.txt"),
)