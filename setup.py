from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="notifyhub",  # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="Notification on telegram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yhchong/notify-me",
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
