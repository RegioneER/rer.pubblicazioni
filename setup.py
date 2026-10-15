"""Installer for the rer.pubblicazioni package."""

from setuptools import find_packages
from setuptools import setup

long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="rer.pubblicazioni",
    version="3.1.0.dev0",
    description="An add-on to manage publications for Regione Emilia Romagna.",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone",
    author="RedTurtle",
    author_email="sviluppo@redturtle.it",
    url="https://pypi.python.org/pypi/rer.pubblicazioni",
    license="GPL version 2",
    python_requires=">=3.10",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["rer"],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "z3c.jbot",
        "plone.volto",
        "collective.volto.blocksfield",
        # plone.volto's migrate_richtext view imports requests without
        # declaring it as a dependency.
        "requests",
        "Zope",
        "Products.CMFCore",
        "Products.CMFPlone",
        "plone.api",
        "plone.app.contenttypes",
        "plone.app.registry",
        "plone.app.textfield",
        "plone.app.vocabularies",
        "plone.app.z3cform",
        "plone.autoform",
        "plone.dexterity",
        "plone.indexer",
        "plone.memoize",
        "plone.namedfile",
        "plone.restapi",
        "plone.supermodel",
        "beautifulsoup4",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.browserlayer",
            # plone.app.contenttypes.testing imports this unconditionally,
            # even without robot tests of our own.
            "plone.app.robotframework",
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
