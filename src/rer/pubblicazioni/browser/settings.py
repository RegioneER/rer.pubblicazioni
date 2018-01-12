# -*- coding: utf-8 -*-

from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.supermodel import model
from z3c.form import field
from z3c.form import group
from zope import schema


class IRerPubblicazioniLingueSettings(model.Schema):
    """ Settaggio per le lingue delle pubblicazioni.
    """

    lingue = schema.Text(
        title=u"Lingue",
        description=u"Lingue per le pubblicazioni",
        required=False)


class IRerPubblicazioniTipologieSettings(model.Schema):
    """ Settaggio per le lingue delle pubblicazioni.
    """

    tipologie = schema.Text(
        title=u"Tipologie",
        description=u"Tipologie delle pubblicazioni",
        required=False)


class IRerPubblicazioniSettings(IRerPubblicazioniLingueSettings,
                                IRerPubblicazioniTipologieSettings):
    """
    Marker interface for settings.
    It's this class that is registered in registry.xml.
    """


class FormLingue(group.Group):
    label = u"Lingue"
    fields = field.Fields(IRerPubblicazioniLingueSettings)


class FormTipologie(group.Group):
    label = u"Tipologie"
    fields = field.Fields(IRerPubblicazioniTipologieSettings)


class RerPubblicazioniSettingsEditForm(RegistryEditForm):

    schema = IRerPubblicazioniSettings
    groups = (FormLingue, FormTipologie)
    label = u"Configurazione Pubblicazioni"


class RerPubblicazioniSettingsView(ControlPanelFormWrapper):
    """ This is the actual view that get called in the control panel.
    """
    form = RerPubblicazioniSettingsEditForm
