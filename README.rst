.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=================
rer.pubblicazioni
=================

A Plone/Volto add-on for Regione Emilia-Romagna that adds a "Pubblicazione"
content type to manage institutional publications (reports, laws, official
documents, ...), with related search and listing views.

Features
--------

- "Pubblicazione" content type with abstract, authors, publication date,
  type, language, series, editor, rights and an attached file.
- Vocabularies for authors, types and languages, populated from the catalog
  and from control panel settings.
- A collection view tailored to list and filter publications.


Examples
--------

This add-on can be seen in action at the following sites:
- Is there a page on the internet where everybody can see the features?


Documentation
-------------

Full documentation for end users can be found in the "docs" folder, and is also available online at http://docs.plone.org/foo/bar


Translations
------------

This product has been translated into

- Italiano


Installation
------------

Install rer.pubblicazioni by adding it to your buildout::

    [buildout]

    ...

    eggs =
        rer.pubblicazioni


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/PloneGov-IT/rer.pubblicazioni/issues
- Source Code: https://github.com/PloneGov-IT/rer.pubblicazioni/


License
-------

The project is licensed under the GPLv2.


Authors
-------

This product has been developed by the `RedTurtle Technology` team.

.. image:: /docs/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/
