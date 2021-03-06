# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

with open(os.path.join('..', 'pyproject.toml'), 'r') as f:
    version = [l for l in f.read().splitlines(keepends=False) if 'version' in l][0].split(' ')[-1].strip('\"')
this_files_path = os.path.abspath(__file__)
this_files_dir = os.path.split(this_files_path)[0]
root_dir = os.path.split(this_files_dir)[0]
src_path = os.path.join(root_dir)
sys.path.insert(1, src_path)

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "recommonmark"
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

if os.getenv("SPELLCHECK"):
    extensions += ("sphinxcontrib.spelling",)
    spelling_show_suggestions = True
    spelling_lang = "en_US"

source_suffix = ".rst"
master_doc = "index"
project = "pupy"
year = "2018"
author = "jesse k rubin"
copyright = "{0}, {1}".format(year, author)
release = version

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/jessekrubin/python-pupy/issues/%s", "#"),
    "pr": ("https://github.com/jessekrubin/python-pupy/pull/%s", "PR #"),
}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"
if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = "sphinx_rtd_theme"

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {"**": ["searchbox.html", "globaltoc.html", "sourcelink.html"]}
html_short_title = "%s-%s" % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False
