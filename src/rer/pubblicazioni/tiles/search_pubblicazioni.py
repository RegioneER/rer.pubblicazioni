# -*- coding: utf-8 -*-
# from zope.interface import implements
from z3c.form import field
from plone.tiles import Tile
from zope.interface import Interface
from plone.autoform import directives
from plone.z3cform.layout import FormWrapper
from plone.app.z3cform.widget import AjaxSelectFieldWidget, AjaxSelectWidget
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import get_top_request
from Products.CMFPlone.resources import add_resource_on_request
from z3c.form.form import Form
from rer.pubblicazioni import _
from zope import schema


class ISearchForm(Interface):

    text = schema.TextLine(
        required=False,
        title=_('Searchable Text')
    )
    publicationAuthor = schema.Tuple(
        title=_(u'rer_pub_author_tags', default=u'Author/authors'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'publicationAuthor',
        AjaxSelectFieldWidget,
        vocabulary='rer.pubblicazioni.autori'
    )
    publicationTypes = schema.Tuple(
        title=_(u'rer_pub_type', default=u'Pubblication types'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'publicationTypes',
        AjaxSelectFieldWidget,
        vocabulary='rer.pubblicazioni.tipologie'
    )

    publicationLanguage = schema.Choice(
        required=False,
        title=_(u'rer_publication_language', default=u'Language'),
        vocabulary="rer.pubblicazioni.lingue"
    )
    publicationDateFrom = schema.Date(
        required=False,
        title=_(u'rer_publication_date_from', default=u'From date'),
    )
    publicationDateTo = schema.Date(
        required=False,
        title=_(u'rer_publication_date_to', default=u'To date'),
    )


class SearchForm(Form):

    fields = field.Fields(ISearchForm)
    label = _(u'Search for pubblications')
    ignoreContext = True

    def updateWidgets(self):
        self.fields['publicationAuthor'].widgetFactory = AjaxSelectFieldWidget
        self.fields['publicationTypes'].widgetFactory = AjaxSelectFieldWidget
        super(SearchForm, self).updateWidgets()


class TileFormViewer(FormWrapper):

    form = SearchForm
    index = ViewPageTemplateFile("templates/search_form.pt")


class SearchPubblicazioni(Tile):
    """
    Tile for pubblicazioni search on site
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.form_wrapper = self.create_form()

    def __call__(self):
        top_request = get_top_request(self.request)
        add_resource_on_request(top_request, 'select2')
        return super(SearchPubblicazioni, self).__call__()

    def create_form(self):

        context = self.context.aq_inner
        # reutrnURL = self.context.absolute_url()
        form = SearchForm(context, self.request)
        view = TileFormViewer(context, self.request)
        view = view.__of__(context)
        view.form_instance = form
        return view
