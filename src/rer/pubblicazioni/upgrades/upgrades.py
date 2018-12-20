# -*- coding: utf-8 -*-

from plone import api
from rer.pubblicazioni import logger
import transaction


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


def fix_author_field(context):
    """ A list of authors has to be written a name at a time, not copy-pasting
    a list of names separated by commas (e.g. "M.Rossi, F.Bianchi").
    We fix this issue with this upgrade step.
    """

    logger.info('Fix wrongly filled authors field')

    pubs_changed = 0
    split_detected = False
    detected = []

    site = api.portal.get()
    logger.info(u"Getting all the pubblications objects in the site...")
    pub_brains = site.portal_catalog.unrestrictedSearchResults(
        portal_type=["Pubblicazione"],
    )
    logger.info(u"Found {} pubblications".format(len(pub_brains)))
    logger.info(u"Checkin all the pubblications...")
    for brain in pub_brains:
        pube = brain.getObject()
        if pube.publicationAuthor:
            names = []
            for stringa in pube.publicationAuthor:
                if "," in stringa:
                    detected.append(stringa)
                    split_detected = True
                    logger.info(u"{} has this authors: {}".format(
                        pube.absolute_url(),
                        stringa,
                    ))
                    for name in stringa.split(','):
                        if name.strip():
                            names.append(name.strip())

                names.append(stringa)

            try:
                if split_detected:
                    for bad_string in detected:
                        del names[names.index(bad_string)]
            except ValueError as err:
                logger.error(err)

            pube.publicationAuthor = tuple(names)
            logger.info(u"{} new authors: {}".format(
                pube.absolute_url(),
                tuple(names),
            ))
            pube.reindexObject(idxs=['authors'])
            logger.info(
                'Fixing authors for {}'.format(pube.absolute_url())
            )
            pubs_changed += 1
            split_detected = False
            detected = []

            if pubs_changed > 10:
                try:
                    print "Partial Commit..."
                    transaction.commit()
                    print "Partial Commit: OK"
                except Exception as e:
                    logger.error(
                        u"Error while committing transaction.")
                    logger.error(u"{}".format(e))
                pubs_changed = 0
