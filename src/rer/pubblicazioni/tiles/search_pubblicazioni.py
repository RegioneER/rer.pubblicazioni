# -*- coding: utf-8 -*-
# from plone.app.vocabularies.catalog import CatalogSource
# from plone.app.z3cform.widget import AjaxSelectFieldWidget, AjaxSelectWidget
# from plone.autoform import directives
# from plone.z3cform.layout import FormWrapper
# from Products.CMFPlone.resources import add_resource_on_request
# from Products.CMFPlone.utils import get_top_request
# from rer.pubblicazioni import _
# from z3c.form import field, button
# from z3c.form.form import Form
# from z3c.form.interfaces import HIDDEN_MODE
# from zope import schema
# from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
# from zope.interface import implements
# from zope.interface import Interface
from plone import api
from plone.app.uuid.utils import uuidToObject
from plone.tiles import Tile
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


# class ISearchForm(Interface):
#
#     text = schema.TextLine(
#         required=False,
#         title=_('Searchable Text')
#     )
#     publicationAuthor = schema.Choice(
#         required=False,
#         title=_(u'rer_pub_author_tags', default=u'Author/Authors'),
#         vocabulary="rer.pubblicazioni.used_authors"
#     )
#     publicationTypes = schema.Choice(
#         required=False,
#         title=_(u'rer_pub_type', default=u'Pubblication types'),
#         vocabulary="rer.pubblicazioni.used_types"
#     )
#
#     publicationLanguage = schema.Choice(
#         required=False,
#         title=_(u'rer_publication_language', default=u'Language'),
#         vocabulary="rer.pubblicazioni.used_languages"
#     )
#     publicationDateFrom = schema.Date(
#         required=False,
#         title=_(u'rer_publication_date_from', default=u'From date'),
#     )
#     publicationDateTo = schema.Date(
#         required=False,
#         title=_(u'rer_publication_date_to', default=u'To date'),
#     )
#     portal_type = schema.TextLine(
#         required=True,
#         title=_(u'portal_type', default=u'Portal type')
#     )
#
#     search_path = schema.TextLine(
#         required=False,
#         title=_(u'search_path', default=u'/')
#     )
#
#
# class SearchForm(Form):
#
#     fields = field.Fields(ISearchForm)
#     label = _(u'Search for pubblications')
#     ignoreContext = True
#
#     def updateWidgets(self):
#         # self.fields['publicationAuthor'].widgetFactory = AjaxSelectFieldWidget
#         # self.fields['publicationTypes'].widgetFactory = AjaxSelectFieldWidget
#         super(SearchForm, self).updateWidgets()
#         self.widgets['text'].name = 'SearchableText'
#         self.widgets['publicationAuthor'].name = 'authors'
#         self.widgets['publicationTypes'].name = 'publication_types'
#         self.widgets['publicationLanguage'].name = 'publication_language'
#         self.widgets['publicationDateFrom'].name = 'start'
#         self.widgets['publicationDateTo'].name = 'end'
#         self.widgets['portal_type'].name = 'portal_type'
#         self.widgets['portal_type'].value = 'Pubblicazione'
#         self.widgets['portal_type'].mode = HIDDEN_MODE
#         self.widgets['search_path'].name = 'search_path'
#         # print "\n\n"
#         # print self.search_path
#         # print "\n\n"
#         # self.widgets['search_path'].value = 'Percorso'
#         self.widgets['search_path'].mode = HIDDEN_MODE
#
#     @button.buttonAndHandler(_(u'Search', default='Search'))
#     def handleApply(self, action):
#         data, errors = self.extractData()
#
#         if errors:
#             return
#
#     @property
#     def action(self):
#         baseurl = "/@@search?portal_type=Pubblicazione"
#         portalurl = api.portal.get().absolute_url()
#         return portalurl + baseurl
#
#
# class TileFormViewer(FormWrapper):
#
#     form = SearchForm
#     index = ViewPageTemplateFile("templates/search_form.pt")
#
#     def get_error_message(self):
#         return self.context.translate(
#             _(u'End date should be great than start date')
#         )


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
