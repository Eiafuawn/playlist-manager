# pip3 install setuptools twine wheel
# python3 setup.py sdist bdist_wheel
# twine upload dist/*


import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

with (HERE / "requirements.txt").open() as f:
    requirements = f.read().splitlines()

setup(
    name="spotia3310",
    version="0.1.0",
    description="python cli program to download your spotify playlist",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Eiafuawn/spotia3310",
    author="Eiafuawn",
    author_email="kenan.henzelin@proton.me",
    license="MIT",
    entry_points={
        'console_scripts': [
            'spotia = spotia3310.__main__:main',
        ],
    },
    python_requires='>=3.11',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["spotia3310"],
    include_package_data=True,
    install_requires=requirements,
)
