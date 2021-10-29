import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()
long_description = "na"

setuptools.setup(
    name='goodToHave',
    version='0.0.2',
    author='Anna Linnea',
    author_email='whatevs',
    description='Good to have things',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/annalp/goodToHave',
    project_urls = {
        "Bug Tracker": "https://github.com/annalp/goodToHave/issues"
    },
    license='MIT',
    packages=['goodtohave'],
    install_requires=['requests']
)