# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme
import recommonmark
from recommonmark.transform import AutoStructify


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Bento'
copyright = '2021, CBIIT'
author = 'CBIIT'
version = "latest"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx_markdown_tables',
    "sphinx_multiversion",
    'sphinx_rtd_theme',
    'recommonmark',
    'sphinxemoji.sphinxemoji',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# replace versions.html
html_sidebars = { 
    "**": [
        "index.html",
        "navigation.html",
        "searchbox.html",
        "versions.html",
        "sourcelink.html",
    ],
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]

html_last_updated_fmt = "%c"
master_doc = "index"

html_context = {
    "display_github": True, # Integrate GitHub
    "github_user": "CBIIT", # Username
    "github_repo": "bento-docs", # Repo name
    #"github_version": "master", # Version
    "conf_py_path": "/source/", # Path in the checkout to the docs root
}

## sphinx_rtd_theme options
html_theme_options = {
    #'vcs_pageview_mode': 'edit',
    'prev_next_buttons_location': 'both',
    'sticky_navigation': True,
    # Toc options
    'navigation_depth': 3,
    #'github_url': 'https://github.com/CBIIT/bento-docs/',
}
html_show_sourcelink = True


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = None

# Whitelist pattern for branches (set to None to ignore all branches)
#smv_branch_whitelist = r'^(?!master).*$'      # Include all branches except "master"
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
# Only use local branches
smv_remote_whitelist = None

# A Regular Expression is used to determine if a version of the documentation 
# has been released or if it’s a development version. To allow more 
# flexibility, the regex is evaluated over the full refname.
smv_released_pattern = r'.*release.*'
smv_latest_version = '.*master.*'

# AutoStructify - for advanced markdown to rst transformations
# Needs to be at the bottom of conf.py
# as described in https://recommonmark.readthedocs.io/en/latest/index.html
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
