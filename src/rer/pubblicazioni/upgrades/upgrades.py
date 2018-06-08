# -*- coding: utf-8 -*-

from plone import api
from rer.pubblicazioni import logger


DEFAULT_PROFILE = 'profile-rer.pubblicazioni:default'


def import_registry(registry_id, dependencies=False):
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile(DEFAULT_PROFILE, registry_id,
                                        run_dependencies=dependencies)


def import_js_registry(context):
    'Import js registry configuration'
    logger.info('Importing js registry configuration for ' +
                'rer.agidtheme.base')
    import_registry('jsregistry')


def import_css_registry(context):
    'Import CSS registry configuration'
    logger.info('Importing CSS registry configuration for ' +
                'rer.agidtheme.base')
    import_registry('cssregistry')
