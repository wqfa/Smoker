from setuptools import setup, find_packages

setup(
    name="Smoker",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "smoker=smoker.cli:cli"
        ]
    },
    author="Valter",
    description="🔥 Smoker – modular Termux friendly tool",
    python_requires=">=3.8",
)
