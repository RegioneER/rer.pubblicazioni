# -*- coding: utf-8 -*-

from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.component import getMultiAdapter


@implementer(IVocabularyFactory)
class Lingue(object):
    """Factory creating a 'lingue' vocabulary
    """
    def get_terms(self, context):
        view = getMultiAdapter((context, context.REQUEST),
                               name="rer-pubblicazioni-utils-view")
        if not view.extract_value_from_settings('lingue'):
            terms = [SimpleTerm(title=u'-- aggiungi lingue dal pannello di controllo --', value='')]
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
