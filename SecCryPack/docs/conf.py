# docs/conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

source_suffix = '.rst'
master_doc = 'index'
