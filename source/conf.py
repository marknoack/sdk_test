# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path += [
    os.path.abspath("../src"),
    os.path.abspath("../src/auth"),
    os.path.abspath("../src/common"),
    os.path.abspath("../src/connection"),
    os.path.abspath("../src/core"),
    os.path.abspath("../src/http"),
    os.path.abspath("../src/logger"),
    os.path.abspath("../src/paramter"),
    os.path.abspath("../src/service"),
    os.path.abspath("../src/statement")
]
print(sys.path)




# -- Project information -----------------------------------------------------

project = 'Node-sdk'
copyright = '2021, MNoack'
author = 'MNoack'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_js']

js_source_path = "../src"
#    ,"../src/auth",
#    "../src/common",
#    "../src/connection",
#    "../src/core",
#    "../src/http",
#    "../src/logger",
#    "../src/paramter",
#    "../src/service",
#    "../src/statement"
#

primary_domain = 'js'
js_language = 'typescript'
jsdoc_config_path = '../tsconfig.json'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']