from setuptools import setup

setup(
    name="peepdf",
    version="0.4.3",
    author="Jose Miguel Esparza",
    license="GNU GPLv3",
    url="http://eternal-todo.com",
    install_requires=[
        "jsbeautifier==1.14.3",
        "colorama==0.4.4",
        "future>=0.18.2",
        "Pillow==9.1.0",
        "pythonaes==1.0",
    ],
    entry_points={
        "console_scripts": [
            "peepdf = peepdf.main:main",
        ],
    },
    packages=[
        "peepdf",
    ],
)
