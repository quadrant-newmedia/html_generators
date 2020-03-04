import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="APP_NAME",
    version="0.0.0",
    author="Alex Fischer",
    author_email="alex@quadrant.net",
    description="TODO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="TODO - github repo",
    packages=['APP_NAME', 'APP_NAME.tests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=2.2,<3.1"],
)