# Configuration file for the Sphinx documentation builder.

# -- Project information

project = '联萌社区教程项目'
copyright = '2022, 联萌及所有贡献者'
author = '社区贡献者们'

release = '0.1'
version = '1.0.0'

# -- General configuration

extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser'
]

myst_enable_extensions = ["deflist"]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/Lianmoe/Lianmoe-Tutorial",
    "use_repository_button": True,
}




# -- Options for EPUB output
epub_show_urls = 'footnote'
