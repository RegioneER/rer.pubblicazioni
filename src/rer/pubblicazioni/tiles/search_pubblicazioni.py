# -*- coding: utf-8 -*-
# from zope.interface import implements
from z3c.form import field, button
from plone.tiles import Tile
from zope.interface import Interface
# from plone.autoform import directives
from plone.z3cform.layout import FormWrapper
# from plone.app.z3cform.widget import AjaxSelectFieldWidget, AjaxSelectWidget
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
# from Products.CMFPlone.utils import get_top_request
# from Products.CMFPlone.resources import add_resource_on_request
from z3c.form.form import Form
from rer.pubblicazioni import _
from zope import schema
from plone import api
from z3c.form.interfaces import HIDDEN_MODE
from plone.app.vocabularies.catalog import CatalogSource
from plone.app.uuid.utils import uuidToObject


class ISearchForm(Interface):

    text = schema.TextLine(
        required=False,
        title=_('Searchable Text')
    )
    publicationAuthor = schema.Choice(
        required=False,
        title=_(u'rer_pub_author_tags', default=u'Author/Authors'),
        vocabulary="rer.pubblicazioni.used_authors"
    )
    publicationTypes = schema.Choice(
        required=False,
        title=_(u'rer_pub_type', default=u'Pubblication types'),
        vocabulary="rer.pubblicazioni.used_types"
    )

    publicationLanguage = schema.Choice(
        required=False,
        title=_(u'rer_publication_language', default=u'Language'),
        vocabulary="rer.pubblicazioni.used_languages"
    )
    publicationDateFrom = schema.Date(
        required=False,
        title=_(u'rer_publication_date_from', default=u'From date'),
    )
    publicationDateTo = schema.Date(
        required=False,
        title=_(u'rer_publication_date_to', default=u'To date'),
    )
    portal_type = schema.TextLine(
        required=True,
        title=_(u'portal_type', default=u'Portal type')
    )

    search_path = schema.TextLine(
        required=False,
        title=_(u'search_path', default=u'/')
    )


class SearchForm(Form):

    fields = field.Fields(ISearchForm)
    label = _(u'Search for pubblications')
    ignoreContext = True

    def updateWidgets(self):
        # self.fields['publicationAuthor'].widgetFactory = AjaxSelectFieldWidget
        # self.fields['publicationTypes'].widgetFactory = AjaxSelectFieldWidget
        super(SearchForm, self).updateWidgets()
        self.widgets['text'].name = 'SearchableText'
        self.widgets['publicationAuthor'].name = 'authors'
        self.widgets['publicationTypes'].name = 'publication_types'
        self.widgets['publicationLanguage'].name = 'publication_language'
        self.widgets['publicationDateFrom'].name = 'start'
        self.widgets['publicationDateTo'].name = 'end'
        self.widgets['portal_type'].name = 'portal_type'
        self.widgets['portal_type'].value = 'Pubblicazione'
        self.widgets['portal_type'].mode = HIDDEN_MODE
        self.widgets['search_path'].name = 'search_path'
        # print "\n\n"
        # print self.search_path
        # print "\n\n"
        # self.widgets['search_path'].value = 'Percorso'
        self.widgets['search_path'].mode = HIDDEN_MODE

    @button.buttonAndHandler(_(u'Search', default='Search'))
    def handleApply(self, action):
        data, errors = self.extractData()

        if errors:
            return

    @property
    def action(self):
        baseurl = "/@@search?portal_type=Pubblicazione"
        portalurl = api.portal.get().absolute_url()
        return portalurl + baseurl


class TileFormViewer(FormWrapper):

    form = SearchForm
    index = ViewPageTemplateFile("templates/search_form.pt")

    def get_error_message(self):
        return self.context.translate(
            _(u'End date should be great than start date')
        )


class SearchPubblicazioni(Tile):
    """
    Tile for pubblicazioni search on site
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.form_wrapper = self.create_form()

    def create_form(self):
        context = self.context.aq_inner
        # reutrnURL = self.context.absolute_url()
        form = SearchForm(context, self.request)
        form.search_path = self.data.get('search_path', '')
        view = TileFormViewer(context, self.request)
        view = view.__of__(context)
        view.form_instance = form
        return view

    def searchone(self):
        search_path = self.data.get('search_path', '')
        if search_path:
            return search_path


class TileDiProva(Tile):
    """
    Nuova Tile per la ricerca di pubblicazioni nel sito
    """

    def searchone(self):
        search_path = self.data.get('search_path', '')
        # self.search_path = self.data.get('search_path', '')
        obj = uuidToObject(self.data.get('search_path', ''))
        self.path = '/'.join(obj.getPhysicalPath())
        import pdb; pdb.set_trace()
        if search_path:
            return search_path
