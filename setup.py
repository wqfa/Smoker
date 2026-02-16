from setuptools import setup

setup(
    name="Smoker",
    version="0.1.0",
    py_modules=["Smoker"],
    entry_points={
        "console_scripts": [
            "smoker=smoker:cli"
        ]
    },
    author="Smoker",
    description="🔥 Smoker – single file Termux friendly tool",
    python_requires=">=3.8",
)
