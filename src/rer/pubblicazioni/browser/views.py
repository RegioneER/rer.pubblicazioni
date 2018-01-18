# -*- coding: utf-8 -*-

from DateTime import DateTime
from plone.app.contenttypes.browser.collection import CollectionView
from Products.Five import BrowserView
from zope.component import getMultiAdapter


class PubblicazioneView(BrowserView):
    """
    Vista del contenuto Pubblicazione
    """

    def __init__(self, context, request):
        super(PubblicazioneView, self).__init__(context, request)
        self.plone_view = getMultiAdapter(
              (context, request), name=u'plone')

    def toLocalizedTime(self, publication_date):
        time = DateTime(publication_date.strftime('%Y-%m-%d'))
        return self.plone_view.toLocalizedTime(time, False, False)


class PubblicazioniCollectionView(CollectionView):
    """
    Vista del contenuto Pubblicazione
    """

    def __init__(self, context, request):
        super(PubblicazioniCollectionView, self).__init__(context, request)
        self.plone_view = getMultiAdapter(
              (context, request), name=u'plone')

    def toLocalizedTime(self, publication_date):
        time = DateTime(publication_date.strftime('%Y-%m-%d'))
        return self.plone_view.toLocalizedTime(time, False, False)
