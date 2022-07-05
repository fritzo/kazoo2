from setuptools import find_packages, setup

setup(
    name="kazoo2",
    version="0.0.0",
    description="Experiments in interactive streaming audio",
    packages=find_packages(include=["kazoo2"]),
    url="https://github.com/fritzo/kazoo2",
    author="Fritz Obermeyer",
    author_email="fritz.obermeyer@gmail.com",
    install_requires=[
        "torch",
        "torchaudio",
    ],
    extras_require={
        "test": [
            "black",
            "isort>=5.0",
            "flake8",
            "pytest>=5.0",
            "mypy>=0.812",
        ],
    },
    python_requires=">=3.7",
)
