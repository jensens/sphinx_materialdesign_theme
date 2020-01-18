#!/bin/bash
pybabel extract -F babel-mapping.ini -o sphinx_materialdesign_theme/locale/sphinx.pot sphinx_materialdesign_theme
pybabel update -D sphinx -i sphinx_materialdesign_theme/locale/sphinx.pot -d sphinx_materialdesign_theme/locale
pybabel compile -D sphinx -d sphinx_materialdesign_theme/locale/
