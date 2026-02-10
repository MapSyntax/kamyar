# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Kamyar Hasanzadeh'
copyright = 'Kamyar Hasanzadeh'
author = 'Kamyar Hasanzadeh'
release = '2025'

kh_profile = {
    "name": "Dr. Kamyar Hasanzadeh",
    "lines": [
        "Lecturer · Adjunct Professor",
        "Geoinformatics & Urban Informatics",
        "University of Helsinki",
    ],
    "details": [
        {"icon": "map", "text": "Helsinki, Finland"},
        {"icon": "home", "text": "University of Helsinki"},
        {"icon": "link", "text": "Website", "href": "https://researchportal.helsinki.fi/en/persons/kamyar-hasanzadeh/"},
        {"icon": "mail", "text": "Email", "href": "mailto:kamyar.hasanzadeh[at]helsinki.fi"},
        {"icon": "github", "text": "Github", "href": "https://github.com/kamyar68"},
        {"icon": "scholar", "text": "Google Scholar", "href": "https://scholar.google.fi/citations?user=XBp2BEEAAAAJ&hl=fi"},
        {"icon": "orcid", "text": "ORCID", "href": "https://orcid.org/0000-0002-0705-7662"},
        {"icon": "linkedin", "text": "LinkedIn", "href": "https://www.linkedin.com/in/kamyar-hasanzadeh-6257a227/"},

    ],
}


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['nbsphinx']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_last_updated_fmt = "%d %B %Y"
html_logo = "_static/logo/kamyarh.png"
html_short_title = "Kamyar H."
html_title = ""
html_css_files = ["custom.css"]

html_context = {
    "kh_profile": kh_profile,
}



html_theme = "furo"


html_theme_options = {
    "collapse_navigation": False,
    'search_bar_position': 'none',
    'nosidebar': False,
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "notebook_interface": "classic"
    },
    "path_to_docs": "docs",
    "repository_branch": "main",
    "repository_url": "https://github.com/MapSyntax/kamyar",
    "use_edit_page_button": True,
    "use_repository_button": True,
    'display_version': False,


}
html_static_path = ['_static']

nb_execution_mode = "force"
nb_execution_timeout = 120  # needed, e.g., when matplotlib updates its font cache
nb_execution_show_tb = True  # show errors
nbsphinx_allow_errors = True
