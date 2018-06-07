# -*- coding: utf-8 -*-

from BTrees.IIBTree import intersection
from plone.app.layout.navigation.root import getNavigationRootObject
from plone.app.vocabularies.terms import safe_encode
from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from zope.component import getMultiAdapter
from zope.component import queryUtility
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.site.hooks import getSite
from plone import api


@implementer(IVocabularyFactory)
class Lingue(object):
    """Factory creating a 'lingue' vocabulary
    """
    def get_terms(self, context):
        view = getMultiAdapter((context, context.REQUEST),
                               name="rer-pubblicazioni-utils-view")
        if not view.extract_value_from_settings('lingue'):
            terms = [SimpleTerm(
                title=u'-- aggiungi lingue dal pannello di controllo --',
                value='')]
            return terms
        terms = [SimpleTerm(title=value,
                            value=value)
                 for value in
                 view.extract_value_from_settings('lingue').split('\r\n')
                 ]
        # terms.insert(0, SimpleTerm(title=u'-- select a value --', value=''))
        return terms

    def __call__(self, context):
        terms = self.get_terms(context)
        return SimpleVocabulary(terms)


@implementer(IVocabularyFactory)
class Tipologie(object):
    """Factory creating a 'lingue' vocabulary
    """
    def get_terms(self, context):
        view = getMultiAdapter((context, context.REQUEST),
                               name="rer-pubblicazioni-utils-view")
        if not view.extract_value_from_settings('tipologie'):
            terms = [SimpleTerm(
                title=u'-- aggiungi tipologie dal pannello di controllo --',
                value='')]
            return terms
        terms = [SimpleTerm(title=value.encode('utf-8'),
                            value=value.encode('utf-8'))
                 for value in
                 view.extract_value_from_settings('tipologie').split('\r\n')
                 ]
        # terms.insert(0, SimpleTerm(title=u'-- select a value --', value=''))
        return terms

    def __call__(self, context):
        terms = self.get_terms(context)
        return SimpleVocabulary(terms)


@implementer(IVocabularyFactory)
class KeywordsVocabulary(object):
    # Allow users to customize the index to easily create
    # KeywordVocabularies for other keyword indexes
    keyword_index = 'Autori'
    path_index = 'path'

    def section(self, context):
        """gets section from which subjects are used.
        """
        registry = queryUtility(IRegistry)
        if registry is None:
            return None
        if registry.get('plone.subjects_of_navigation_root', False):
            portal = getToolByName(context, 'portal_url').getPortalObject()
            return getNavigationRootObject(context, portal)
        return None

    def all_keywords(self, kwfilter):
        site = getSite()
        self.catalog = getToolByName(site, 'portal_catalog', None)
        if self.catalog is None:
            return SimpleVocabulary([])
        index = self.catalog._catalog.getIndex(self.keyword_index)
        return safe_simplevocabulary_from_values(index._index, query=kwfilter)

    def keywords_of_section(self, section, kwfilter):
        """Valid keywords under the given section.
        """
        pcat = getToolByName(section, 'portal_catalog')
        cat = pcat._catalog
        path_idx = cat.indexes[self.path_index]
        tags_idx = cat.indexes[self.keyword_index]
        result = []
        # query all oids of path - low level
        pquery = {
            self.path_index: {
                'query': '/'.join(section.getPhysicalPath()),
                'depth': -1,
            }
        }
        kwfilter = safe_encode(kwfilter)
        # uses internal zcatalog specific details to quickly get the values.
        path_result, info = path_idx._apply_index(pquery)
        for tag in tags_idx.uniqueValues():
            if kwfilter and kwfilter not in safe_encode(tag):
                continue
            tquery = {self.keyword_index: tag}
            tags_result, info = tags_idx._apply_index(tquery)
            if intersection(path_result, tags_result):
                result.append(tag)
        # result should be sorted, because uniqueValues are.
        return safe_simplevocabulary_from_values(result)

    def __call__(self, context, query=None):
        section = self.section(context)
        if section is None:
            return self.all_keywords(query)
        return self.keywords_of_section(section, query)


KeywordsVocabularyFactory = KeywordsVocabulary()


class BaseIndexValuesVocabulary(object):

    def __call__(self, context):
        portal = api.portal.get()
        pc = getToolByName(portal, 'portal_catalog')

        values = pc.uniqueValuesFor(self.INDEX)
        values = sorted(values)
        terms = [SimpleTerm(title=value.encode('utf-8'), value=value.encode('utf-8')) for value in values if value]
        return SimpleVocabulary(terms)


@implementer(IVocabularyFactory)
class PublicationUsedLanguagesVocabulary(BaseIndexValuesVocabulary):

    INDEX = 'publication_language'


PublicationUsedLanguagesVocabularyFactory = PublicationUsedLanguagesVocabulary()


@implementer(IVocabularyFactory)
class PublicationUsedAuthorsVocabulary(BaseIndexValuesVocabulary):

    INDEX = 'authors'


PublicationUsedAuthorsVocabularyFactory = PublicationUsedAuthorsVocabulary()


@implementer(IVocabularyFactory)
class PublicationUsedTypesVocabulary(BaseIndexValuesVocabulary):

    INDEX = 'publication_types'


PublicationUsedTypesVocabularyFactory = PublicationUsedTypesVocabulary()
