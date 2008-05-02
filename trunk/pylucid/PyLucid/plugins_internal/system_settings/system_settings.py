#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
    PyLucid system settings
    ~~~~~~~~~~~~~~~~~~~~~~~

    A pseudo plugin for holding the system settings via the plugin preferences.

    Last commit info:
    ~~~~~~~~~
    $LastChangedDate$
    $Rev$
    $Author: JensDiemer $

    :copyright: 2008 by Jens Diemer
    :license: GNU GPL v2 or above, see LICENSE for more details
"""

__version__= "$Rev$"

#from django import newforms as forms
#from django.utils.translation import ugettext as _
#from django.utils.safestring import mark_safe

from PyLucid.system.BasePlugin import PyLucidBasePlugin
from PyLucid.models import Page


class system_settings(PyLucidBasePlugin):
    def lucidTag(self):
        """
        TODO!
        """
        self.page_msg("Preferences:", preferences)
