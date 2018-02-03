from distutils.core import setup
from os.path import abspath, dirname, join

with open(join(abspath(dirname(__file__)), "README.rst")) as f:
    long_description = f.read()

setup(
    name="ircclive",
    version="1.0",
    author="Mayu Laierlence",
    author_email="minacle@live.com",
    url="https://github.com/minacle/ircclive",
    description="Simple IRCCloud session keeper; written in python3.",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat :: Internet Relay Chat",
        "Topic :: Utilities",
    ],
    py_modules=["ircclive"],
    keywords=["irccloud"],
    entry_points={
        "console_scripts": ["ircclive = ircclive:_main"],
        "setuptools.installation": ["eggsecutable = ircclive:_main"],
    },
    zip_safe=True,
    long_description=long_description,
)