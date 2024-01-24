# -*- coding: utf-8 -*-
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.supermodel import model
from zope import schema


class IRerPubblicazioniSettings(model.Schema):
    lingue = schema.Text(
        title="Lingue", description="Lingue per le pubblicazioni", required=False
    )

    tipologie = schema.Text(
        title="Tipologie", description="Tipologie delle pubblicazioni", required=False
    )


class RerPubblicazioniSettingsEditForm(RegistryEditForm):
    schema = IRerPubblicazioniSettings
    label = "Configurazione Pubblicazioni"


class RerPubblicazioniSettingsView(ControlPanelFormWrapper):
    """This is the actual view that get called in the control panel."""

    form = RerPubblicazioniSettingsEditForm
