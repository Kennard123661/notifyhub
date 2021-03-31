from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="notifyhub",  # Replace with your own username
    version="0.0.3",
    author="Kennard Ng",
    author_email="kennard.ng.pool.hua@gmail.com",
    description="Notification on instant messaging platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Kennard123661/notifyhub",
    packages=find_packages(),
    install_requires=[
        'requests',
        'discord.py'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
