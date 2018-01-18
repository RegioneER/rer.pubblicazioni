# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.app.textfield import RichText
from plone.app.z3cform.widget import AjaxSelectFieldWidget
from plone.autoform import directives
from plone.namedfile.field import NamedFile
from rer.pubblicazioni import _
from zope import schema
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IRerPubblicazioniLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IPubblicazione(Interface):

    abstract = RichText(
        title=_(u'rer_description_abstract', default=u'Description/Abstract'),
        description=_(
            u'help_rer_description_abstract',
            default=u'An abstract of the publication.'
        ),
        required=False,
    )

    publicationAuthor = schema.Tuple(
        title=_(u'rer_pub_author_tags', default=u'Author/Authors'),
        description=_(
            u'help_rer_pub_author_tags',
            default=u'Autore/autori della pubblicazione',
        ),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
    )
    directives.widget(
        'publicationAuthor',
        AjaxSelectFieldWidget,
        vocabulary='rer.pubblicazioni.autori'
    )

    publicationDate = schema.Date(
        title=_(u'rer_publication_date', default=u'Publication date'),
        description=_(
            u'help_rer_publication_date',
            default=u'Insert the date for this publication'
        ),
        required=True,
    )

    publicationType = schema.List(
        title=_(u'rer_publication_type', default=u'Publication type'),
        description=_(
            u'help_rer_publication_type',
            default=u'Insert a list of types for this publication'
        ),
        required=False,
        default=[],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary='rer.pubblicazioni.tipologie'
        )
    )

    publicationLanguage = schema.Choice(
        title=_(u'rer_publication_language', default=u'Language'),
        description=_(
            u'help_rer_publication_language',
            default=u'Select the language of this publication'
        ),
        required=False,
        default=None,
        vocabulary="rer.pubblicazioni.lingue"
    )

    # "Pubblicato in" - era "Collana"
    publicationSeries = schema.Text(
        title=_(u'rer_published_in', default=u'Published in'),
        description=_(
            u'help_rer_publication_series',
            default=u''
        ),
        required=False,
    )

    publicationEditor = schema.Text(
        title=_(u'rer_publication_editor', default=u'Editor'),
        description=_(
            u'help_rer_publication_editor',
            default=u''
        ),
        required=False,
    )

    publicationRights = schema.Text(
        title=_(u'rer_publication_rights', default=u'Copyrights'),
        description=_(
            u'help_rer_rer_publication_rights',
            default=u''
        ),
        required=False,
    )

    publicationFile = NamedFile(
        title=_(u'rer_publication_file', default=u'File'),
        description=_(
            u'help_rer_publication_file',
            default=u''
        ),
        required=False,
    )

    publicationURL = schema.TextLine(
        title=_(u'rer_publication_url', default=u'URL'),
        description=_(
            u'help_rer_publication_url',
            default=u''
        ),
        default=u"http://",
        required=False,
    )
