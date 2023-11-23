# Polygon docs

Welcome to the Polygon Docs website, built with [the Material theme for MkDocs](https://squidfunk.github.io/mkdocs-material/).

## Instructions for use

Work on a local branch and request a review from a teammate.

## How to run the site locally

### Clone the repo

```sh
git clone https://github.com/0xPolygon/polygon-docs.git
cd polygon-docs
```

### Run with Python

1. Download and install Python 3.11: https://www.python.org/downloads/

2. Install the `virtualenv` package:

```sh
pip install virtualenv
```

3. Build and serve the html

```sh
./run.sh
```

The site runs at: http://127.0.0.1:8000/

### Run with Docker

1. Run the following commands from the project root:

```sh
docker build -t polygon-docs .
docker compose up
```

### Run manually

1. Download and install Python, as above, and ensure you have installed all the packages listed in `requirements.txt`:

```sh
pip3 install -r requirements.txt
```

2. Run the following from the project root to bring up the site:

```sh
./run.sh
```

## Questions

Feel free to contact the team any time: `#disc_tkd_techdocs`