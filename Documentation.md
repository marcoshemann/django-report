# URLs #

Create a file named "report\_urls.py" within your app directory.

From there you can add new URLs that will be appended to the main report URL.

For this example I created a simple action log report with a generic view:

```

# -*- coding: utf-8 -*-

import datetime, imp
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.date_based import archive_year
from django.contrib.admin.models import LogEntry

queryset    = LogEntry.objects.all()
report_conf = settings.REPORT_CONF
report_conf['title'] = 'Admin action log (%d total)' % len(queryset)

urlpatterns = patterns('',
    url(r'^actions/$', archive_year, {
        'year':             datetime.datetime.now().year,
        'date_field':       'action_time',
        'make_object_list': True,
        'queryset':         queryset,
        'template_name':    'myapp/actions.html',
        'extra_context':    settings.REPORT_CONF,
    },name='reports-actions'),
) 
```

Here's the `mayapp/actions.html` template:

```
{% extends "report/base.html" %}
{% block report.content %}
{% for period in date_list %}
<h2>{{ period|date:"F" }}</h2>
<table class="report-list" cellpadding="0" cellspacing="0">
    <thead>
        <tr>
            <th>Action</th>
            <th>User</th>
            <th>Object type</th>
            <th>Date</th>
        </tr>
    </thead>
    <tbody>
        {% for object in object_list %}
        {% ifequal object.action_time.month period.month %}
        <tr>
            <td>{{ object.object_repr }}</td>
            <td style="width:50px;">{{ object.user }}</td>
            <td style="width:80px;">{{ object.content_type }}</td>
            <td style="width:140px;">{{ object.action_time }}</td>
        </tr>
        {% endifequal %}
        {% endfor %}
    </tbody>
</table>
{% endfor %}
{% endblock %}
```

## Template tags ##

Django-report provides template tags that interface the pisa API, load it using `{% load report %}`

Example usage that generates a barcode (only in the PDF output):

```

{% barcode "1234567891012" %}

```

### Available template tags ###

| tag | arguments |
|:----|:----------|
| pagenumber`*` | example   |
| nexttemplate | name      |
| nextpage | name      |
| nextframe | -         |
| spacer | height    |
| toc | -         |
| fontembed | name, src |
| barcode | value, align |

`*` There is a known issue with pagenumber. If you get duplicated page numbers (ex: 11 instead of 1), put the pagenumber tag on it's own line. ([more info](http://groups.google.com/group/xhtml2pdf/browse_frm/thread/46dfce4237310c15/ddb44fff0c6))




## Output screenshots ##

### HTML ###

![http://i.imgur.com/8cRtB.png](http://i.imgur.com/8cRtB.png)

### PDF ###

![http://i.imgur.com/qFNRO.png](http://i.imgur.com/qFNRO.png)