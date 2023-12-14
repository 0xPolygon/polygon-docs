# Author: Katharine Murphy
# --------------------------------------------------------------------------------------------------------------
### INSTRUCTIONS FOR USE ###
# --------------------------------------------------------------------------------------------------------------
# Originally created for the output of solidity-docgen plugin.
#
# Feel free to improve it. It may need tweaking as I haven't used it in a while.
#
# Paste the markdown files into the relevant folder.
# Run the script from the root `docs` and add the path to list_files(path_parameter).
# Paste the resulting output directly into the `mkdocs.yaml` file at the relevant spot.
# --------------------------------------------------------------------------------------------------------------

import os

def list_files(startpath):
    for root, dirs, files in sorted(os.walk(startpath)):
            level = root.replace(startpath, '').count(os.sep)
            indent = ' ' * 4 * (level)
            print('  {}- {}:'.format(indent, os.path.basename(root).capitalize()),)
            subindent = ' ' * 4 * (level + 1)
            for f in sorted(files):
                title = str(f).replace('.md', '')
                filepath = os.path.join(root, f)
                print('  {}- {}:  {}'.format(subindent, title, filepath))

list_files("miden")