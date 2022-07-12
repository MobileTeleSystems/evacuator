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
import subprocess
import sys

from packaging import version as Version
from setuptools_git_versioning import get_all_tags, get_sha, get_tag

sys.path.insert(0, os.path.abspath(os.path.dirname(os.path.dirname(__file__))))


# -- Project information -----------------------------------------------------

project = "Evacuator"
copyright = "2022, ONEtools Team"
author = "ONEtools Team"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.

ver = Version.parse(subprocess.check_output("python ../setup.py --version", shell=True, text=True).strip())
version = ver.base_version
# The full version, including alpha/beta/rc tags.
release = ver.public

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx.ext.autosummary", "numpydoc", "sphinx_rtd_theme", "sphinx.ext.autodoc"]
numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "my-project-doc"

tags = {ver}
tags.update(Version.parse(tag) for tag in get_all_tags())
tags = [tag.public for tag in reversed(sorted(list(tags)))]

versions = [("latest", "/latest/")]
versions.extend([(tag, f"/{tag}/") for tag in tags])

tag = get_tag()
tag_sha = get_sha(tag)
head_sha = get_sha("HEAD")
on_tag = tag and head_sha is not None and head_sha == tag_sha

context = {
    "current_version": release,
    "version_slug": release,
    "versions": versions,
    "downloads": [
        ("html", f"https://rep.msk.mts.ru/artifactory/files/everproject/evacuator/docs/html-{release}.tar.gz"),
    ],
    "single_version": False,
    "gitlab_host": "gitlab.services.mts.ru",
    "gitlab_user": "bigdata/platform/everproject",
    "gitlab_repo": "evacuator",
    "gitlab_version": version if on_tag else "master",
    "conf_py_path": "/docs/",  # префикс для путей к файлам
    "display_gitlab": True,
    "commit": head_sha[:8] if head_sha is not None else None,
}

if "html_context" in globals():
    html_context.update(context)

else:
    html_context = context
