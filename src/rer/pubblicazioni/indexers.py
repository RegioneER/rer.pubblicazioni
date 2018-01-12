# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from .interfaces import IPubblicazione


@indexer(IPubblicazione)
def author_indexer(object, **kw):
    """ Factory method per l'indicizzazione del campo autori di una
    pubblicazione.
    """
    return object.publicationAuthor
