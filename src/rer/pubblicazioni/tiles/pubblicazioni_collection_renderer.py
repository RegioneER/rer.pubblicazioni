# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from collective.tiles.collection.interfaces import ICollectionTileRenderer
from zope.interface import implementer
from collective.tiles.collection import _
from zope.component import getUtility
from plone.memoize.view import memoize
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import ISiteSchema
from zope.component import getMultiAdapter
from DateTime import DateTime


@implementer(ICollectionTileRenderer)
class PubblicazioniCollectionRenderer(BrowserView):

    display_name = _("Layout pubblicazioni")


class HelpersView(BrowserView):

    def __init__(self, context, request):
        super(HelpersView, self).__init__(context, request)

        self.plone_view = getMultiAdapter(
            (context, request), name=u'plone')

    @memoize
    def get_thumb_scale_list(self):
        if getattr(self.context, 'suppress_thumbs', False):
            return None
        thsize = getattr(self.context, 'thumb_scale_list', None)
        if thsize:
            return thsize
        registry = getUtility(IRegistry)
        settings = registry.forInterface(
            ISiteSchema, prefix='plone', check=False)
        if settings.no_thumbs_lists:
            return None
        return settings.thumb_scale_listing

    def toLocalizedTime(self, time, long_format=False, time_only=False):
        time = DateTime(time.strftime('%Y-%m-%d'))
        return self.plone_view.toLocalizedTime(time, long_format, time_only)
