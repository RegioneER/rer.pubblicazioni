# -*- coding: utf-8 -*-

from plone import api
from plone.app.uuid.utils import uuidToObject
from plone.tiles import Tile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


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
        factory = getUtility(
            IVocabularyFactory,
            'rer.pubblicazioni.used_authors')
        vocabulary = factory(self.context)
        return vocabulary

    def get_publication_type(self):
        values = api.portal.get_registry_record('rer.pubblicazioni.browser.settings.IRerPubblicazioniSettings.tipologie')  # noqa
        if values:
            return values.split('\r\n')
        else:
            return []

    def get_publication_language(self):
        values = api.portal.get_registry_record('rer.pubblicazioni.browser.settings.IRerPubblicazioniSettings.lingue')  # noqa
        if values:
            return values.split('\r\n')
        else:
            return []
