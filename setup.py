import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="repeatstring"
    version="0.0.1",
    author="Andrew Scholly",
    author_email="ajscholly191@stevenscollege.edu",
    url="https://github.com/AndrewScholly/Python-quiz-skeleton",
    description="This project simply runs a string six times",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
