#!/usr/bin/env python

from SettingsWidgets import *
from gi.repository import Gio

class Module:
    def __init__(self, content_box):
        keywords = _("desktop, home, button, trash")
        advanced = False
        sidePage = SidePage(_("Desktop"), "desktop.svg", keywords, advanced, content_box)
        self.sidePage = sidePage
        self.name = "desktop"
        self.category = "prefs"

    def _loadCheck(self):
        if 'org.gnome.nautilus' in Gio.Settings.list_schemas():
            nautilus_desktop_schema = Gio.Settings.new("org.gnome.nautilus.desktop")
            nautilus_desktop_keys = nautilus_desktop_schema.list_keys()
            if "computer-icon-visible" in nautilus_desktop_keys:
                self.sidePage.add_widget(GSettingsCheckButton(_("Show a computer icon"), "org.gnome.nautilus.desktop", "computer-icon-visible", None))
            if "home-icon-visible" in nautilus_desktop_keys:
                self.sidePage.add_widget(GSettingsCheckButton(_("Show a home icon"), "org.gnome.nautilus.desktop", "home-icon-visible", None))
            if "trash-icon-visible" in nautilus_desktop_keys:
                self.sidePage.add_widget(GSettingsCheckButton(_("Show the trash"), "org.gnome.nautilus.desktop", "trash-icon-visible", None))
            if "volumes-visible" in nautilus_desktop_keys:
                self.sidePage.add_widget(GSettingsCheckButton(_("Show mounted volumes"), "org.gnome.nautilus.desktop", "volumes-visible", None))
            if "network-icon-visible" in nautilus_desktop_keys:
                self.sidePage.add_widget(GSettingsCheckButton(_("Show network servers"), "org.gnome.nautilus.desktop", "network-icon-visible", None))
            return True
        else:
            return False

