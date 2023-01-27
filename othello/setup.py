import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="XXX",
    version="XXX",
    author="XXX",
    author_email="XXX",
    description="XXX",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: XXX",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    scripts = ["bin/XXX"],
    python_requires=">=3.9",
    install_requires = [
        "XXX"
        ]
)
