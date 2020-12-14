# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx_rtd_theme

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
copyright = '2020, CBIIT'
author = 'CBIIT'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    "sphinx_multiversion",
    'sphinx_rtd_theme',
    'recommonmark'
]
# sphinx_rtd_theme

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# replace versions.html
html_sidebars = { 
    "**": [
        "index.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "versions.html",
    ],
}

#html_sidebars = {
#    '**': [
#        'versions.html',
#    ],
#}

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

#html_theme_options = {
#    "github_repo": "bento-docs-versioned",
#    "github_user": "CBIIT",
#    "github_banner": True,
#    "github_button": True,
#    "travis_button": True,
#    "show_relbar_bottom": True,
#}
html_last_updated_fmt = "%c"
master_doc = "index"

## sphinx_rtd_theme options
html_theme_options = {
    'logo_only': False,
    #'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# Whitelist pattern for tags (set to None to ignore all tags)
smv_tag_whitelist = None

# Whitelist pattern for branches (set to None to ignore all branches)
#smv_branch_whitelist = r'^(master).*$'
smv_branch_whitelist = r'^.*$'

# Whitelist pattern for remotes (set to None to use local branches only)
# Only use local branches
smv_remote_whitelist = None
