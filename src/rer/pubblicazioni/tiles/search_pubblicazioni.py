# -*- coding: utf-8 -*-

from plone import api
from plone.app.uuid.utils import uuidToObject
from plone.tiles import Tile
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


class SearchPubblicazioni(Tile):
    """
    Tile for pubblicazioni search on site
    """

    def get_search_path(self):
        # search_path = self.data.get('path', '')
        obj = uuidToObject(self.data.get('search_path', ''))
        if obj:
            path = '/'.join(obj.getPhysicalPath())
            return path
        else:
            return ""

    def get_authors(self):
        search_path = self.get_search_path()
        results = api.content.find(
            portal_type='Pubblicazione', path=search_path
        )
        authors_options = []

        for brain in results:
            if brain.authors:
                for author in brain.authors:
                    if author not in authors_options:
                        authors_options.append(author)

        terms = []
        for author in sorted(authors_options):
            terms.append(SimpleTerm(title=author, token=author, value=author,))
        vocabulary = SimpleVocabulary(terms)

        return vocabulary

    def get_publication_type(self):
        values = api.portal.get_registry_record(
            'rer.pubblicazioni.browser.settings.IRerPubblicazioniSettings.tipologie'  # noqa
        )
        if values:
            return values.split('\r\n')
        else:
            return []

    def get_publication_language(self):
        values = api.portal.get_registry_record(
            'rer.pubblicazioni.browser.settings.IRerPubblicazioniSettings.lingue'  # noqa
        )
        if values:
            return values.split('\r\n')
        else:
            return []
