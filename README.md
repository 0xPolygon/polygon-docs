# mkdocs-minify-plugin

[![PyPI - Python Version][python-image]][pypi-link]

An MkDocs plugin to minify HTML, JS or CSS files prior to being written to disk.

HTML minification is done using [htmlmin2](https://github.com/wilhelmer/htmlmin).

JS minification is done using [jsmin](https://github.com/tikitu/jsmin/).

CSS minification is done using [csscompressor](https://github.com/sprymix/csscompressor).

## Setup

Install the plugin using pip:

```bash
pip install mkdocs-minify-plugin
```

Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - search
  - minify:
      minify_html: true
      minify_js: true
      minify_css: true
      htmlmin_opts:
          remove_comments: true
      cache_safe: true
      js_files:
          - my/javascript/dir/file1.js
          - my/javascript/dir/file2.js
      css_files:
          - my/css/dir/file1.css
          - my/css/dir/file2.css
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

## Options

- `minify_html`:
  - Defaults to `False`.
  - Sets whether HTML files should be minified.
- `minify_js`:
  - Defaults to `False`.
  - Sets whether JS files should be minified.<br>
    If set to `True`, you must specify the JS to be minified files using `js_files` (see below).
- `minify_css`:
  - Defaults to `False`.
  - Sets whether CSS files should be minified.<br>
    If set to `True`, you must specify the CSS to be minified files using `css_files` (see below).
- `htmlmin_opts`:
  - Defaults to `None`.
  - Sets runtime htmlmin API options using the [config parameters of htmlmin](https://htmlmin.readthedocs.io/en/latest/reference.html#main-functions)
- `cache_safe`:
  - Defaults to `False`.
  - Sets whether a hash should be added to the JS and CSS file names. This ensures that the browser always loads the latest version of the files instead of loading them from the cache.<br>
    If set to `True`, you must specify the files using `js_files` or `css_files` (see below).
- `js_files`:
  - Defaults to `None`.
  - List of JS files to be minified.<br>
    The plugin will generate minified versions of these files and save them as `.min.js` in the output directory.
- `css_files`:
  - Defaults to `None`.
  - List of CSS files to be minified.<br>
    The plugin will generate minified versions of these files and save them as `.min.css` in the output directory.

> **Note:** When using `minify_js` or `minify_css`, you don't have to modify the `extra_javascript` or `extra_css` entries
in your `mkdocs.yml` file. The plugins automatically takes care of that.
Both `minify_js` and `minify_css` support the use of **globs** (e.g. `**/*.css`).

[pypi-link]: https://pypi.python.org/pypi/mkdocs-minify-plugin/
[python-image]: https://img.shields.io/pypi/pyversions/mkdocs-minify-plugin?logo=python&logoColor=aaaaaa&labelColor=333333

[creating-a-pull-request-summary-with-github-copilot.md](https://github.com/user-attachments/files/16593516/creating-a-pull-request-summary-with-github-copilot.md)
[CODING_GUIDELINES.md](https://github.com/user-attachments/files/16593514/CODING_GUIDELINES.md)
[Etehereum_compData.json](https://github.com/user-attachments/files/16593510/Etehereum_compData.json)
# Polygon Knowledge Layer


Welcome to the Polygon Knowledge Layer.

These docs use [the Material theme for MkDocs](https://squidfunk.github.io/mkdocs-material/). Our goal is to establish a high-quality, curated, and comprehensive "source of truth" for Polygon's technology. 

This includes sections on:

- Polygon CDK
- Polygon zkEVM
- Polygon PoS
- Polygon Miden
- Developer tools 

## Run locally

### Prerequisites

1. [Python 3.12](https://www.python.org/downloads/).
2. [`virtualenv`](https://pypi.org/project/virtualenv/): Install using `pip3 install virtualenv`.

### Setup

1. Clone the repository.
2. `cd` to the root.
3. Run the `run.sh` script. You may need to make the script executable: `chmod +x run.sh`

```sh
./run.sh
```

The site comes up at http://127.0.0.1:8000/ 

### Docker 

If you prefer Docker, you can build and run the site using the following commands:

```sh
docker build -t polygon-docs .
docker compose up
```

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

## Contact and support

- For docs issues (technical or language) open an issue here.
- For technical issues with the software, either raise an issue here and we will follow up, or check https://support.polygon.technology/support/home. 

## The team

- Anthony Matlala (@EmpieichO)
- Katharine Murphy (@kmurphypolygon)
- Hans (@hsutaiyu) 
