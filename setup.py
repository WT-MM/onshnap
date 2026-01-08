# mypy: disable-error-code="import-untyped"
#!/usr/bin/env python
"""Setup script for onshnap - Frozen-snapshot URDF exporter for Onshape."""

import re

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description: str = f.read()


with open("onshnap/requirements.txt", "r", encoding="utf-8") as f:
    requirements: list[str] = [
        line.strip() for line in f.read().splitlines() if line.strip() and not line.startswith("#")
    ]


with open("onshnap/requirements-dev.txt", "r", encoding="utf-8") as f:
    requirements_dev: list[str] = [
        line.strip() for line in f.read().splitlines() if line.strip() and not line.startswith("#")
    ]


with open("onshnap/__init__.py", "r", encoding="utf-8") as fh:
    version_re = re.search(r"^__version__ = \"([^\"]*)\"", fh.read(), re.MULTILINE)
assert version_re is not None, "Could not find version in onshnap/__init__.py"
version: str = version_re.group(1)


setup(
    name="onshnap",
    version=version,
    description="Frozen-snapshot URDF exporter for Onshape assemblies",
    author="Wesley Maa",
    url="https://github.com/WT-MM/onshnap.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.10",
    install_requires=requirements,
    tests_require=requirements_dev,
    extras_require={"dev": requirements_dev},
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "onshnap=onshnap.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering",
    ],
)
