![example workflow](https://github.com/YHallouard/Shell_ai_evse/actions/workflows/main.yml/badge.svg)

# Introduction

EVSE Work from TotalEnergies team 1 on the EV charlenge proposed by [Shell](https://www.hackerearth.com/en-us/challenges/competitive/shellai-hackathon-2022)

# Getting Started

## Requirements

* Python version 3.8 or higher
* Python Environment management system: [Conda](https://docs.conda.io/en/latest/miniconda.html) or [venv](https://docs.python.org/3/library/venv.html)
* [Poetry](https://python-poetry.org/docs/#installation) for dependency management and packaging.
* [npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) to install Azurite (emulator of azure data storages)


# Local Development Configuration

Here are the steps to follow:

* Create a virtual environment with conda
    ```sh
    conda create --name evse python=3.8
    conda activate evse
    # Verify that python path is inside the env created previously(path should contain degas-00)
    which python
    ```
* Install poetry
    ```sh
    # Install poetry
    pip install --user poetry
    # Verify that the CLI is accessible
    poetry --version
    # Verify that poetry is using the right python
    poetry poetry env info
    # The virtual env should point to evse
    # The System's python should also point to evse
    ```
