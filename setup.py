import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_dynamic_path",
    version="0.0.1",
    author="Alex Fischer",
    author_email="alex@quadrant.net",
    description="A django path() replacement enabling truly dynamic urls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="TODO",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=2.2,<3.1"],
)