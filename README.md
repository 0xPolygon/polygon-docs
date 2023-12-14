# Polygon Knowledge Layer

Welcome to the Polygon Knowledge Layer! This documentation is built using [the Material theme for MkDocs](https://squidfunk.github.io/mkdocs-material/). Our goal is to establish a high-quality, curated, and comprehensive "source of truth" for technical knowledge surrounding Polygon's main technology. This includes detailed sections on:

- Polygon CDK
- Polygon zkEVM
- Polygon PoS
- Polygon Miden

In addition, we include top-level sections for Tools and Tutorials to support developers in their journey with Polygon technology.

## Contributing

### Getting started

1. **Fork and branch**: Fork the `main` branch into your own GitHub account. Create a feature branch for your changes.
2. **Make changes**: Implement your changes or additions in your feature branch.
3. **Contribution quality**: Ensure that your contributions are:
   - **Atomic**: Small, self-contained, logical updates are preferred.
   - **Well documented**: Use clear commit messages. Explain your changes in the pull request description.
   - **Tested**: Verify your changes do not break existing functionality.
   - **Styled correctly**: Follow the [Microsoft Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/).

### Creating a pull request

1. **Pull request**: Once your changes are complete, create a pull request against the main branch of Polygon Knowledge Layer.
2. **Review process**: Your pull request will be reviewed by the maintainers. They may request changes or clarifications.
3. **Responsibility**: Contributors are expected to maintain their contributions over time and update them as necessary to ensure continued accuracy and relevance.

### Best practices

- **Stay informed**: Keep up-to-date with the latest developments in Polygon technologies.
- **Engage with the community**: Participate in discussions and provide feedback on other contributions.
- **Stay consistent**: Ensure your contributions are coherent with the rest of the documentation and do not overlap or contradict existing content.


## Running locally

### Prerequisites

Before running the site locally, you need to have the following installed:

1. [Python 3](https://www.python.org/downloads/).
2. [`virtualenv`](https://pypi.org/project/virtualenv/): Install using `pip3 install virtualenv`.

### Setup

1. **Clone repository**: Clone the Polygon Knowledge Layer repository to your local machine.
2. **Create a virtual environment**: Run `virtualenv venv; source venv/bin/activate` in the root directory.
3. **Install dependencies**: Install required Python packages with `pip3 install -r requirements.txt`.

### Running the website

Before running the website, you'll need to first load the Python virtual environment in your current shell. To do this, type the following (depending on your shell):

- **Bash**, **zsh** (most common): `virtualenv venv; source venv/bin/activate`
- **Fish**: `virtualenv venv; source venv/bin/activate.fish`
- **Nu**: `virtualenv venv; source venv/bin/activate.nu`

You only need to do the above once per shell session. Then, pick one of the following:

1. **MkDocs in strict mode**: Use `mkdocs serve --strict` for a production-like environment.
2. **MkDocs in normal mode**: Use `mkdocs serve` for a less strict, more forgiving environment, suitable for debugging.

### Docker alternative

If you prefer Docker, you can build and run the site using the following commands:

```sh
docker build -t polygon-docs .
docker compose up
```

## Automated deployments

This repository uses GitHub Actions to automate some deployments from certain branches, which is useful for testing:

- **`main`**: Staging branch. Changes are deployed per-commit to https://docs-staging.polygon.technology.
- **`dev`**: Experimental branch. Updates with `main` every 24 hours. Changes are deployed per-commit to https://docs-dev.polygon.technology.

Whenever we are happy with `main`, a trigger can be manually done through GitHub Actions which deploys staging to production at https://docs.polygon.technology.

## Contact and support

For any queries or support, join our Polygon Slack channel at `#disc_tkd_techdocs`. Current team members:

- Grace Torrellas (@0xgraciegrace)
- Anthony Matlala (@EmpieichO)
- Katharine Murphy (@kmurphypolygon)