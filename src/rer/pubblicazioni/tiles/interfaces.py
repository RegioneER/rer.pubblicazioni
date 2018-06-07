# -*- coding: utf-8 -*-

from plone.supermodel import model
from zope import schema
from rer.pubblicazioni import _
from plone.app.vocabularies.catalog import CatalogSource


class ISearchPubblicazioniTile(model.Schema):
    """ Interfaccia per la tile di ricerca pubblicazioni della RER.
    """

    searchone_path = schema.TextLine(
        required=False,
        title=_(u'path', default=u'/')
    )

    content_uid = schema.Choice(
        title=_(u"Select an existing content"),
        required=True,
        source=CatalogSource(),
    )

    search_path = schema.Choice(
        title=_(
            'searchpub_tile_folderuid',
            u'Percorso di ricerca'),
        description=_(
            'searchpub_tile_folderuid_help',
            u'Usa questo campo per limitare la ricerca di pubblicazioni ad un'
            u'percorso specifico.'),
        source=CatalogSource(portal_type=('Folder')),
        required=False,
    )


class ITileDiProva(model.Schema):
    """ interfaccia della tile di prova - cancellare
    """

    searchone_path = schema.TextLine(
        required=False,
        title=_(u'path', default=u'/')
    )

    search_path = schema.Choice(
        title=_(
            'searchpub_tile_folderuid',
            u'Percorso di ricerca'),
        description=_(
            'searchpub_tile_folderuid_help',
            u'Usa questo campo per limitare la ricerca di pubblicazioni ad un'
            u'percorso specifico.'),
        source=CatalogSource(portal_type=('Folder')),
        required=False,
    )
