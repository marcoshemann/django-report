# -*- coding: utf-8 -*-

import datetime, imp
from django.conf.urls.defaults import *
from django.conf import settings
from reports.views import *
from django.views.generic.date_based import archive_year
from django.contrib.admin.models import LogEntry

#REPORT_CONF = {
#    'base_title':           u'Report: ',
#    'toolbar_back_txt':     u'&laquo; Retour',
#    'toolbar_download_txt': u'Télécharger PDF',
#    'report_title':         u"Untitled report",
#}

urlpatterns = patterns('',
    url(r'^actions/$', archive_year, {
        'year': datetime.datetime.now().year,
        'date_field': 'action_time',
        'make_object_list': True,
        'queryset': LogEntry.objects.all(),
        'template_name': 'report/actions.html',
        'extra_context': settings.REPORT_CONF,
    },name='reports-actions'),
) 


from django.utils.importlib import import_module
for app in settings.INSTALLED_APPS:
    try:
        app_path = import_module(app).__path__
    except AttributeError:
        continue
    try:
        imp.find_module('report_urls', app_path)
    except ImportError:
        continue
        
    urlpatterns += patterns('',
        (r'^%s/' % app, include('%s.report_urls' % app)),
    )
