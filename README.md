# Polygon Knowledge Layer - PDF generator branch

This is a protected branch with instructions for how to generate PDFs from the documentation.

## Instructions for use:

1. **ALWAYS** generate PDFs on a local machine.
2. Never merge this branch to any environment.
3. Before doing **ANYTHING**, run `git merge origin main` and deal with any conflicts. 
4. Hide/reveal the sections you want to publish in a PDF in the `mkdocs.yml` toc.
5. Run `mkdocs build` from the root.
6. You will see some warnings, you can ignore them (at the time of writing).
7. The PDF is generated in the `site/pdf/` directory.

## Warnings

1. The index page graphics break the plugin, so I have removed those pages. 
2. You can ignore the warnings about broken links to index pages.
2. If you want PDFs of Learn or Miden docs, it needs to be done in those repos directly.

## Example PDF

I have put an example PDF into the `pdf/` directory.
