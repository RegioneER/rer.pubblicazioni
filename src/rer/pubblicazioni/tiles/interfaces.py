# -*- coding: utf-8 -*-

from plone.supermodel import model
from zope import schema
from rer.pubblicazioni import _
from plone.app.vocabularies.catalog import CatalogSource


class ISearchPubblicazioniTile(model.Schema):
    """ Interfaccia per la tile di ricerca pubblicazioni della RER.
    """

    title = schema.TextLine(title=_(u'Title'), required=True, default=u'')

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

    css_class = schema.TextLine(
        title=_('search_publication_tile_css_class', u'CSS class'),
        description=_(
            'search_publication_tile_css_class_help',
            u'Insert a list of additional css classes for this tile.',
        ),
        required=False,
        default=u'',
    )

