from os import path

__version__ = '0.1.11'
__version_full__ = __version__

package_dir = path.dirname(path.abspath(__file__))

def get_path():
    return package_dir

def setup(app):
    app.add_html_theme('sphinx_materialdesign_theme', package_dir)

    if sphinx.version_info >= (1, 8, 0):
        # Add Sphinx message catalog for newer versions of Sphinx
        # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
        rtd_locale_path = path.join(get_path(), 'locale')
        app.add_message_catalog('sphinx', rtd_locale_path)